"""box.py contains the component that draws a basic rectangle.
"""

import pygame
from ..._component import Component


class Box(Component):

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes Box instance.
        """
        super().__init__(the_name, the_engine)
        self.color = kwargs.get('the_color', 'black')
        self.rect = kwargs.get('the_rect', None)
        self.border = kwargs.get('the_border', 0)

    def callback_out_of_bounds(self, **kwargs):
        """callback_out_of_bounds is being called when entity is out of
        bounds.
        """
        print("callback with {}\n".format(kwargs))

    def on_after_update(self):
        """on_after_update calls all on_after_update methods.
        """
        self.rect = self.entity.transform.get_rect()

    def on_load(self):
        """on_load is called when instance is loaded.
        """
        if self.rect is None:
            self.rect = self.entity.transform.get_rect()

    def on_render(self):
        """on_render calls all on_render methods.
        """
        pygame.draw.rect(self.engine.pygame_screen, self.color, self.rect, self.border)

    def on_start(self):
        """on_start calls start methods.
        """
        # a_component = self.entity.get_component("OutOfBounds")
        # if a_component:
        #     self.engine.delegate_manager.register_callback_to_delegate(self, a_component.delegate, self.callback_out_of_bounds)
