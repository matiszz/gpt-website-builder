from dotenv import dotenv_values
import openai
import re
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
openai.api_key = os.environ.get("OPENAI_API_KEY")

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
            temperature=0.4, max_tokens=30, top_p=1, frequency_penalty=0.1, presence_penalty=0.3, stop=[SEPARATOR]
        )

        print(' -- Result tagline: {}'.format(response.choices[0].text))
        return response.choices[0].text

    @staticmethod
    def get_copy(description):
        print('Generating copy...')
        instruction = "Someone told me about their company:"
        action = "I rephrased it to make it more catchy for a marketing copy:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + '\n' + SEPARATOR + '\n' + description + '\n' + SEPARATOR + '\n' + action + '\n' + SEPARATOR,
            temperature=0.8, max_tokens=50, top_p=1, frequency_penalty=0.2, presence_penalty=0.4, stop=[SEPARATOR]
        )

        print(' -- Result copy: {}'.format(response.choices[0].text))
        return response.choices[0].text

    @staticmethod
    def get_sample_testimonial_bio(description):
        instruction = "A review of the product:"
        action = "This is a list of three user's product review experience: \n1."
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + '\n' + description + '\n' + SEPARATOR + '\n' + action,
            temperature=0.6, max_tokens=90, top_p=1, frequency_penalty=0.2,presence_penalty=0.58, stop=[SEPARATOR]
        )
        text = str(response.choices[0].text).split('"""')[0]
        list_testimonial = list(
            map(lambda feature: ' '.join(feature.split()), re.split('\d\.', text)))

        print(' -- Result testimonials bios: {}'.format(list_testimonial))
        return list_testimonial

    @staticmethod
    def get_sample_testimonial_names():
        instruction = "This are three names:\n1. Martha Taylor\n2. Lucy Williams\n3. John Smith\n"
        action = "This is a list of three new names: \n1."
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + "\n" + action,
            temperature=0.9, max_tokens=15, top_p=1, frequency_penalty=0.7, presence_penalty=0.88,
            stop=[SEPARATOR]
        )
        text = str(response.choices[0].text).split('"""')[0]
        names_list = list(map(lambda feature: ' '.join(feature.split()), re.split('\d\.', text)))

        print(' -- Result testimonials names: {}'.format(names_list))
        return names_list

    @staticmethod
    def get_sample_testimonial_roles():
        instruction = "This are three roles:\n1. Product Designer\n2. UI Developer\n3. CIO\n"
        action = "This is a list of only three roles: \n1."
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + action,
            temperature=0.9, max_tokens=20, top_p=1, frequency_penalty=0.5, presence_penalty=0.88, stop=[SEPARATOR]
        )
        text = str(response.choices[0].text).split('"""')[0]
        roles_list = list(map(lambda feature: ' '.join(feature.split()), re.split('\d\.', text)))

        print(' -- Result testimonials roles: {}'.format(roles_list))
        return roles_list

    @staticmethod
    def get_pricing_features(description):
        print('Generating pricing...')

        instruction = "This is a company:"
        action = "I wrote 3 features for these plans: START, PRO and BUSINESS:"
        prompt = instruction + '\n' + SEPARATOR + '\n' + description + '\n' + SEPARATOR + '\n' + action + '\n\n'
        response_start = openai.Completion.create(
            engine="davinci",
            prompt=prompt + 'START\n1.',
            temperature=0.8, max_tokens=30, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )
        response_pro = openai.Completion.create(
            engine="davinci",
            prompt=prompt + 'PRO\n1.',
            temperature=0.8, max_tokens=30, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )
        response_business = openai.Completion.create(
            engine="davinci",
            prompt=prompt + 'BUSINESS\n1.',
            temperature=0.8, max_tokens=30, top_p=1, frequency_penalty=0.2, presence_penalty=0.3, stop=[SEPARATOR]
        )

        start_features = list(
            map(lambda feature: ' '.join(feature.split()),
                re.split('\d\.', response_start.choices[0].text)))
        pro_features = list(
            map(lambda feature: ' '.join(feature.split()),
                re.split('\d\.', response_pro.choices[0].text)))
        business_features = list(
            map(lambda feature: ' '.join(feature.split()),
                re.split('\d\.', response_business.choices[0].text)))

        print(' -- Result START features: {}'.format(response_start))
        print(' -- Result PRO features: {}'.format(response_pro))
        print(' -- Result BUSINESS features: {}'.format(response_business))

        return {"start": start_features, "pro": pro_features, "business": business_features}

    @staticmethod
    def get_landing_blocks(product_type):
        print('Generating blocks...')

        instruction = "This is a generator of websites with blocks. The available blocks are contact, features, footer, hero, navbar, pricing, and testimonial.\n"
        example1 = "Description: Landing page for a SaaS product:\n- navbar\n- hero\n- features\n- testimonial\n- pricing\n"
        example2 = "Description: Landing page for a lawyer's firm:\n- hero\n- testimonial\n- contact\n- footer\n"
        completion = "Description: Landing page for {}.\n-".format(product_type)
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + example1 + SEPARATOR + '\n' + example2 + SEPARATOR + '\n' + completion,
            temperature=0.7, max_tokens=30, top_p=1, frequency_penalty=0, presence_penalty=0, stop=[SEPARATOR]
        )
        print(' -- Result landing blocks: {}'.format(response))
        return list(map(lambda feature: ' '.join(feature.split()).lower(), re.split('- ', response.choices[0].text)))

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
        print(' -- Result Feature: {}'.format(response_feature.choices[0].text))

        instruction = "Text: {}\n\n".format(description)
        action = "Keywords:"
        response_keyword_feature = openai.Completion.create(
            engine="davinci",
            prompt=instruction + action,
            temperature=0.7, max_tokens=3, top_p=1, frequency_penalty=0.8, presence_penalty=0, stop=["\n"]
        )
        print(' -- Result Feature Keyword: {}'.format(response_keyword_feature.choices[0].text))

        # feature[0] is the name, keyword of the description
        feature[0] = response_keyword_feature.choices[0].text.strip().capitalize().split(',')[0]
        return feature
      
    @staticmethod
    def get_image_keywords(description):
        print('Generating keywords...')

        instruction = "Text: {}\n\n".format(description)
        action = "Keywords:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + action,
            temperature=0.3, max_tokens=20, top_p=1, frequency_penalty=0.8, presence_penalty=0, stop=["\n"]
        )

        print(' -- Result image keywords: {}'.format(response.choices[0].text))
        return ' '.join(response.choices[0].text.split())

    @staticmethod
    def get_testimonial_features(description):
        names_list = OpenAIController.get_sample_testimonial_names()
        roles_list = OpenAIController.get_sample_testimonial_roles()
        testimonial_bio_list = OpenAIController.get_sample_testimonial_bio(description)

        for i in range(len(names_list)):
            if names_list[i] == " " or names_list[i] == "": names_list[i] = "James Milner"
        for i in range(len(roles_list)):
            if roles_list[i] == " " or roles_list[i] == "": roles_list[i] = " Developer"
        for i in range(len(testimonial_bio_list)):
            if testimonial_bio_list[i] == " " or testimonial_bio_list[i] == "": testimonial_bio_list[i] = "I loved using the product"

        while len(names_list) < 3: names_list.append("Simon Tyler")
        while len(roles_list) < 3: roles_list.append("Customer")
        while len(testimonial_bio_list) < 3: testimonial_bio_list.append("This product is amazing")



        return {"names": names_list, "roles": roles_list, "testimonials": testimonial_bio_list}

    def get_navbar_links(self, product_type):
        print('Generating navbar links...')

        instruction = "This is a generator of links for navigation bars on websites.\n"
        example1 = "Description: A website for a SaaS product:\n- Features\n- Pricing\n- CTA: Register\n"
        example2 = "Description: A website for a lawyer's firm:\n- Our services\n- Experience\n- CTA: Contact\n"
        example3 = "Description: A website for a trainer:\n- Training\n- Clients\n- CTA: Book now!\n"
        completion = "Description: A website for a {}:\n-".format(product_type)

        response = openai.Completion.create(
            engine="davinci",
            prompt=instruction + SEPARATOR + '\n' + example1 + SEPARATOR + '\n' + example2 + SEPARATOR + '\n' + example3 + SEPARATOR + '\n' + completion,
            temperature=0.7, max_tokens=10, top_p=1, frequency_penalty=0, presence_penalty=0, stop=[SEPARATOR]
        )

        result = list(map(lambda feature: ' '.join(feature.split()), re.split('- ', response.choices[0].text)))

        if len(result) < 3:
            print('Not enough links')
            return self.get_navbar_links(product_type)

        print(' -- Result navbar links: {}'.format(result))

        result[2] = result[2].replace('CTA:', '')
        if result[2] == '' or result[2] == ' ' or result[2] == 'CTA': result[2] = 'Sign Up'
        return result
