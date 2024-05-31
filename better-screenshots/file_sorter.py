import os
import steam_api_setup as sas
import config as conf
import json
import logging as log
from pathlib import Path
import shutil

FORMAT = '%(asctime)s %(message)s'
log.basicConfig(filename='bss.log', format=FORMAT, level=log.INFO)

log.info("Attaining steam api with config key...")
steam = sas.steam_key()
log.info("Success!")
log.info("Attaining root and destination screenshot folder...")
ROOT = Path(conf.screenshot_path)
DEST = Path(conf.destination_path)
log.info("Success!")


def path_exist(P):
    if (P.is_file()):
        return True
    return False


def import_local_dict():
    if (not path_exist(Path(r"better-screenshots/game_list_data.json"))):
        log.info("Game list data DNE. Returning empty dict.")
        return dict()
    
    log.info("game_list_data.json exists -> converting to dict.")
    with open(r"better-screenshots/game_list_data.json") as json_file:
        lgd = json.load(json_file)
    log.info("Returning dict.")
    return lgd


def search_game_name(game_id):
    return steam.apps.get_app_details(game_id)[str(game_id)]["data"]["name"]


def image_iter(local_game_dict):
    for file in ROOT.glob("*.png"):
        sort_store_image(file, local_game_dict)


def sort_store_image(file, local_game_dict):
    if (not path_exist(DEST)):
        DEST.mkdir(parents=True, exist_ok=True)
    pass


if __name__ == "__main__":
    log.info("Attaining local game list data.")
    local_game_dict = import_local_dict()
    image_iter(local_game_dict)