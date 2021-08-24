"""_key_controller.py component control keyboard actions with arrow
keys.
"""

from pygame.locals import *
from ..._component import Component


class KeyController(Component):

    def __init__(self, the_name, the_engine=None, **kwargs):
        super().__init__(the_name, the_engine)

    def on_update(self):
        a_key_pressed = self.engine.pygame_key_pressed
        a_position = self.entity.transform.position
        if a_key_pressed[K_UP]:
            a_position.y -= 5
        if a_key_pressed[K_DOWN]:
            a_position.y += 5
        if a_key_pressed[K_LEFT]:
            a_position.x -= 5
        if a_key_pressed[K_RIGHT]:
            a_position.x += 5