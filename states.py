from langchain.schema import Document
from langgraph.graph import END, StateGraph

from typing_extensions import TypedDict
from typing import List
from nodes import (
    categorize_email,
    research_info_search,
    state_printer,
    draft_email_writer,
    analyze_draft_email,
    rewrite_email,
    no_rewrite
)
from edges import (
    route_to_research,
    route_to_rewrite
)
### State

class GraphState(TypedDict):
    """
    Represents the state of our graph.
    Attributes:
        initial_email: email
        email_category: email category
        draft_email: LLM generation
        final_email: LLM generation
        research_info: list of documents
        info_needed: whether to add search info
        num_steps: number of steps
    """
    initial_email : str
    email_category : str
    draft_email : str
    final_email : str
    research_info : List[str]
    # info_needed : bool
    num_steps : int
    draft_email_feedback : dict

# INITIALIZE THE GRAPH
workflow = StateGraph(GraphState)

# Define the nodes in the GRAPH
workflow.add_node("categorize_email", categorize_email) # categorize email
workflow.add_node("research_info_search", research_info_search) # web search
workflow.add_node("state_printer", state_printer)
workflow.add_node("draft_email_writer", draft_email_writer)
workflow.add_node("analyze_draft_email", analyze_draft_email)
workflow.add_node("rewrite_email", rewrite_email)
workflow.add_node("no_rewrite", no_rewrite)


# ADD THE EDGES in THE GRAPH
workflow.set_entry_point("categorize_email")

# 1. conditional edge : use edge route_to_research to decide if we need to search for research_info or write a draft email
workflow.add_conditional_edges(
    "categorize_email",
    route_to_research,
    {
        "research_info": "research_info_search",
        "draft_email": "draft_email_writer",
    },
)
workflow.add_edge("research_info_search", "draft_email_writer")

# 2. conditional edge : use edge route_to_rewrite to decide if we need to rewrite the email or not
workflow.add_conditional_edges(
    "draft_email_writer",
    route_to_rewrite,
    {
        "rewrite": "analyze_draft_email",
        "no_rewrite": "no_rewrite",
    },
)

workflow.add_edge("no_rewrite", "state_printer")
workflow.add_edge("analyze_draft_email", "rewrite_email")
workflow.add_edge("rewrite_email", "state_printer")

workflow.add_edge("state_printer", END)

# Compile
app = workflow.compile()