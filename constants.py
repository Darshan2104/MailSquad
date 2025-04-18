import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

from agents import EmailCategorizerAgent, ResearchRouterAgent, SearchKeywordAgent
from agents import DraftWriterAgent, RewriterRouterAgent, DraftAnalysisAgent,FinalEmailWriterAgent

GROQ_API = os.getenv('GROQ_API_KEY')
TAVILY_API = os.getenv('TAVILY_API_KEY')

os.environ["GROQ_API_KEY"] = GROQ_API
os.environ["TAVILY_API_KEY"] = TAVILY_API


GROQ_LLM = ChatGroq(
            model="llama3-70b-8192",
            )

# 1. Categorize email
email_categorizer = EmailCategorizerAgent(GROQ_LLM)

# 2. Research Router :
research_route_decider = ResearchRouterAgent(GROQ_LLM)

# 3. Search for keyworkds : 
keyword_searcher =SearchKeywordAgent(GROQ_LLM)

# 4. Write a draft email :
drafter = DraftWriterAgent(GROQ_LLM)

# 5. Rewrite the email :
rewrite_decider = RewriterRouterAgent(GROQ_LLM)

# 6. draft email analysis :
draft_analyzer =DraftAnalysisAgent(GROQ_LLM)

# 7. rewrite the email with analysis
final_mail_writer = FinalEmailWriterAgent(GROQ_LLM)

if __name__ == "__main__":
    pass
    # 1. categorize email
    # cat = EmailCategorizerAgent(GROQ_LLM)
    # res = cat.categorize(EMAIL)
    # print(res)

    # 2. Research Router :
    # Take email and email_category and return what it should do ->  'research_info' or 'draft_email'    
    # router=ResearchRouterAgent(GROQ_LLM)
    # ans = router.research_router(EMAIL, email_category)
    # print(ans)

    # 3. Search for keyworkds : 
    # Return us a list of keywords from email based on the email_category
    # search =SearchKeywordAgent(GROQ_LLM)
    # keywords = search.search_keyword(EMAIL, email_category)
    # print(keywords)

    # 4. Write a draft email :

    # draft = DraftWriterAgent(GROQ_LLM)
    # ans = draft.draft_writer(EMAIL, email_category, research_info)
    # print(ans)

    # 5. Rewrite the email :
    # Take the email and the draft email and return if it needs to be rewritten or not
    
    # rewriter = RewriterRouterAgent(GROQ_LLM)
    # ans = rewriter.rewrite_router(EMAIL,email_category, draft_email)
    # print(ans)

    # 6. draft email analysis :
    # analysis =DraftAnalysisAgent(GROQ_LLM)
    # ana =analysis.draft_analysis(EMAIL, email_category, research_info, draft_email)
    # print(ana)
    
    
    # 7. rewrite the email with analysis
    # finalWriter = FinalEmailWriterAgent(GROQ_LLM)
    # ans = finalWriter.final_email(EMAIL, email_category, research_info, draft_email, email_analysis)
    # print(ans)


