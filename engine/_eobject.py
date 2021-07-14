"""_eobject extends IObject for any object making use of the Engine.
"""

from ._iobject import IObject


class EObject(IObject):
    """EObject extends IObject for any object using the Engine.
    """

    def __init__(self, the_engine, the_name):
        """__init__ initializes an EObject instance.
        """
        super().__init__(the_name)
        self.engine = the_engine

    def get_cursor_manager(self):
        """get_cursor_manager returns the engine CursorManager.
        """
        return self.engine.cursor_manager

    def get_delegate_manager(self):
        """get_delegate_manager returns the engine DelegateManager.
        """
        return self.engine.delegate_manager

    def get_event_manager(self):
        """get_event_manager returns the engine EventManager.
        """
        return self.engine.event_manager

    def get_font_manager(self):
        """get_font_manager returns the engine FontManager.
        """
        return self.engine.font_manager

    def get_game_manager(self):
        """get_game_manager returns engine GameManager instance.
        """
        return self.engine.game_manager

    def get_resource_manager(self):
        """get_resource_manager returns engine ResourceManager instance.
        """
        return self.engine.resource_manager

    def get_scene_manager(self):
        """get_scene_manager returns engine SceneManager instance.
        """
        return self.engine.scene_manager

    def get_sound_manager(self):
        """get_sound_manager returns engine SoundManager instance.
        """
        return self.engine.sound_manager
