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

