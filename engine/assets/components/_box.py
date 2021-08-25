"""box.py contains the component that draws a basic rectangle.
"""

import pygame
from ..._component import Component


class Box(Component):

    def __init__(self, the_name, the_engine=None, **kwargs):
        super().__init__(the_name, the_engine)
        self.color = kwargs.get('the_color', 'black')
        self.rect = kwargs.get('the_rect', None)
        self.border = kwargs.get('the_border', 0)

    def callback_out_of_bounds(self, **kwargs):
        print("callback with {}\n".format(kwargs))

    def on_after_update(self):
        self.rect = self.entity.transform.get_rect()

    def on_load(self):
        if self.rect is None:
            self.rect = self.entity.transform.get_rect()

    def on_render(self):
        pygame.draw.rect(self.engine.pygame_screen, self.color, self.rect, self.border)

    def on_start(self):
        a_component = self.entity.get_component("OutOfBounds")
        self.engine.delegate_manager.register_callback_to_delegate(self, a_component.delegate, self.callback_out_of_bounds)
