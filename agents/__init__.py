# __init__.py
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from agents.base_agent import BaseAgent
from agents.draft_email_analyzer import DraftAnalysisAgent
from agents.draft_email_writer import DraftWriterAgent
from agents.email_categorizer import EmailCategorizerAgent
from agents.final_email_writer import FinalEmailWriterAgent
from agents.research_router import ResearchRouterAgent
from agents.rewrite_router import RewriterRouterAgent
from agents.search_keyword_generator import SearchKeywordAgent
# Re-export for use in other files
__all__ = [
    "ChatPromptTemplate",
    "PromptTemplate",
    "StrOutputParser",
    "JsonOutputParser",
    "BaseAgent",
    "DraftAnalysisAgent",
    "DraftWriterAgent",
    "EmailCategorizerAgent",
    "FinalEmailWriterAgent",
    "ResearchRouterAgent",
    "RewriterRouterAgent",
    "SearchKeywordAgent"
]