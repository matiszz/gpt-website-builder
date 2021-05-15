from OpenAIController import OpenAIController
from HTMLGenerator import HTMLGenerator

sample_description = "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, " \
                     "can create new conversations for different topics. It also allows you to create different " \
                     "domain levels and organize users in addresses. "
sample_product_type = "a SaaS product"

if __name__ == '__main__':
    openAI = OpenAIController()
    htmlGen = HTMLGenerator()

    # tagline = openAI.get_tagline(sample_description)
    # description = openAI.get_description(sample_description)
    # openAI.get_sample_testimonial_bio(sample_description)
    # pricing = openAI.get_pricing_features(sample_description)
    # blocks = openAI.get_landing_blocks(sample_product_type)

    blocks = ['navbar', 'features', 'hero', 'pricing', 'contact']
    print("blocks: {}".format(blocks))
    htmlGen.create_result_file(blocks)
