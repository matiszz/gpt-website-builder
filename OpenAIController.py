from dotenv import dotenv_values
import openai

openai.api_key = dotenv_values(".env")['OPENAI_API_KEY']

SEPARATOR = "\"\"\"\"\"\""


class OpenAIController(object):

    def __init__(self):
        print("OpenAI Controller created")

    ### HELPERS ###
    @staticmethod
    def list2string(list_of_strings):
        result = ""
        for name in list_of_strings:
            result = result + name + "\n" + SEPARATOR + "\n"
        return result

    ### METHODS ###


    @staticmethod
    def get_tagline(description):
        instruction = "Write a copy title for the following product:"
        action = "This is the title tagline I wrote for the product's page:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + description + '\n' + SEPARATOR + '\n' + action + SEPARATOR,
            temperature=0.5,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.48,
            stop=[SEPARATOR]
        )
        print(response.choices[0].text)

    @staticmethod
    def get_sample_testimonial_bio(description):
        instruction = "A good description of the product:"
        action = "This is product's user experience:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + description + '\n' + SEPARATOR + '\n' + action + SEPARATOR,
            temperature=0.5+0.3,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.1+0.3,
            presence_penalty=0.48+0.3,
            stop=[SEPARATOR]
        )
        print(response.choices[0].text)
        return response.choices[0].text

    @staticmethod
    def get_sample_testimonial_name(sample_testimonial_names):
        description = OpenAIController.list2string(sample_testimonial_names)
        #print(description)
        instruction = "This is a name:"
        #print(instruction)
        action = "This is a name:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + description + '\n' + SEPARATOR + '\n' + action + SEPARATOR,
            temperature=0.5 + 0.4,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.1+0.4,
            presence_penalty=0.48+0.4,
            stop=[SEPARATOR]
        )
        print(response.choices[0].text)
        return response.choices[0].text



    @staticmethod
    def get_sample_testimonial_role(sample_testimonial_names):
        description = OpenAIController.list2string(sample_testimonial_names)
        #print(description)
        instruction = "This is a role:"
        #print(instruction)
        action = "This is a role:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + description + '\n' + SEPARATOR + '\n' + action + SEPARATOR,
            temperature=0.5 + 0.4,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.1+0.4,
            presence_penalty=0.48+0.4,
            stop=[SEPARATOR]
        )
        print(response.choices[0].text)
        return response.choices[0].text

