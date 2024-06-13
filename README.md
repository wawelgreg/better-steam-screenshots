# Better Steam Screenshots
<p align="center">
  <img src="https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/b58919fe-21b1-47db-a6b9-ed9f90469d0b">
  <img src="https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/2862a29c-151d-4c68-abc0-06d5759e5609" width="500" align="center">
</p>


Before:
![image](https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/659a061f-bce6-4819-b328-4107482ddbd6)
After:
![image](https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/6c1198c8-f47b-47aa-8d82-7cd747baf4ea)

## Goal + Background:
The goal of this project is to better the uncompressed screenshot experience from steam by automatically sorting said images to folders based on game title -> year -> session day of game played and general automatic file manipulation pracitces. This aims to better enhance the screenshot experience for Steam screenshot artists out there by taking their long existing list of saved external screenshots and sorting them in a more user-friendly searching manner. I have made plenty of artistic pictures myself that I have taken over the years with different online communities over the years- be it for personal use, sharing with friends, saving fond memories, or even for usage in community content, media, banners, etc.

## API + Libraries:
### API
- [python-steam-api 2.0.2](https://pypi.org/project/python-steam-api/)

### GUI
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)

### Paths Libirary
- [Pathlib](https://docs.python.org/3/library/pathlib.html)

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
5. Click `Sort my images!` and sorted copies of your images will be stored at the destination path you set.
Enjoy! :)
