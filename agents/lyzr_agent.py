from lyzr import ChatBot


def get_requirements(query):

    bot = ChatBot(
        system_prompt="""
        You are a club management expert.

        Extract:
        - Required skills
        - Experience
        - Leadership qualities

        Return only keywords.
        """
    )

    response = bot.chat(query)

    return str(response)
