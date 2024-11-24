from agents import ChatPromptTemplate,PromptTemplate,StrOutputParser,JsonOutputParser
from agents import BaseAgent

class SearchKeywordAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are a master at working out the best keywords to search for in a web search to get the best info for the customer.

            given the INITIAL_EMAIL and EMAIL_CATEGORY. Work out the best keywords that will find the best
            info for helping to write the final email.

            Return a JSON with a single key 'keywords' with no more than 3 keywords and no premable or explaination.

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            INITIAL_EMAIL: {initial_email} \n
            EMAIL_CATEGORY: {email_category} \n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            input_variables=["initial_email","email_category"],
        )
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def search_keyword(self, initial_email, email_category):
        return self.chain.invoke({"initial_email": initial_email, "email_category":email_category})