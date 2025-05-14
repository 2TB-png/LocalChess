import pygame as pyg
from ui_elements.ui_element import Element

class Label(Element):
    def __init__(self, pos, width, height, text=""):
        super().__init__(pos, width, height)
        self.__text = text
        self.__font = pyg.font.Font("Mono.ttf", 32)
        self.__bg = (100, 100, 100)
        self.__roundness = 10

    def change___text(self, __text):
        self.__text = __text

    def update(self, screen):
        __text = self.__font.render(self.__text, True, "black")
        __text_r = __text.get_rect()
        __text_x = self.rect.x + self.rect.w - __text_r.w
        __text_y = self.rect.y + (self.rect.h - __text_r.h) // 2

        pyg.draw.rect(screen, self.__bg, self.rect, border_radius=self.__roundness)

        screen.blit(__text, (__text_x, __text_y))
