from sys import exit
from os import getenv

import pygame as pyg

import ui_elements as ui
from ui_elements import utils
import colors

pyg.init()

NAME = "Local chess"
VERSION = "v0.1"

MODE = getenv("MODE")

config = utils.get_json_as_dict("config.json")
WIDTH = config["width"]
HEIGHT = config["height"]

MONO = pyg.font.Font("assets/Mono.ttf", 32)

def main():

    b1 = ui.Button((100, 100), 300, 100, "Easy button", font=MONO)

    screen = pyg.display.set_mode((WIDTH, HEIGHT))
    pyg.display.set_caption(f"{NAME}  {VERSION}")

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit()
        screen.fill(colors.nice_purple)
        b1.update(screen)
        pyg.display.update()


if __name__ == '__main__':
    main()
