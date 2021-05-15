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


@app.route('/', methods=['GET'])
def index():
    return render_template("public/index.html")


@app.route('/result', methods=['GET'])
def result():
    return render_template("generated/index.html")


@app.route('/webhook', methods=['POST'])
def hello():
    htmlGen = HTMLGenerator()
    openAI = OpenAIController()
    pexels = PexelsController()

    form = request.json['form_response']['answers']

    provided_key = list(filter(lambda field: field['field']['id'] == 'ZKyWAMzdVY9h', form))[0]['text']

    if provided_key == MAGIC_KEY:
        info = {
            'description': list(filter(lambda field: field['field']['id'] == 'MXo1rWpND8vZ', form))[0]['text'],
            'product_type': list(filter(lambda field: field['field']['id'] == 'cPauKwCscbCk', form))[0]['text'],
            'address': list(filter(lambda field: field['field']['id'] == 'R4aBPISAiiTO', form))[0]['text'],
            'email': list(filter(lambda field: field['field']['id'] == 'lTFrpytOV3f5', form))[0]['email'],
            'phone_number': list(filter(lambda field: field['field']['id'] == 'OtMQqEttgCq9', form))[0]['phone_number'],
            'web_name': list(filter(lambda field: field['field']['id'] == 'cBdcNK94ys9R', form))[0]['text']
        }

        blocks = openAI.get_landing_blocks(info['product_type'])

        keywords = openAI.get_image_keywords(info['description'])
        info['photo1'] = pexels.search_photo(keywords, "large", 1)
        info['photo2'] = pexels.search_photo(keywords, "large", 2)

        htmlGen.create_result_file(blocks, info)

        return '200'
    else:
        abort(403)


if __name__ == '__main__':
    # app.run()

    openAI = OpenAIController()
    htmlGen = HTMLGenerator()
    pexels = PexelsController()

    # blocks = openAI.get_landing_blocks(sample_info['product_type'])
    # print(blocks)
    keywords = openAI.get_image_keywords(sample_info['description'])
    sample_info['photo1'] = pexels.search_photo(keywords, "large", 1)
    sample_info['photo2'] = pexels.search_photo(keywords, "large", 2)

    htmlGen.create_result_file(['features'], sample_info)
