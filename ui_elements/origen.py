from ui_elements.group import Group

class Origen(Group):
    def __init__(self, pos, width=0, height=0, render_debug=False, debug_color="red", border_width=1):
        super().__init__(pos=pos, width=width, height=height, render_debug=render_debug, debug_color=debug_color, border_width=border_width)

    def update(self, screen):
        for element in self.get_elements():

            el_pos = element.get_pos()
            pos = self.get_pos()
            element.move_to((el_pos[0] + pos[0], el_pos[1] + pos[1]))

            element.update(screen)

            if self.render_debug:
                element.render_debug(screen, debug_color=self.debug_color, border_width=self.border_width)

            element.move_to((el_pos[0], el_pos[1]))

