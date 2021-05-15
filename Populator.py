from OpenAIController import OpenAIController


class Populator(object):
    openAI = OpenAIController()

    def __init__(self):
        pass

    @staticmethod
    def populate_contact_html(content, address, email, phone_number):
        return content.format(address=address, email=email, phone_number=phone_number)

    def populate_features_html(self, content, description, web_name):
        features_1 = self.openAI.get_feature(description)
        features_2 = self.openAI.get_feature(description)
        features_3 = self.openAI.get_feature(description)
        return content.format(
            web_name=web_name,
            feature_1_name=features_1[0],
            feature_1_description=features_1[1],
            feature_2_name=features_2[0],
            feature_2_description=features_2[1],
            feature_3_name=features_3[0],
            feature_3_description=features_3[1],
            # image_src_features=features['image_features'][0],
        )

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
