"""_move_to contains component that controls movement in a given direction.
"""

import pygame
from ..._component import Component


class MoveTo(Component):
    """MoveTo class implements component that control movement in a given
    direction.
    """

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes MoveTo instance.
        """
        super().__init__(the_name, the_engine, **kwargs)
        self.speed = kwargs.get("the_speed", pygame.Vector2(0, 0))
        self.behavior = kwargs.get("the_behavior", None)

    def callback_key_controller(self, the_key):
        """callback_key_controller is the callback to be called when a key is
        being pressed.
        """
        self.speed = self.behavior["KeyController"][the_key]

    def on_start(self):
        """on_start calls start methods.
        """
        if self.behavior is None:
            return
        for a_key, a_value in self.behavior.items():
            a_delegate = None
            a_key_split = a_key.split(":")
            if a_key_split[0] == "component":
                a_component = self.entity.get_component(a_key_split[1])
                if a_component:
                    a_delegate_name = a_key_split[2] if len(a_key_split) == 3 else None
                    a_delegate = a_component.get_delegate(a_delegate_name)
            elif a_key_split[0] == "entity":
                a_scene = self.entity.scene
                a_scene_entity = a_scene.lookup_by_name(a_scene.entities, a_key_split[1])
                a_scene_component = a_scene_entity.lookup_by_name(a_scene_entity.components, a_key_split[2])
                a_delegate_name = a_key_split[3] if len(a_key_split) == 4 else None
                a_delegate = a_scene_component.get_delegate(a_delegate_name)
            elif a_key_split[0] == "scene":
                a_scene = self.entity.scene
                a_scene_entity = a_scene.lookup_by_name(a_scene.entities, a_scene.SCENE_HANDLER_ENTITY_NAME)
                a_scene_component = a_scene_entity.lookup_by_name(a_scene_entity.components, a_scene.SCENE_HANDLER_COMPONENT_NAME)
                a_delegate_name = a_key_split[1] if len(a_key_split) == 2 else None
                a_delegate = a_scene_component.get_delegate(a_delegate_name)
            if a_delegate:
                # self.engine.delegate_manager.register_callback_to_delegate(self, a_component.delegate, self.callback_key_controller)
                self.engine.delegate_manager.register_callback_to_delegate(self, a_delegate, a_value(self))

    def on_update(self):
        """on_update calls all on_update methods.
        """
        super().on_update()
        self.entity.transform.position.x += self.speed.x
        self.entity.transform.position.y += self.speed.y
