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
    def populate_footer_html(content, web_name):
        return content.format(web_name=web_name)

    @staticmethod
    def populate_head_html(content, web_name):
        return content.format(web_name=web_name)

    def populate_hero_html(self, content, description):
        tagline = self.openAI.get_tagline(description)
        copy = self.openAI.get_copy(description)
        # TODO: Change
        image_src = 'https://images.pexels.com/photos/7473282/pexels-photo-7473282.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'

        return content.format(tagline=tagline, copy=copy, image_src=image_src)

    @staticmethod
    def populate_navbar_html(content):
        return content

    @staticmethod
    def populate_testimonial_html(content):
        return content

    @staticmethod
    def populate_pricing_html(content):
        return content
