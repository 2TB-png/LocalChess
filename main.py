from sys import exit
from os import getenv

import pygame as pyg

import ui_elements as ui
import utils


NAME = "Local chess"
VERSION = "v0.1"

MODE = getenv("MODE")

config = utils.get_json_as_dict("config.json")
WIDTH = config["width"]
HEIGHT = config["height"]

def main():

    screen = pyg.display.set_mode((WIDTH, HEIGHT))
    pyg.display.set_caption(f"{NAME}  {VERSION}")

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()


        pyg.display.update()


if __name__ == '__main__':
    main()
