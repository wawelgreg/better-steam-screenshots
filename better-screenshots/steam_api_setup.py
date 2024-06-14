import os
from steam_web_api import Steam

def steam_access(key_text: str) -> Steam:
    steam = Steam(key_text)
    return steam