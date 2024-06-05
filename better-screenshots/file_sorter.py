import steam_api_setup as sas
import config as conf
import json
import logging as log
from pathlib import Path
import shutil

# Logger configuration
FORMAT = '%(asctime)s|%(levelname)s|%(message)s'
log.basicConfig(filename='bss.log', format=FORMAT, level=log.INFO)

# Steam API key and paths setup from config
log.info("Attaining steam api with config key...")
steam = sas.steam_key()
log.info("Success!")

log.info("Attaining root and destination screenshot folder...")
SOURCE = Path(conf.screenshot_path)
DEST = Path(conf.destination_path)
log.info("Success!")

DEFAULT_DATA = {"Key": "", "Src": "", "Dest": ""}
DEFAULT_GAME_JSON_PATH = fr"better-screenshots/game_list_data.json"
DEFUALT_DATA_JSON_PATH = fr"better-screenshots/data.json"


def import_data_dict_json():
    if (not Path(DEFUALT_DATA_JSON_PATH).exists()):
        log.info("%s DNE. Returning blank data.", DEFUALT_DATA_JSON_PATH)
        return DEFAULT_DATA
    
    log.info("data.json exists -> converting to dict.")
    with open(DEFUALT_DATA_JSON_PATH) as json_file:
        data = json.load(json_file)
    log.info("Returning data dict.")
    return data


def import_game_dict_json():
    if (not Path(DEFAULT_GAME_JSON_PATH).exists()):
        log.info("%s DNE. Returning empty dict.", DEFAULT_GAME_JSON_PATH)
        return dict()
    
    log.info("game_list_data.json exists -> converting to dict.")
    with open(DEFAULT_GAME_JSON_PATH) as json_file:
        lgd = json.load(json_file)
    log.info("Returning game list dict.")
    return lgd


def update_dict(d: dict, d_key: int, d_val: str):
    d[d_key] = d_val


def update_dict_json(d: dict, file_path: str):
    with open(file_path, "w") as outfile:
        json.dump(d, outfile)


def search_game_name(game_id: int):
    return steam.apps.get_app_details(game_id)[str(game_id)]["data"]["name"]


def handle_title(game_name: str):
    temp = game_name.replace(" ", "-")
    res = "".join(x for x in temp if x.isalnum())
    return res


def image_iter(local_game_dict: dict):
    for file in SOURCE.glob("*.png"):
        sort_store_image(file, local_game_dict)


def sort_store_image(file, local_game_dict: dict):
    if (not DEST.exists()):
        DEST.mkdir(parents=True, exist_ok=True)
    
    details = file.name.removesuffix(".png")
    parsed = details.split('_')

    log.info("Checking game name existence in dict: {}".format(local_game_dict))
    if parsed[0] in local_game_dict:
        game_name = local_game_dict[parsed[0]]
    else:
        game_name = search_game_name(parsed[0])
        update_dict(local_game_dict, parsed[0], game_name)
        log.info("New game name: local dict: {}".format(local_game_dict))

    scrn_game_name = handle_title(game_name)
    scrn_year = parsed[1][0:4]
    scrn_month = parsed[1][4:6]
    scrn_day = parsed[1][6:8]
    scrn_hour = parsed[1][8:10]
    scrn_minute = parsed[1][10:12]
    scrn_seconds = parsed[1][12:]

    log.info("%s %s %s %s %s:%s:%s", 
             scrn_game_name, scrn_year, scrn_month,
             scrn_day, scrn_hour, scrn_minute, scrn_seconds)
    
    final_dest = conf.destination_path + fr"\{scrn_game_name}\{scrn_year}\{scrn_month+"-"+scrn_day}"
    log.info(final_dest)

    log.info("Checking directory existence...")
    if (not Path(final_dest).exists()):
        log.info("Directory DNE: Making directory")
        Path(final_dest).mkdir(parents=True, exist_ok=True)

    res_file = Path(final_dest + fr"\{file.name}")
    
    log.info("Checking file existence...")
    if (res_file.exists()):
        log.info("Sorted file already exists!")
        return

    log.info("Copying file...")
    shutil.copy(file, res_file)
    log.info("Success!")


def main():
    log.info(">>> >>> PROGRAM START <<< <<<")

    log.info("Attaining local game list data.")
    local_game_dict = import_game_dict_json()
    image_iter(local_game_dict)
    log.info("All images copied and sorted!")

    log.info("Updating game_list_data.json...")
    update_dict_json(local_game_dict, DEFAULT_GAME_JSON_PATH)
    log.info("Success!")

    log.info(">>> >>> All ACTIONS COMPLETED <<< <<<")



if __name__ == "__main__":
    main()