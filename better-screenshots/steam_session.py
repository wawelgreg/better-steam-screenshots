import config as conf
import os
from pathlib import Path
from steam_web_api import Steam

KEY = os.environ.get(conf.steam_key)
steam = Steam(KEY)

def main():
    print("")
    p = Path(conf.screenshot_path)
    print(p)
main()