from agents import ChatPromptTemplate,PromptTemplate,StrOutputParser,JsonOutputParser
from agents import BaseAgent 

class DraftWriterAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are the Email Writer Agent take the INITIAL_EMAIL below from a human that has emailed our company email address, 
            the email_category that the categorizer agent gave it and the research from the research agent and 
            write a helpful email in a thoughtful and friendly way.

            If the customer email is 'off_topic' then ask them questions to get more information.
            If the customer email is 'customer_complaint' then try to assure we value them and that we are addressing their issues.
            If the customer email is 'customer_feedback' then try to assure we value them and that we are addressing their issues.
            If the customer email is 'product_enquiry' then try to give them the info the researcher provided in a succinct and friendly way.
            If the customer email is 'price_equiry' then try to give the pricing info they requested.

            You never make up information that hasn't been provided by the research_info or in the initial_email.
            Always sign off the emails in appropriate manner and from mr.xyz

            Return the email a JSON with a single key 'email_draft' and no premable or explaination.

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            INITIAL_EMAIL: {initial_email} \n
            EMAIL_CATEGORY: {email_category} \n
            RESEARCH_INFO: {research_info} \n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
            input_variables=["initial_email","email_category","research_info"],
        )
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def draft_writer(self, initial_email:str, email_category:str,research_info:str):
        return self.chain.invoke({"initial_email": initial_email, "email_category":email_category,"research_info":research_info})