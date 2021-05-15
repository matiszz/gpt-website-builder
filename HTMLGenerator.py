import os.path
import webbrowser
from Populator import Populator

FILE_NAME = 'generated/index.html'


def get_populated_html_content(block_name, web_info):
    try:
        block_file = open("blocks/{}.html".format(block_name), 'r')
        populator = Populator()

        if block_name == 'contact':
            return populator.populate_contact_html(block_file.read(), web_info['address'], web_info['email'],
                                                   web_info['phone_number'])
        elif block_name == 'features':
            return populator.populate_features_html(block_file.read())
        elif block_name == 'footer':
            return populator.populate_footer_html(block_file.read(), web_info['web_name'])
        elif block_name == 'head':
            return populator.populate_head_html(block_file.read(), web_info['web_name'])
        elif block_name == 'hero':
            return populator.populate_hero_html(block_file.read(), web_info['description'])
        elif block_name == 'navbar':
            return populator.populate_navbar_html(block_file.read(), web_info['web_name'], web_info['description'])
        elif block_name == 'pricing':
            return populator.populate_pricing_html(block_file.read(), web_info['description'], web_info['web_name'])
        elif block_name == 'testimonial':
            return populator.populate_testimonial_html(block_file.read())
    except IOError:
        print("{} does not exist as HTML".format(block_name))
        return ""


class HTMLGenerator(object):

    def __init__(self):
        print("HTML Generator created")

    @staticmethod
    def create_result_file(html_blocks, web_info):
        result_file = open(FILE_NAME, 'w')

        # Insert the 'head' block at the beginning
        html_blocks.insert(0, 'head')

        for block_name in html_blocks:
            result_file.write(get_populated_html_content(block_name, web_info))

        # Close file and open in browser
        result_file.write("</body>\n</html>")
        result_file.close()
        webbrowser.open("file://{}".format(os.path.abspath(FILE_NAME)), new=2)
