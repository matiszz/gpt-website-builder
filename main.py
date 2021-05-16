import os
from OpenAIController import OpenAIController
from HTMLGenerator import HTMLGenerator
from PexelsController import PexelsController
from flask import Flask, render_template, request, abort
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
MAGIC_KEY = os.environ.get("MAGIC_KEY")

app = Flask(__name__)

sample_info = {
    'description': "Velox is a real-time platform that helps remote teams keeping organized chats. In Velox, can create new conversations for different topics. It also allows you to create different domain levels and organize users in addresses. ",
    'product_type': "a SaaS product",
    'address': "C/ Jordi Girona, 21, Barcelona",
    'email': 'info@fib.edu',
    'phone_number': '+34672900943',
    'web_name': "Velox"
}

htmlGen = HTMLGenerator()


@app.route('/', methods=['GET'])
def index():
    return render_template("public/index.html")


@app.route('/result', methods=['GET'])
def result():
    return htmlGen.get_html()


@app.route('/webhook', methods=['POST'])
def hello():
    openAI = OpenAIController()
    pexels = PexelsController()

    form = request.json['form_response']['answers']

    provided_key = list(filter(lambda field: field['field']['id'] == 'ZKyWAMzdVY9h', form))[0]['text']

    if provided_key == MAGIC_KEY:
        htmlGen.create_loading_file()

        info = {
            'description': list(filter(lambda field: field['field']['id'] == 'MXo1rWpND8vZ', form))[0]['text'],
            'product_type': list(filter(lambda field: field['field']['id'] == 'cPauKwCscbCk', form))[0]['text'],
            'address': list(filter(lambda field: field['field']['id'] == 'R4aBPISAiiTO', form))[0]['text'],
            'email': list(filter(lambda field: field['field']['id'] == 'lTFrpytOV3f5', form))[0]['email'],
            'phone_number': list(filter(lambda field: field['field']['id'] == 'OtMQqEttgCq9', form))[0]['phone_number'],
            'web_name': list(filter(lambda field: field['field']['id'] == 'cBdcNK94ys9R', form))[0]['text']
        }

        blocks = openAI.get_landing_blocks(info['product_type'])
        blocks = sort_blocks(blocks)
        keywords = openAI.get_image_keywords(info['description'])
        info['photo1'] = pexels.search_photo(keywords, "large", 1)
        info['photo2'] = pexels.search_photo(keywords, "large", 2)

        htmlGen.create_result_file(blocks, info)

        return '200'
    else:
        abort(403)


def criteria(object):
    return object['priority']


def sort_blocks(blocks):
    priorities = {"navbar": 1, "hero": 2, "features": 3, "pricing": 4, "testimonial": 5, "contact": 6, "footer": 7}

    blocks_obj = []
    for block in blocks:
        if block in priorities: blocks_obj.append({"block": block, "priority": priorities[block]})
    blocks_obj.sort(key=criteria)
    return_blocks = []
    for single_Block in blocks_obj: return_blocks.append(single_Block["block"])
    return return_blocks


if __name__ == '__main__':
    app.run()

    # openAI = OpenAIController()
    # htmlGen = HTMLGenerator()
    # pexels = PexelsController()
    # htmlGen.create_loading_file()

    # blocks = openAI.get_landing_blocks(sample_info['product_type'])

    # blocs = ['navbar', 'features', 'pricing', 'footer', 'hero']
    # blocs = sortBlocks(blocs)
    # print(blocs)
    # keywords = openAI.get_image_keywords(sample_info['description'])
    # sample_info['photo1'] = pexels.search_photo(keywords, "large", 1)
    # sample_info['photo2'] = pexels.search_photo(keywords, "large", 2)

    # htmlGen.create_result_file(['features'], sample_info)
