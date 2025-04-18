from agents import ChatPromptTemplate,PromptTemplate,JsonOutputParser
from agents import BaseAgent 

class FinalEmailWriterAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are the Final Email Agent read the email analysis below from the QC Agent and 
            use it to rewrite and improve the draft_email to create a final email.

            You never make up or add information that hasn't been provided by the research_info or in the initial_email.

            Return the final email as JSON with a single key 'final_email' which is a string and no premable or explaination.
            
            <|eot_id|><|start_header_id|>user<|end_header_id|>
            EMAIL_CATEGORY: {email_category} \n
            RESEARCH_INFO: {research_info} \n
            DRAFT_EMAIL: {draft_email} \n
            DRAFT_EMAIL_FEEDBACK: {email_analysis} \n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            input_variables=["initial_email",
                            "email_category",
                            "research_info",
                            "email_analysis",
                            "draft_email",
                            ],
        )

        self.chain = self.prompt | self.llm | JsonOutputParser()

    def final_email(self, initial_email, email_category, research_info, draft_email, email_analysis):
        return self.chain.invoke({"initial_email": initial_email,
                                 "email_category":email_category,
                                 "research_info":research_info,
                                 "draft_email": draft_email,
                                "email_analysis":email_analysis})