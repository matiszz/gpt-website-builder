from OpenAIController import OpenAIController


class Populator(object):
    openAI = OpenAIController()

    def __init__(self):
        pass

    @staticmethod
    def populate_contact_html(content, address, email, phone_number):
        return content.format(address=address, email=email, phone_number=phone_number)

    @staticmethod
    def populate_features_html(content):
        return content

    @staticmethod
    def populate_footer_html(content):
        return content

    @staticmethod
    def populate_head_html(content):
        return content

    @staticmethod
    def populate_hero_html(content):
        return content

    @staticmethod
    def populate_navbar_html(content):
        return content

    @staticmethod
    def populate_testimonial_html(content):
        return content

    @staticmethod
    def populate_pricing_html(content):
        return content
