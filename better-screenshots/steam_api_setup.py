import os
from steam_web_api import Steam

def steam_access(key_text: str) -> Steam:
    KEY = os.environ.get(key_text)
    steam = Steam(KEY)
    return steam