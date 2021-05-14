from dotenv import dotenv_values
import openai

openai.api_key = dotenv_values(".env")['OPENAI_API_KEY']

SEPARATOR = "\"\"\"\"\"\""


class OpenAIController(object):

    def __init__(self):
        print("OpenAI Controller created")

    @staticmethod
    def get_tagline(description):
        instruction = "This is a tagline generator for companies."
        example1 = "Company description: Pitch is uncompromisingly good presentation software, enabling modern teams " \
                   "to craft and distribute beautiful presentations more effectively." \
                   "\nTagline: The new face of presentations."
        example2 = "Company description: Testimonial.to allows you to embed video testimonials to your website with " \
                   "no coding to increase conversion on your site.\nTagline: Get video testimonials from your " \
                   "customers with ease"
        completion = "Company description: {}.\nTagline:".format(description)
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + example1 + '\n' + SEPARATOR + '\n' + example2 + '\n' + SEPARATOR + '\n' + completion,
            temperature=0.4,
            max_tokens=30,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.3,
            stop=[SEPARATOR]
        )
        return response.choices[0].text

    @staticmethod
    def get_description(description):
        instruction = "Someone told me about their company:"
        action = "I rephrased it to make it more catchy for a marketing copy:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + '\n' + SEPARATOR + '\n' + description + '\n' + SEPARATOR + '\n' + action + '\n' + SEPARATOR,
            temperature=0.8,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0.4,
            stop=["\"\"\"\"\"\""]
        )
        return response.choices[0].text
