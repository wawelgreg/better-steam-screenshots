import steam_api_setup as sas
import json
from pathlib import Path
import shutil
import log_manager as l

DEFAULT_DATA = {"Key": "", "Src": "", "Dest": ""}
DEFAULT_GAME_JSON_PATH = fr"game_list_data.json"
DEFAULT_DATA_JSON_PATH = fr"data.json"


# GLOBAL Steam api key, steam object, and source and dest paths
steam_key = "BLANK_KEY"
source_path = "BLANK_SRC"
dest_path = "BLANK_DEST"
steam = ""


def update_glob_vars(entry_values: tuple):
    global steam_key
    global source_path
    global dest_path

    steam_key, source_path, dest_path = entry_values
    print("Hello: {} {} {}".format(steam_key, source_path, dest_path))


def import_data_dict_json():
    if (not Path(DEFAULT_DATA_JSON_PATH).exists()):
        l.log.info("%s DNE. Returning blank data", DEFAULT_DATA_JSON_PATH)
        return DEFAULT_DATA
    
    l.log.info("data.json exists -> converting to dict")
    with open(DEFAULT_DATA_JSON_PATH) as json_file:
        data = json.load(json_file)
    # l.log.info("updating global variables")
    # update_glob_vars(data)
    l.log.info("Returning data dict")
    return data


def update_dict_json(d: dict, file_path: str):
    with open(file_path, "w") as outfile:
        json.dump(d, outfile)


def import_game_dict_json():
    if (not Path(DEFAULT_GAME_JSON_PATH).exists()):
        l.log.info("%s DNE. Returning empty dict.", DEFAULT_GAME_JSON_PATH)
        return dict()
    
    l.log.info("game_list_data.json exists -> converting to dict.")
    with open(DEFAULT_GAME_JSON_PATH) as json_file:
        lgd = json.load(json_file)
    l.log.info("Returning game list dict.")
    return lgd


def update_dict(d: dict, d_key: int, d_val: str):
    d[d_key] = d_val


def search_game_name(game_id: int):
    return steam.apps.get_app_details(game_id)[str(game_id)]["data"]["name"]


def handle_title(game_name: str):
    temp = game_name.replace(" ", "-")
    res = "".join(x for x in temp if x.isalnum())
    return res


def check_format(png_name: str) -> bool:
    if len(png_name) < 22 or len(png_name) > 23:
        return False
    
    if len(png_name) == 22:
        if (png_name[5] == '_') and (png_name[20] == '_'):
            return True
        
    if len(png_name) == 23:
        if(png_name[6] == '_') and (png_name[21] == '_'):
            return True
    
    return False


def image_iter(local_game_dict: dict):
    for file in Path(source_path).glob("*.png"):
        l.log.info("Checking format of %s", file.stem)
        if check_format(file.stem):
            sort_store_image(file, local_game_dict)


def sort_store_image(file, local_game_dict: dict):
    if (not Path(dest_path).exists()):
        Path(dest_path).mkdir(parents=True, exist_ok=True)
    
    details = file.name.removesuffix(".png")
    parsed = details.split('_')

    l.log.info("Checking id <{}> existence in dict: {}".format(parsed[0], local_game_dict))
    if parsed[0] in local_game_dict:
        game_name = local_game_dict[parsed[0]]
    else:
        game_name = search_game_name(parsed[0])
        update_dict(local_game_dict, parsed[0], game_name)
        l.log.info("New game name: local dict: {}".format(local_game_dict))

    scrn_game_name = handle_title(game_name)
    scrn_year = parsed[1][0:4]
    scrn_month = parsed[1][4:6]
    scrn_day = parsed[1][6:8]
    scrn_hour = parsed[1][8:10]
    scrn_minute = parsed[1][10:12]
    scrn_seconds = parsed[1][12:]

    l.log.info("%s %s %s %s %s:%s:%s", 
             scrn_game_name, scrn_year, scrn_month,
             scrn_day, scrn_hour, scrn_minute, scrn_seconds)
    
    final_dest = dest_path + fr"/Sorted-Screenshots/{scrn_game_name}/{scrn_year}/{scrn_month+"-"+scrn_day}"
    l.log.info(final_dest)

    l.log.info("Checking directory existence...")
    if (not Path(final_dest).exists()):
        l.log.info("Directory DNE: Making directory")
        Path(final_dest).mkdir(parents=True, exist_ok=True)

    res_file = Path(final_dest + fr"/{file.name}")
    
    l.log.info("Checking file existence...")
    if (res_file.exists()):
        l.log.info("Sorted file already exists!")
        return

    l.log.info("Copying file...")
    shutil.copy(file, res_file)
    l.log.info("Success!")


# def startup_procedures():
#     update_glob_vars(import_data_dict_json())

def startup_procedures(entry_values: tuple):
    update_glob_vars(entry_values)


# def sort():
#     l.log.info(">>> >>> PROGRAM START <<< <<<")
    
#     l.log.info("Backend checks...")
#     startup_procedures()
#     global steam
#     steam = sas.steam_access(steam_key)

#     l.log.info("Attaining local game list data.")
#     local_game_dict = import_game_dict_json()
#     image_iter(local_game_dict)
#     l.log.info("All images copied and sorted!")

#     l.log.info("Updating game_list_data.json...")
#     update_dict_json(local_game_dict, DEFAULT_GAME_JSON_PATH)
#     l.log.info("Success!")

#     l.log.info(">>> >>> All ACTIONS COMPLETED <<< <<<")

def sort(entry_values: tuple):
    l.log.info(">>> >>> PROGRAM START <<< <<<")
    
    l.log.info("Backend checks...")
    startup_procedures(entry_values)
    global steam
    steam = sas.steam_access(steam_key)

    l.log.info("Attaining local game list data.")
    local_game_dict = import_game_dict_json()
    image_iter(local_game_dict)
    l.log.info("All images copied and sorted!")

    l.log.info("Updating game_list_data.json...")
    update_dict_json(local_game_dict, DEFAULT_GAME_JSON_PATH)
    l.log.info("Success!")

    l.log.info(">>> >>> All ACTIONS COMPLETED <<< <<<")


if __name__ == "__main__":
    sort()