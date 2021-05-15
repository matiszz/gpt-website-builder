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
        print('Generating tagline...')
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
    def get_copy(description):
        print('Generating copy...')
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
        print('Generating pricing...')
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
        print('Generating blocks...')

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

    @staticmethod
    def get_feature(info):
        print('Generating features...')
        feature = [None, None]
        description = info['description']
        example_1_description = "Fill a simple form in less than two minutes. Tell us about your company as if you were explaining it to your friend."
        example_2_description = "Just click send. Give us a few seconds. Our OpenAI and GPT-3 powered engine will create the best <b>unique</b> website for your product. It's gonna be amazing."
        instruction = "This is a " + info['product_type'] + " feature example:\n"
        action = "Write a feature description for a " + info['product_type'] + ":"
        prompt = instruction + '\n' + description + '\n' + example_1_description + '\n' + SEPARATOR + '\n' + example_2_description + '\n' + SEPARATOR + '\n' + action
        response_feature = openai.Completion.create(
            engine="davinci",
            prompt=prompt + '\n',
            temperature=0.85, max_tokens=69, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )
        # feature[1] is the description
        feature[1] = response_feature.choices[0].text

        instruction = "Text: {}\n\n".format(description)
        action = "Keywords:"
        response_keyword_feature = openai.Completion.create(
            engine="davinci",
            prompt=instruction + action,
            temperature=0.7, max_tokens=3, top_p=1, frequency_penalty=0.8, presence_penalty=0, stop=["\n"]
        )
        # feature[0] is the name, keyword of the description
        feature[0] = response_keyword_feature.choices[0].text.strip().capitalize().split(',')[0]
        return feature

