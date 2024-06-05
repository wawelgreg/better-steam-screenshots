import file_sorter as fs
import os
from steam_web_api import Steam

def steam_key():
    KEY = os.environ.get(fs.import_data_dict_json()["Key"])
    steam = Steam(KEY)
    return steam