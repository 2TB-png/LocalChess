import pygame as pyg
from ui_elements.ui_element import Element

class Button(Element):
    def __init__(self, pos, width, height, text, font, # Basics
                 command=lambda *args:print("Button pressed"), args=(), kwargs=(), #Command setup
                 fg=(150, 150, 150), bg=(100, 100, 100), font_color=(0,0,0), roundness=10, depth=10, push_depth=5): # Style

        super().__init__(pos, width, height, element_type="button")
        # Command control
        self.__text = text
        self.__command = command
        self.__command_args = args
        self.__command_kwargs = kwargs

        # Style
        self.__roundness = roundness
        self.__depth = depth
        self.__push_depth = push_depth
        self.__bg = bg
        self.__fg = fg
        self.__font_color = font_color
        self.__font = font

        # State
        self.mouse_was_down = False
        self.is_active = False
        self.hover = False

    def display_visuals(self, screen):

        text = self.__font.render(self.__text, True, "black")
        text_r = text.get_rect()
        text_x = self.get_pos()[0] + (self.__rect.w-text_r.w)//2
        text_y = self.get_pos()[1] + (self.__rect.h-text_r.h)//2

        pyg.draw.rect(screen, self.__bg,
                      pyg.Rect(self.__rect.x, self.__rect.y+self.__depth, self.__rect.w, self.__rect.h),
                      border_radius=self.__roundness)
        if self.is_active and self.hover:
            pyg.draw.rect(screen, self.__fg,
                          pyg.Rect(self.__rect.x, self.__rect.y + self.__push_depth, self.__rect.w, self.__rect.h),
                          border_radius=self.__roundness)

            screen.blit(text, (text_x, text_y + self.__push_depth))

        else:
            pyg.draw.rect(screen, self.__fg, self.__rect, border_radius=self.__roundness)
            screen.blit(text, (text_x, text_y))




    def update(self, screen):
        mouse = pyg.mouse
        mouse_pos = mouse.get_pos()
        mouse_down = mouse.get_pressed()[0]
        self.hover = self.__rect.collidepoint(mouse_pos[0], mouse_pos[1])

        if mouse_down and self.hover and not self.mouse_was_down:
            self.is_active =True
        if self.is_active and self.mouse_was_down and self.hover and not mouse_down :
            self.__command(*self.__command_args)
        if not mouse_down:
            self.is_active = False

        self.mouse_was_down = mouse_down

        self.display_visuals(screen)

    def __str__(self):
        return f"<Button with text '{self.__text}' of type {self.__type} at ({self.__rect.x, self.__rect.y})>"

    def __repr__(self):
        return f"<Button(type={self.__type}, pos=({self.__rect.x, ",", self.__rect.y}), width={self.__rect.w}, height={self.__rect.h}, text='{self.__text}', fg={self.__fg}, bg={self.__fg}, font_color={self.__font_color}, roundness={self.__roundness}, depth={self.__depth}, push_depth={self.__push_depth})>"
