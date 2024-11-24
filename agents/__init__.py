# __init__.py
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

from agents.base_agent import BaseAgent
from agents.email_categorizer import EmailCategorizerAgent
# Re-export for use in other files
__all__ = [
    "ChatPromptTemplate",
    "PromptTemplate",
    "StrOutputParser",
    "JsonOutputParser",
    "BaseAgent",
    "EmailCategorizerAgent"
]
