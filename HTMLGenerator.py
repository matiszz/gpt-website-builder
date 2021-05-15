import os.path
import webbrowser

FILE_NAME = 'generated/index.html'


def get_populated_html_content(block_name):
    block_file = open("blocks/{}.html".format(block_name), 'r')

    return block_file.read()


class HTMLGenerator(object):

    def __init__(self):
        print("HTML Generator created")

    @staticmethod
    def create_result_file(html_blocks):
        result_file = open(FILE_NAME, 'w')

        # Insert the 'head' block at the beginning
        html_blocks.insert(0, 'head')

        for block_name in html_blocks:
            result_file.write(get_populated_html_content(block_name))

        # Close file and open in browser
        result_file.write("</body>\n</html>")
        result_file.close()
        webbrowser.open("file://{}".format(os.path.abspath(FILE_NAME)), new=2)

