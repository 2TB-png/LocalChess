import pygame as pyg

class Element:
    def __init__(self, pos, width, height, element_type="ui_element"):
        self.__rect = pyg.Rect(pos, (width, height))
        self.__type = element_type

    def move_to(self, new_pos):
        self.__rect.x, self.__rect.y = new_pos

    def get_pos(self):
        return self.__rect.x, self.__rect.y

    def update(self, screen):
        ...

    def render_debug(self, screen, debug_color="red", border_width=1):
        pyg.draw.rect(screen, debug_color, self.__rect, border_width)

    def __str__(self):
        return f"<Element of type {self.__type} at ({self.__rect.x, self.__rect.y})>"

    def __repr__(self):
        return f"<Element(type={self.__type}, pos=({self.__rect.x, ",", self.__rect.y}), width={self.__rect.w}, height={self.__rect.h})>"
