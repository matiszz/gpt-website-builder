import pprint

from dotenv import dotenv_values
from pexels_api import API

PEXELS_API_KEY = dotenv_values(".env")['PEXELS_API_KEY']
# Create API object
api = API(PEXELS_API_KEY)


## CALL FROM main.py
# pexels = PexelsController()
# second attribute for the size, first one for keyword
# photo = pexels.search_photo("barcelona", "medium")

class PexelsController(object):
    def __init__(self):
        print("Pexels Controller created")

    @staticmethod
    def search_photo(photo, size):
        api.search(photo, page=1, results_per_page=1)
        photos_result = api.get_entries()
        return getattr(photos_result[0], size)
