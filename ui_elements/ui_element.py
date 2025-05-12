import pygame as pyg

class Element:
    def __init__(self, pos, width, height, element_type="ui_element"):
        self.rect = pyg.Rect(pos, (width, height))
        self.type = element_type

    def move_to(self, new_pos):
        self.rect.x, self.rect.y = new_pos

    def get_pos(self):
        return self.rect.x, self.rect.y

    def update(self, screen):
        pass

    def render_debug(self, screen, debug_color="red", border_width=1):
        pyg.draw.rect(screen, debug_color, self.rect, border_width)