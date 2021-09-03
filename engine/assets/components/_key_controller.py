"""_key_controller.py component control keyboard actions with arrow
keys.
"""

from pygame.locals import *
from ..._component import Component


class KeyController(Component):

    KEYBOARD_EVENT_NAME = "keyboard-event"

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes KeyController instance.
        """
        super().__init__(the_name, the_engine)

    def on_load(self):
        """on_load is called all on_load methods.
        """
        super().on_load()
        self.delegates[self.KEYBOARD_EVENT_NAME] = self.engine.delegate_manager.create_delegate(self, self.KEYBOARD_EVENT_NAME)

    def on_update(self):
        """on_update calls all on_update methods.
        """
        a_key_pressed = self.engine.pygame_key_pressed
        for a_key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
            if a_key_pressed[a_key]:
                # self.react_to_pressed_key(a_key)
                self.engine.delegate_manager.trigger_delegate(self.delegates[self.KEYBOARD_EVENT_NAME].id, True, the_key=a_key)


    def react_to_pressed_key(self, the_key):
        """react_to_pressed_key execute some code when key is being pressed.
        """
        a_position = self.entity.transform.position
        if the_key == K_UP:
            a_position.y -= 5
        if the_key == K_DOWN:
            a_position.y += 5
        if the_key == K_LEFT:
            a_position.x -= 5
        if the_key ==K_RIGHT:
            a_position.x += 5
