import file_sorter as fs
from log_manager import log

# Get values from gui and send to file_sorter
def save_settings(key_text: str, src_text: str, dest_text: str):
    res_dict = {"Key": key_text, "Src": src_text, "Dest": dest_text}
    fs.update_dict_json(res_dict, fs.DEFAULT_DATA_JSON_PATH)


# Get saved key, src, and dest from file_sorter
def get_settings() -> dict:
    return fs.import_data_dict_json()


# Run sorting algorithm in file_sorter
# def run_sort():
#     fs.sort()

# Run sorting algorithm in file_sorter with data from entry widgets
def run_sort(entry_values: tuple):
    fs.sort(entry_values)