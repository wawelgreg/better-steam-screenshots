# Better Steam Screenshots
Better Steam Screenshots is a GUI app that organizes a copy of your uncompressed external Steam screenshots into an easily navigable sorted structure of folders.

<p align="center">
  <img src="https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/b58919fe-21b1-47db-a6b9-ed9f90469d0b">
  <img src="https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/2862a29c-151d-4c68-abc0-06d5759e5609" width="500" align="center">
</p>


### Before:
```
External-screenshots/
├── 34900_20240602143223_1.png
├── 34900_20240602143224_1.png
├── 34900_20240602143225_1.png
├── 427520_20240530161026_1.png
├── 427520_20240530161031_1.png
├── 427520_20240530161032_1.png
├── 427520_20240602140755_1.png
├── 427520_20240602140757_1.png
├── 427520_20240602140757_2.png
├── 427520_20240602140757_3.png
└── 427520_20240602140758_1.png
```

### After:
```
External-screenshots/
├── 34900_20240602143223_1.png
├── 34900_20240602143224_1.png
├── 34900_20240602143225_1.png
├── 427520_20240530161026_1.png
├── 427520_20240530161031_1.png
├── 427520_20240530161032_1.png
├── 427520_20240602140755_1.png
├── 427520_20240602140757_1.png
├── 427520_20240602140757_2.png
├── 427520_20240602140757_3.png
├── 427520_20240602140758_1.png
└── Sorted-Screenshots/
    ├── BadRatstheRatsRevenge/
    │   └── 2024/
    │       └── 06-02/
    │           ├── 34900_20240602143223_1.png
    │           ├── 34900_20240602143224_1.png
    │           └── 34900_20240602143225_1.png
    └── Factorio/
        └── 2024/
            ├── 05-30/
            │   ├── 427520_20240530161026_1.png
            │   ├── 427520_20240530161031_1.png
            │   └── 427520_20240530161032_1.png
            └── 06-02/
                ├── 427520_20240602140755_1.png
                ├── 427520_20240602140757_1.png
                ├── 427520_20240602140757_2.png
                ├── 427520_20240602140757_3.png
                └── 427520_20240602140758_1.png
```

## How it Works:
The app takes your external screenshots (all located together in one directory where steam sends them), parses the file names for information regarding steam game ID and date information, references either the locally-saved json or Steam Web API for getting the string name of the game, reformats the name of the game into a legal directory name, and then creates year -> month-day directories for where those copied screenshots are finally pasted.

## API + Libraries:
### API
- [python-steam-api 2.0.2](https://pypi.org/project/python-steam-api/)
  - Used to correlate the game IDs parsed from the screenshot filenames to the title of the game used in the naming of the sorted directories.

### GUI
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)
   - Library that powers the GUI of the app with a more modern look and feel.

### Paths Libirary
- [Pathlib](https://docs.python.org/3/library/pathlib.html)
   - Library that offers the ability for this application to work on multiple OS and their respective Windows or Posix Paths.

## Usage:
1. Download the repo (or clone it locally)
2. Make sure you have installed Python **3.0+**, Python Steam API, CustomTkinter, and lastly, get your Steam API Key:
   * [Python 3 Download](https://www.python.org/downloads/)
   * `pip install python-steam-api`
   * `pip install customtkinter`
   * *IMPORTANT*: [Steam API Web Key](https://steamcommunity.com/dev/apikey)
3. Run `gui.py` from a Python3-compatible editor
4. With the app open and running, fill-in these fields:
   * Your steam api key
   * External screenshot path
   * Destination path of your sorted images
* Optional: If you want your settings to be saved for future sorting of more images, click `Save Selections`
5. Click `Sort my images!` and sorted copies of your images will be stored at the destination path you set

Enjoy! :)

## Design:
For the overall design on the structure of this program, I went with the Model View Controller (MVC) design pattern. I split the program into three parts- GUI, Controller, and File Sorter- in order to make maintenence and expansion much easier, as any modular architecture with seperate objects typicially provides. Two JSON files, `game_list_data.json` and `data.json`, are used to store the user's saved entry options (Steam API Key, Screenshot Source Path, and Sorted Screenshot Destination Path) for when they open the application again, while the `data.json` file is used to store automatically generated/updated dictionry lists of saved correlated game IDs to their game names which are found with the help of the Steam Web API. With the locally stored `data.json` file, the Steam API does not need to be called much at all if the list of screenshots usually comes from 3-4 different games max.
