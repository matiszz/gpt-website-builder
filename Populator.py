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

    def populate_testimonial_html(self, content, web_info):
        features = self.openAI.get_testimonial_features(web_info)
        return content.format(
            testimonial_1=features['testimonials'][0],
            testimonial_2=features['testimonials'][1],
            testimonial_3=features['testimonials'][2],
            name_1=features['names'][0],
            name_2=features['names'][1],
            name_3=features['names'][2],
            role_1=features['roles'][0],
            role_2=features['roles'][1],
            role_3=features['roles'][2],
        )

    def populate_pricing_html(self, content, description, web_name):
        features = self.openAI.get_pricing_features(description)
        return content.format(
            web_name=web_name,
            feature_1_p1=features['start'][0],
            feature_2_p1=features['start'][1],
            feature_3_p1=features['start'][2],
            feature_1_p2=features['pro'][0],
            feature_2_p2=features['pro'][1],
            feature_3_p2=features['pro'][2],
            feature_1_p3=features['business'][0],
            feature_2_p3=features['business'][1],
            feature_3_p3=features['business'][2],
        )
