"""_scene_handler.py contains scene component.
"""

from ..._component import Component
from ..._scene import Scene


class SceneHandlerComponent(Component):
    """SceneHandlerComponent class implements scene component.
    """

    # ON_COLLISION_EVENT_NAME = "on-collision-event"
    # ON_DESTROY_EVENT_NAME = "on-destroy-event"
    # ON_LOAD_EVENT_NAME = "on-load_event"

    def __init__(self, the_name, the_engine=None, **kwargs):
        super().__init__(the_name, the_engine, **kwargs)

    def on_load(self):
        """on_load is called all on_load methods.
        """
        super().on_load()
        self.delegates[Scene.ON_COLLISION_EVENT_NAME] = self.engine.delegate_manager.create_delegate(self, Scene.ON_COLLISION_EVENT_NAME)
        self.delegates[Scene.ON_DESTROY_EVENT_NAME] = self.engine.delegate_manager.create_delegate(self, Scene.ON_DESTROY_EVENT_NAME)
        self.delegates[Scene.ON_LOAD_EVENT_NAME] = self.engine.delegate_manager.create_delegate(self, Scene.ON_LOAD_EVENT_NAME)