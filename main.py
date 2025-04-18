from constants import email_categorizer
from utils import write_markdown_file
from states import app


if __name__ == "__main__":
   
    EMAIL_1 = """HI there, \n
    I am emailing to find out the current price of doller to inr. \n

    Can you please help me.

    Thanks,
    John
    """

    EMAIL_2 = """HI there, \n
    I am emailing to say that I had a wonderful stay at your resort last week.

    I really appreaciate what your staff did

    Thanks,
    Paul
    """

    EMAIL_3 = """HI there, \n
    I am emailing to say that the resort weather was way to cloudy and overcast.
    I wanted to write a song called 'Here comes the sun but it never came'

    What should be the weather in Goa in April?

    I really hope you fix this next time.

    Thanks,
    George
    """

    # EMAIL_5 = """HI there, \n
    # Thanks for confirming my booking

    # Thanks,
    # Ringo
    # """
    
        # run the agent
    inputs = {"initial_email": EMAIL_2,"research_info": None, "num_steps":0}
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Finished running: {key}:")
    # output = app.invoke(inputs)
    # print(output['final_email'])