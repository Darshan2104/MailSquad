from agents import ChatPromptTemplate,PromptTemplate,StrOutputParser,JsonOutputParser
from agents import BaseAgent 

class DraftAnalysisAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are the Quality Control Agent read the INITIAL_EMAIL below  from a human that has emailed \
            our company email address, the email_category that the categorizer agent gave it and the \
            research from the research agent and write an analysis of how the email.

            Check if the DRAFT_EMAIL addresses the customer's issued based on the email category and the \
            content of the initial email.\n

            Give feedback of how the email can be improved and what specific things can be added or change\
            to make the email more effective at addressing the customer's issues.

            You never make up or add information that hasn't been provided by the research_info or in the initial_email.

            Return the analysis a JSON with a single key 'draft_analysis' and no premable or explaination.

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            INITIAL_EMAIL: {initial_email} \n\n
            EMAIL_CATEGORY: {email_category} \n\n
            RESEARCH_INFO: {research_info} \n\n
            DRAFT_EMAIL: {draft_email} \n\n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            input_variables=["initial_email","email_category","research_info"],
        )

        self.chain = self.prompt | self.llm | JsonOutputParser()

    def draft_analysis(self, initial_email, email_category, research_info, draft_email):
        return self.chain.invoke({"initial_email": initial_email,
                                 "email_category":email_category,
                                 "research_info":research_info,
                                 "draft_email": draft_email})