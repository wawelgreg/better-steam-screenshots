# Better Steam Screenshots
<p align="center">
  <img src="https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/b58919fe-21b1-47db-a6b9-ed9f90469d0b">
  <img src="https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/2862a29c-151d-4c68-abc0-06d5759e5609" width="500" align="center">
</p>


Before:
![image](https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/659a061f-bce6-4819-b328-4107482ddbd6)
After:
![image](https://github.com/wawelgreg/better-steam-screenshots/assets/141285799/6c1198c8-f47b-47aa-8d82-7cd747baf4ea)


## Goal
The goal of this project is to better the uncompressed screenshot experience from steam by automatically sorting said images to folders based on game title -> year -> session day of game played and general automatic file manipulation pracitces. This aims to better enhance the screenshot experience for Steam screenshot artists out there by taking their long existing list of saved external screenshots and sorting them in a more user-friendly searching manner.

## API
- [python-steam-api 2.0.2](https://pypi.org/project/python-steam-api/)

## GUI
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [CustomTkinter](https://customtkinter.tomschimansky.com/)

## How It Works
After filling-out the config with your generated steam key, external screenshot directory path, and source directory path for where your sorted uncompressed screenshots shall be copied, the program will use the saved *game_list_data.json* file along with any new game titles that need to be fetched from the Steam Web API to store copies of your uncompressed external screenshots to their respective sorted directories.

## TODO
- [x] Base functionality
- [ ] Implement Functional GUI
- [ ] Make executable
