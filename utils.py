import json
import colorama
from colorama import Fore, Back, Style

class Debug:
    def __init__(self):
        self.do_debug = False
        colorama.init()

    def __call__(self, *args, **kwargs):
        if self.do_debug:
            print(f"{Fore.MAGENTA}DEBUG:", *args, **kwargs, end="")
            print(Fore.RESET)
debug = Debug()
debug("Test")

def get_json_as_dict(path: str) -> dict:
    with open(path, "r") as file:
        rez = json.load(file)
    return rez

