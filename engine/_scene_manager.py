"""_game_manager.py contains the SceneManager base class, used to custom handle
any scene in the game.
"""

from ._eobject import EObject
from ._loggar import Log


class ActiveScene:
    """ActiveScene class identifies the active scene.
    """

    def __init__(self, the_scene, the_index):
        """__init__ initializes the ActiveScene instance.
        """
        self.scene = the_scene
        self.index = the_index


class SceneManager(EObject):
    """SceneManager class implements the base class for any custom scene.
    """

    def __init__(self, the_name, the_engine=None):
        """__init__ initializes the SceneManager instance.

        Args:
            the_name (str): String with the SceneManager name.
        """
        super().__init__(the_name, the_engine)
        self.scenes = []
        self.active_scene = None
        self.standby_scene = None

    def add_scene(self, the_scene):
        """add_scene adds the given scene to the SceneManager.

        Args:
            the_scene (Scene): Scene instance to be added to the SceneManager.

        Returns:
            bool : True if scene was properly added to the SceneManager, or
                False if there was any problem adding the scene.
        """
        Log.SceneManager(self.name).AddScene(the_scene.name).call()
        if self.get_scene_by_id(the_scene.id):
            return False
        the_scene.engine = self.engine
        self.scenes.append(the_scene)
        return True

    def assign_active_scene(self, the_scene=None, the_scene_index=0):
        """assign_active_scene assigns the given scene or scene index
        as the active scene without running the scene per se.
        """
        if the_scene is None:
            the_scene = self.scenes[the_scene_index]
        else:
            the_scene_index = self.get_scene_index_by_id(the_scene.id)
        self.active_scene = ActiveScene(the_scene, the_scene_index)

    def delete_scene(self, the_id):
        """delete_scene deletes the given scene by the scene id from the
        SceneManager.

        Args:
            the_id (str): string with the id of the scene to delete from the
                SceneManager.

        Returns:
            bool : True if scene was deleted from the SceneManager or False if
                scene was not found.
        """
        Log.SceneManager(self.name).DeleteScene(the_id).call()
        a_scene = self.get_scene_by_id(the_id)
        if a_scene is None:
            return False
        a_scene.engine = None
        self.scenes.remove(a_scene)
        return True

    def get_scene_by_id(self, the_id):
        """get_scene_by_id returns a scene in the SceneManager by the scene id.

        Args:
            the_id (str): string with the scene id to look for.

        Returns:
            Scene : scene instance if it is found or None if not.
        """
        for a_scene in self.scenes:
            if a_scene.id == the_id:
                return a_scene
        return None

    def get_scene_index_by_id(self, the_id):
        """get_scene_index_by_id returns the scene index in the SceneManager
        by the given scene id.

        Args:
            the_id (str): string with the scene id to look for.

        Returns:
            int : scene index.
        """
        for a_scene_index, a_scene in self.scenes:
            if a_scene.id == the_id:
                return a_scene_index
        return None

    def is_active_scene(self, the_scene_id):
        """is_active_scene returns if the given scene id belongs to the
        active scene.
        """
        return self.active_scene.scene.id == the_scene_id

    def on_after_update(self):
        """on_after_update calls all on_after_update methods for every asset..
        """
        super().on_after_update()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_after_update()

    # def on_cleanup(self):
    #     """on_cleanup cleans up all assets.
    #     """
    #     Log.SceneManager(self.name).OnCleanUp().call()

    def on_end(self):
        """on_end calls all on_end for all scenes.
        """
        super().on_end()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_end()

    def on_frame_end(self):
        """on_frame_end calls on_frame_end for the active scene.
        """
        super().on_frame_end()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_frame_end()

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of a tick frame.
        """
        super().on_frame_start()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_frame_start()

    def on_init(self):
        """on_init initializes all SceneManager assets and resources.
        """
        super().on_init()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_init()

    def on_render(self):
        """on_render calls all on_render methods for every asset.
        """
        super().on_render()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_render()

    def on_start(self):
        """on_start calls all on_start methods for every asset.
        """
        super().on_start()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_start()

    def on_update(self):
        """on_update calls all on_update methods for every asset.
        """
        super().on_update()
        if self.active_scene and self.active_scene.scene:
            self.active_scene.scene.on_update()

    def restart_scene(self):
        """restart_scene restars the active scene.
        """
        if self.active_scene is None:
            return False
        return self.set_active_scene(self.active_scene)

    def _set_active_scene(self, the_scene, the_index):
        """_set_active_scene sets the given scene and index and active one. It
        proceeds to unload previous scene active and load new one.
        """
        if self.active_scene is not None:
            self.active_scene.scene.on_destroy()
        self.active_scene.scene = the_scene
        self.active_scene.index = the_index
        self.active_scene.scene.run_code()
        self.active_scene.scene.on_load()
        self.active_scene.scene.on_start()

    def set_active_scene(self, the_scene):
        """set_active_scene sets the given scene as the active scene.
        """
        if the_scene is None:
            return False
        if not self.get_scene_by_id(the_scene.id):
            return False
        # Event Manager creates an scene event with the given scene.
        return True

    def set_active_first_scene(self):
        """set_active_first_scene sets the first scene as the active one.
        """
        if len(self.scenes) == 0:
            return None
        self._set_active_scene(self.scenes[0], 0)
        return self.active_scene

    def set_active_last_scene(self):
        """set_active_last_scene sets the last scene as the active one.
        """
        if len(self.scenes) == 0:
            return None
        self._set_active_scene(self.scenes[-1], len(self.scenes) - 1)
        return self.active_scene

    def set_active_next_scene(self):
        """set_active_next_scene sets the next scene as the active one.
        """
        if len(self.scenes) == 0 or self.active_scene.index >= len(self.scenes):
            return None
        a_index = self.active_scene.index + 1
        a_scene = self.scenes[a_index]
        return self._set_active_scene(a_scene, a_index)

    def set_active_prev_scene(self):
        """set_active_prev_scene sets the previous scene as the active one.
        """
        if len(self.scenes) == 0 or self.active_scene.index == 0:
            return None
        a_index = self.active_scene.index - 1
        a_scene = self.scenes[a_index]
        return self._set_active_scene(a_scene, a_index)
