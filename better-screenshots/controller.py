import file_sorter as fs
import logging

log = logging.getLogger(__name__)


def save_settings(key_text: str, src_text: str, dest_text: str):
    '''Get values from GUI and send to file_sorter'''
    res_dict = {"Key": key_text, "Src": src_text, "Dest": dest_text}
    fs.update_dict_json(res_dict, fs.DEFAULT_DATA_JSON_PATH)


def get_settings() -> dict:
    '''Get saved key, src, and dest from file_sorter'''
    return fs.import_data_dict_json()


def run_sort(entry_values: tuple):
    '''Run sorting algotithm in file_sorter with data from entry widgets'''
    fs.sort(entry_values)