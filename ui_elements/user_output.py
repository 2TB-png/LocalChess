import pygame as pyg
from ui_elements.ui_element import Element

class Label(Element):
    def __init__(self, pos, width, height, text=""):
        super().__init__(pos, width, height)
        self.text = text
        self.font = pyg.font.Font("Mono.ttf", 32)
        self.bg = (100, 100, 100)
        self.roundness = 10

    def change_text(self, text):
        self.text = text

    def update(self, screen):
        text = self.font.render(self.text, True, "black")
        text_r = text.get_rect()
        text_x = self.rect.x + self.rect.w - text_r.w
        text_y = self.rect.y + (self.rect.h - text_r.h) // 2

        pyg.draw.rect(screen, self.bg, self.rect, border_radius=self.roundness)

        screen.blit(text, (text_x, text_y))
