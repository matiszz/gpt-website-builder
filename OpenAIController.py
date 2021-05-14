import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIController(object):

    def __init__(self):
        print("OpenAI Controller created")

    def foo(self):
        response = openai.Completion.create(
            engine="davinci",
            prompt="Write a creative ad for the following product to run on Facebook:\n\"\"\"\"\"\"\nAiree is a line "
                   "of skin-care products for young women with delicate skin. The ingredients are "
                   "all-natural.\n\"\"\"\"\"\"\nThis is the ad I wrote for Facebook aimed at teenage "
                   "girls:\n\"\"\"\"\"\"",
            temperature=0.5,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\"\"\"\"\"\""]
        )
        print(response)
