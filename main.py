from OpenAIController import OpenAIController
from HTMLGenerator import HTMLGenerator

# Sample data, we should get this with TypeForm
from PexelsController import PexelsController

info = {
    'description': "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, can create new conversations for different topics. It also allows you to create different domain levels and organize users in addresses. ",
    'product_type': "a SaaS product",
    'address': "C/ Jordi Girona, 21, Barcelona",
    'email': 'info@fib.edu',
    'phone_number': '+34672900943',
    'web_name': "Velox"
}
sample_description = "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, " \
                     "you can create new conversations for different topics. "



if __name__ == '__main__':
    htmlGen = HTMLGenerator()
    openAI = OpenAIController()
    pexels = PexelsController()

    blocks = openAI.get_landing_blocks(info['product_type'])
    print(blocks)

    keywords = openAI.get_image_keywords(info['description'])
    info['photo1'] = pexels.search_photo(keywords, "large", 1)
    info['photo2'] = pexels.search_photo(keywords, "large", 2)

    htmlGen.create_result_file(blocks, info)

    #openAI.get_sample_testimonial_bio(sample_description)
    print("---")
    #openAI.get_sample_testimonial_names()
    print("---")
    #openAI.get_sample_testimonial_roles()

