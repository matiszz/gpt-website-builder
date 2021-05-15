from OpenAIController import OpenAIController
from HTMLGenerator import HTMLGenerator

# Sample data, we should get this with TypeForm
info = {
    'description': "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, can create new conversations for different topics. It also allows you to create different domain levels and organize users in addresses. ",
    'product_type': "a SaaS product",
    'address': "C/ Jordi Girona, 21, Barcelona",
    'email': 'info@fib.edu',
    'phone_number': '+34672900943',
    'web_name': "Velox"
}

if __name__ == '__main__':
    htmlGen = HTMLGenerator()
    openAI = OpenAIController()

    # blocks = openAI.get_landing_blocks(sample_product_type)

    blocks = ['navbar', 'features', 'hero', 'pricing', 'contact']

    htmlGen.create_result_file(blocks, info)
