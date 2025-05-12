import pygame as pyg
from ui_elements.ui_element import Element

class Button(Element):
    def __init__(self, pos, width, height, text, command=lambda *args:print("Button pressed"), args=()):
        super().__init__(pos, width, height, element_type="button")
        self.command = command
        self.command_args = args
        self.text = text

        self.mouse_was_down = False
        self.is_active = False
        self.hover = False
        
        self.roundness = 10
        self.depth = 10
        self.push_depth = 5
        self.bg = (100, 100, 100)
        self.fg = (150, 150, 150)
        self.active = 0

        self.font = pyg.font.Font("Mono.ttf", 32)

    def display_visuals(self, screen):

        text = self.font.render(self.text, True, "black")
        text_r = text.get_rect()
        text_x = self.get_pos()[0] + (self.rect.w-text_r.w)//2
        text_y = self.get_pos()[1] + (self.rect.h-text_r.h)//2

        pyg.draw.rect(screen, self.bg,
                      pyg.Rect(self.rect.x, self.rect.y+self.depth, self.rect.w, self.rect.h),
                      border_radius=self.roundness)
        if self.is_active and self.hover:
            pyg.draw.rect(screen, self.fg,
                          pyg.Rect(self.rect.x, self.rect.y + self.push_depth, self.rect.w, self.rect.h),
                          border_radius=self.roundness)

            screen.blit(text, (text_x, text_y + self.push_depth))

        else:
            pyg.draw.rect(screen, self.fg, self.rect, border_radius=self.roundness)
            screen.blit(text, (text_x, text_y))




    def update(self, screen):
        mouse = pyg.mouse
        mouse_pos = mouse.get_pos()
        mouse_down = mouse.get_pressed()[0]
        self.hover = self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

        if mouse_down and self.hover and not self.mouse_was_down:
            self.is_active =True
        if self.is_active and self.mouse_was_down and self.hover and not mouse_down :
            self.command(*self.command_args)
        if not mouse_down:
            self.is_active = False

        self.mouse_was_down = mouse_down

        self.display_visuals(screen)
