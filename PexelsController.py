from pexels_api import API
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")
api = API(PEXELS_API_KEY)


## CALL FROM main.py
# pexels = PexelsController()
# second attribute for the size, first one for keyword
# photo = pexels.search_photo("barcelona", "medium")

class PexelsController(object):
    def __init__(self):
        print("Pexels Controller screated")

    @staticmethod
    def search_photo(photo, size, page=1):
        if photo == '' or photo is None: photo = "startup"
        api.search(photo, page=page, results_per_page=1)
        photos_result = api.get_entries()
        return getattr(photos_result[0], size)
