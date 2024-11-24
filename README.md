# MailSquad: Email Automation with AgentSquad

## Overview

**MailSquad** is an advanced email automation tool that leverages the power of **LangGraph**  and **LLM Agents** to create customizable, graph-based workflows for handling email-related tasks. This project is designed to help users automate tasks such as categorizing emails, researching information, drafting email content, and more.


### File Structure

```
langgraph-project/
├── README.md                 # Project overview and setup instructions
├── requirements.txt          # Dependencies for the project
├── .env                      # Environment variables (optional)
├── src/                      # Main source code
│   ├── __init__.py
│   ├── agents/               # Custom agents and workflows
│   │   ├── __init__.py
│   │   ├── base_agent.py     # Base agent implementation
│   │   ├── conversational_agent.py  # Example agent
│   └── pipelines/            # Graph-based pipelines and utilities
│       ├── __init__.py
│       ├── langgraph_pipeline.py    # Main LangGraph pipeline logic
│   ├── tools/                # Custom tools for the agents
│       ├── __init__.py
│       ├── search_tool.py    # Example: Search functionality
│       ├── math_tool.py      # Example: Mathematical utilities
│   ├── utils/                # Helper functions
│       ├── __init__.py
│       ├── logger.py         # Logging utilities
│       ├── config_loader.py  # Configuration management
│   ├── app.py                # Main entry point for running the project
├── tests/                    # Unit and integration tests
│   ├── __init__.py
│   ├── test_agents.py        # Test cases for agents
│   ├── test_pipeline.py      # Test cases for LangGraph pipelines
│   ├── test_tools.py         # Test cases for tools
└── configs/                  # Configuration files
    ├── langgraph_config.yaml # Pipeline-specific configurations
    ├── agent_config.yaml     # Configuration for agents

```

### LangGraph Pipeline:
- Define State
- Define Nodes
- Define Conditional Edges

-> Build Graph
    - Add nodes
    - Add edges
    - Compile workflow
    - Boom! it is ready to invoke!

### Nodes
1. categorize_email
2. research_info_search
3. draft_email_writer
4. analyze_draft_email
5. rewrite_email
6. no_rewrite
7. state_printer


### TODO: 
- For each task, instead of calling LLM, Make it configurable!
    - For example, for categorization, instead of using LLM, I should be able to use any classical ML model!
- Add RAG for information retirval along with option of internet search
