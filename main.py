from OpenAIController import OpenAIController

sample_description = "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, " \
                     "can create new conversations for different topics. It also allows you to create different " \
                     "domain levels and organize users in addresses. "


if __name__ == '__main__':
    # execute only if run as the entry point into the program

    openAI = OpenAIController()
    # tagline = openAI.get_tagline(sample_description)
    # description = openAI.get_description(sample_description)
    # openAI.get_sample_testimonial_bio(sample_description)
    pricing = openAI.get_pricing_features(sample_description)

    print("pricing: {}".format(pricing))

