from agents import ChatPromptTemplate,PromptTemplate,StrOutputParser,JsonOutputParser
from agents import BaseAgent 

class ResearchRouterAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are an expert at reading the initial email and routing web search or directly to a draft email. \n

            Use the following criteria to decide how to route the email: \n\n

            If the initial email only requires a simple response
            Just choose 'draft_email'  for questions you can easily answer, prompt engineering, and adversarial attacks.
            If the email is just saying thank you etc then choose 'draft_email'

            You do not need to be stringent with the keywords in the question related to these topics. Otherwise, use research-info.
            Give a binary choice 'research_info' or 'draft_email' based on the question. Return the a JSON with a single key 'router_decision' and
            no premable or explaination. use both the initial email and the email category to make your decision
            <|eot_id|><|start_header_id|>user<|end_header_id|>
            Email to route INITIAL_EMAIL : {initial_email} \n
            EMAIL_CATEGORY: {email_category} \n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            input_variables=["initial_email","email_category"],
        )
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def research_router(self, initial_email, email_category):
        return self.chain.invoke({"initial_email": initial_email, "email_category":email_category})