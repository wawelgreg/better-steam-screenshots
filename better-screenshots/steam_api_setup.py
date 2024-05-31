import config as conf
import os
from steam_web_api import Steam

def steam_key():
    KEY = os.environ.get(conf.steam_key)
    steam = Steam(KEY)
    return steam