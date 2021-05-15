from dotenv import dotenv_values
import openai
import re

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
            stop=[SEPARATOR]
        )
        return response.choices[0].text

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

    @staticmethod
    def get_pricing_features(description):
        instruction = "This is a company:"
        action = "I wrote 3 features for these plans: START, PRO and BUSINESS:"
        prompt = instruction + '\n'+SEPARATOR+'\n' + description + '\n'+SEPARATOR+'\n' + action + '\n\n'
        response_start = openai.Completion.create(
            engine="davinci",
            prompt=prompt + 'START\n1.',
            temperature=0.8, max_tokens=50, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )
        response_pro = openai.Completion.create(
            engine="davinci",
            prompt=prompt + 'PRO\n1.',
            temperature=0.8, max_tokens=50, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )
        response_business = openai.Completion.create(
            engine="davinci",
            prompt=prompt + 'BUSINESS\n1.',
            temperature=0.8, max_tokens=50, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )

        start_features = list(map(lambda feature: ' '.join(feature.split()), re.split('\d\.', response_start.choices[0].text)))
        pro_features = list(map(lambda feature: ' '.join(feature.split()), re.split('\d\.', response_pro.choices[0].text)))
        business_features = list(map(lambda feature: ' '.join(feature.split()), re.split('\d\.', response_business.choices[0].text)))

        return {"start": start_features, "pro": pro_features, "business": business_features}

    @staticmethod
    def get_landing_blocks(product_type):
        instruction = "This is a generator of websites with blocks. The available blocks are contact, features, footer, hero, navbar, pricing, and testimonial.\n"
        example1 = "Description: Landing page for a SaaS product:\n- navbar\n- hero\n- features\n- testimonial\n- pricing\n"
        example2 = "Description: Landing page for a lawyer's firm:\n- hero\n- testimonial\n- contact\n- footer\n"
        completion = "Description: Landing page for{}.\n-".format(product_type)
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + example1 + SEPARATOR + '\n' + example2 + SEPARATOR + '\n' + completion,
            temperature=0.7,
            max_tokens=30,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[SEPARATOR]
        )
        return list(map(lambda feature: ' '.join(feature.split()), re.split('- ', response.choices[0].text)))
