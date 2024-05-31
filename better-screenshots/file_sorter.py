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


def import_local_dict():
    if (not Path(r"better-screenshots/game_list_data.json").is_file()):
        log.info("Game list data DNE. Returning empty dict.")
        return dict()
    
    log.info("game_list_data.json exists -> converting to dict.")
    with open(r"better-screenshots/game_list_data.json") as json_file:
        lgd = json.load(json_file)
    log.info("Returning dict.")
    return lgd


def search_game_name(game_id):
    return steam.apps.get_app_details(game_id)[str(game_id)]["data"]["name"]


if __name__ == "__main__":
    log.info("Attaining local game list data.")
    local_game_dict = import_local_dict()