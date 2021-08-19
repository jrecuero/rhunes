"""box.py contains the component that draws a basic rectangle.
"""

import pygame
from ..._component import Component


class Box(Component):

    def __init__(self, the_name, the_engine=None, **kwargs):
        super().__init__(the_name, the_engine)
        self.color = kwargs.get('the_color', 'black')
        self.rect = kwargs.get('the_rect', (0, 0, 10, 10))
        self.border = kwargs.get('the_border', 0)


    def on_render(self):
        pygame.draw.rect(self.engine.screen, self.color, self.rect, self.border)

