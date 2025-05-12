from ui_elements.ui_element import Element

class Group(Element):
    def __init__(self, pos=(0,0), width=0, height=0, render_debug=False, debug_color="red", border_width=1):
        super().__init__(pos, width, height, element_type="group")

        # Debug tools
        self.render_debug = render_debug
        self.debug_color=debug_color
        self.border_width = border_width

        self.__elements = []

        self.compatible_elements = [
            "ui_element",
            "button",
            "group"
        ]
    def append(self, *elements):

        for element in elements:
            if element.type not in self.compatible_elements:
                raise TypeError(f"Type '{element.type}' is not supported!")
            else:
                self.__elements.append(element)

    def get_elements(self):
        return self.__elements.copy()

    def update(self, screen):
        for element in self.__elements:
            element.update(screen)
            if self.render_debug:
                element.render_debug(screen, debug_color=self.debug_color, border_width=self.border_width)
