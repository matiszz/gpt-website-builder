import os.path

from OpenAIController import OpenAIController
import webbrowser

sample_description = "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, " \
                     "can create new conversations for different topics. It also allows you to create different " \
                     "domain levels and organize users in addresses. "

sample_product_type = "a SaaS product"

if __name__ == '__main__':
    # execute only if run as the entry point into the program

    openAI = OpenAIController()
    # tagline = openAI.get_tagline(sample_description)
    # description = openAI.get_description(sample_description)
    # openAI.get_sample_testimonial_bio(sample_description)
    # pricing = openAI.get_pricing_features(sample_description)
    # blocks = openAI.get_landing_blocks(sample_product_type)

    blocks = ['navbar', 'features', 'hero', 'pricing', 'contact']
    print("blocks: {}".format(blocks))

    result_file = open('generated/index.html', 'w')
    blocks.insert(0, 'head')
    for block_name in blocks:
        block_file = open("blocks/{}.html".format(block_name), 'r')
        result_file.write(block_file.read())

    result_file.write("</body>\n</html>")
    result_file.close()
    webbrowser.open('file:///home/mati/Code/Projects/gpt-website-builder/generated/index.html', new=2)
