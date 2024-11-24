from agents import ChatPromptTemplate,PromptTemplate,StrOutputParser,JsonOutputParser
from agents import BaseAgent 

class EmailCategorizerAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm)
        self.prompt = PromptTemplate(
            template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
            You are a Email Categorizer Agent You are a master at understanding what a customer wants when they write an email and are able to categorize it in a useful way

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            Conduct a comprehensive analysis of the email provided and categorize into one of the following categories:
                price_equiry - used when someone is asking for information about pricing \
                customer_complaint - used when someone is complaining about something \
                product_enquiry - used when someone is asking for information about a product feature, benefit or service but not about pricing \\
                customer_feedback - used when someone is giving feedback about a product \
                off_topic when it doesnt relate to any other category \


                    Output a single cetgory only from the types ('price_equiry', 'customer_complaint', 'product_enquiry', 'customer_feedback', 'off_topic') \
                    eg:
                    'price_enquiry' \

            EMAIL CONTENT:\n\n {initial_email} \n\n
            <|eot_id|>
            <|start_header_id|>assistant<|end_header_id|>
            """,
            input_variables=["initial_email"],
        )

        self.chain = self.prompt | self.llm | StrOutputParser()

    def categorize(self, initial_email):
        return self.chain.invoke({"initial_email": initial_email})