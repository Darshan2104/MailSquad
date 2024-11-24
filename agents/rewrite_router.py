from agents import ChatPromptTemplate,PromptTemplate,StrOutputParser,JsonOutputParser
from agents import BaseAgent 

class RewriterRouterAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are an expert at evaluating the emails that are draft emails for the customer and deciding if they
            need to be rewritten to be better. \n

            Use the following criteria to decide if the DRAFT_EMAIL needs to be rewritten: \n\n

            If the INITIAL_EMAIL only requires a simple response which the DRAFT_EMAIL contains then it doesn't need to be rewritten.
            If the DRAFT_EMAIL addresses all the concerns of the INITIAL_EMAIL then it doesn't need to be rewritten.
            If the DRAFT_EMAIL is missing information that the INITIAL_EMAIL requires then it needs to be rewritten.

            Give a binary choice 'rewrite' (for needs to be rewritten) or 'no_rewrite' (for doesn't need to be rewritten) based on the DRAFT_EMAIL and the criteria.
            Return the a JSON with a single key 'router_decision' and no premable or explaination. \
            <|eot_id|><|start_header_id|>user<|end_header_id|>
            INITIAL_EMAIL: {initial_email} \n
            EMAIL_CATEGORY: {email_category} \n
            DRAFT_EMAIL: {draft_email} \n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            input_variables=["initial_email","email_category","draft_email"],
        )
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def rewrite_router(self, initial_email, email_category, draft_email):
        return self.chain.invoke({"initial_email": initial_email, "email_category":email_category, "draft_email":draft_email})