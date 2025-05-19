import pygame as pyg
from ui_elements.ui_element import Element

class Label(Element):
    def __init__(self, pos, width, height, text=""):
        super().__init__(pos, width, height)
        self.__text = text
        self.__font = pyg.font.Font("Mono.ttf", 32)
        self.__bg = (100, 100, 100)
        self.__roundness = 10

    def change_text(self, text):
        self.__text = text

    def update(self, screen):
        text = self.__font.render(self.__text, True, "black")
        text_r = text.get_rect()
        text_x = self.__rect.x + self.__rect.w - text_r.w
        text_y = self.__rect.y + (self.__rect.h - text_r.h) // 2

        pyg.draw.rect(screen, self.__bg, self.__rect, border_radius=self.__roundness)

        screen.blit(text, (text_x, text_y))

    def __str__(self):
        return f"<Label of type {self.__type} at ({self.__rect.x, self.__rect.y})>"

    def __repr__(self):
        return f"<Label(type={self.__type}, pos=({self.__rect.x, ",", self.__rect.y}), width={self.__rect.w}, height={self.__rect.h})>"
