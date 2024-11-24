import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

GROQ_API = os.getenv('GROQ_API')
TAVILY_API = os.getenv('TAVILY_API')

os.environ["GROQ_API_KEY"] = GROQ_API
os.environ["TAVILY_API_KEY"] = TAVILY_API


GROQ_LLM = ChatGroq(
            model="llama3-70b-8192",
        )


# from agents import EmailCategorizerAgent, ResearchRouterAgent
       
from utils import write_markdown_file
    # ... (Import necessary libraries and set up environment variables) ...

def main():
    # 1. Initialize Agents:
    email_categorizer = EmailCategorizerAgent(GROQ_LLM)
    research_router = ResearchRouterAgent(GROQ_LLM)
    # ... Initialize other agents ...

    # 2. Process Email:
    email_category = email_categorizer.categorize(EMAIL)
    # ... Continue with the rest of your workflow logic ...

if __name__ == "__main__":
    # main()
    from agents import EmailCategorizerAgent
    EMAIL = """HI there, \n
        I am emailing to say that I had a wonderful stay at your resort last week. \n

        I really appreaciate what your staff did

        Thanks,
        Paul
        """
    cat = EmailCategorizerAgent(GROQ_LLM)
    res = cat.categorize(EMAIL)
    print(res)
