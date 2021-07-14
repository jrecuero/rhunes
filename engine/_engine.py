"""_engine.py contains the main engine module which drives and handles
all application.
"""

from ._loggar import Log


class Engine:
    """Engine class is the main class that drives and handles all application.
    """

    __instance = None

    @staticmethod
    def get():
        """get is an Engine static method that returns the singleton instance.
        """
        if Engine.__instance is None:
            raise Exception("Engine not created!")
        return Engine.__instance

    @staticmethod
    def delete():
        """delete is an Engine static method that deletes the singleton instance.
        """
        if Engine.__instance is None:
            raise Exception("Engine not created!")
        Engine.__instance = None


    def __init__(self, the_name="engine", the_width=640, the_height=480, **kwargs):
        """__init__ initializes singleton Engine instance.

        Args:
            the_name (str): Engine instance name.
            the_width (int): screen width for the application.
            the_height (int): screen height for the application.
        """
        if Engine.__instance is not None:
            raise Exception("Engine can be only one!")
        Engine.__instance = self
        Log.Engine(the_name).New((the_width, the_height)).call()
        self.name = the_name
        self.width = the_width
        self.height = the_height
        self.active = False
        self.managers = {
            "cursor-manager": kwargs.get("the_cursor_manager", None),
            "delegate-manager": kwargs.get("the_delegate_manager", None),
            "event-manager": kwargs.get("the_event_manager", None),
            "font-manager": kwargs.get("the_font_manager", None),
            "game-manager": kwargs.get("the_game_manager", None),
            "resource-manager": kwargs.get("the_resource_manager", None),
            "scene-manager": kwargs.get("the_scene_manager", None),
            "sound-manager": kwargs.get("the_sound_manager", None), }

    @property
    def cursor_manager(self):
        """cursor_manager returns Engine CursorManager instance.
        """
        return self.managers["cursor-manager"]

    @cursor_manager.setter
    def cursor_manager(self, the_value):
        """cursor_manager setter sets Engine CursorManage instance.
        """
        self.managers["cursor-manager"] = the_value

    @property
    def delegate_manager(self):
        """delegate_manager returns Engine DelegateManager instance.
        """
        return self.managers["delegate-manager"]

    @delegate_manager.setter
    def delegate_manager(self, the_value):
        """delegate_manager setter sets Engine DelegateManage instance.
        """
        self.managers["delegate-manager"] = the_value

    @property
    def event_manager(self):
        """event_manager returns Engine EventManager instance.
        """
        return self.managers["event-manager"]

    @event_manager.setter
    def event_manager(self, the_value):
        """event_manager setter sets Engine EventManage instance.
        """
        self.managers["event-manager"] = the_value

    @property
    def font_manager(self):
        """font_manager returns Engine FontManager instance.
        """
        return self.managers["font-manager"]

    @font_manager.setter
    def font_manager(self, the_value):
        """font_manager setter sets Engine FontManage instance.
        """
        self.managers["font-manager"] = the_value

    @property
    def game_manager(self):
        """game_manager returns Engine GameManager instance.
        """
        return self.managers["game-manager"]

    @game_manager.setter
    def game_manager(self, the_value):
        """game_manager setter sets Engine GameManage instance.
        """
        self.managers["game-manager"] = the_value

    @property
    def resource_manager(self):
        """resource_manager returns Engine ResourceManager instance.
        """
        return self.managers["resource-manager"]

    @resource_manager.setter
    def resource_manager(self, the_value):
        """resource_manager setter sets Engine ResourceManage instance.
        """
        self.managers["resource-manager"] = the_value

    @property
    def scene_manager(self):
        """scene_manager returns Engine SceneManager instance.
        """
        return self.managers["scene-manager"]

    @scene_manager.setter
    def scene_manager(self, the_value):
        """scene_manager setter sets Engine SceneManage instance.
        """
        self.managers["scene-manager"] = the_value

    @property
    def sound_manager(self):
        """sound_manager returns Engine SoundManager instance.
        """
        return self.managers["sound-manager"]

    @sound_manager.setter
    def sound_manager(self, the_value):
        """sound_manager setter sets Engine SoundManage instance.
        """
        self.managers["sound-manager"] = the_value

    def add_scene(self, the_scene):
        """add_scene adds the given scene to the Engine SceneManager.

        Args:
            the_scene (Scene): Scene instance to be added to the Engine
                SceneManager.

        Returns:
            bool : True if scene was added properly to the Engine SceneManager
                or False is there was any error adding the scene.
        """
        Log.Engine(self.name).AddScene(the_scene.name).call()
        return self.scene_manager.add_scene(the_scene)

    def destroy_entity(self, the_entity):
        """destroy_entity removes the given entity from the engine.

        Args:
            the_entity (Entity): Entity instance to be removed from the Engine.

        Returns:
        bool : True if entity instance was properly removed from the Engine or
            False if there was any error removing it.
        """
        Log.Engine(self.name).DestroyEntity(the_entity.name).call()
        a_scene = the_entity.get_scene()
        a_scene.delete_entity(the_entity)
        the_entity.set_active(False)
        return True

    def on_after_update(self):
        """on_after_update calls all on_after_update methods for every manager.
        """
        for a_manager in self.managers:
            a_manager.on_after_update()

    def on_cleanup(self):
        """on_cleanup cleans up all graphical and none graphical resources.
        """
        Log.Engine(self.name).OnCleanUp().call()
        self.on_graphical_cleanup()

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of a tick frame.
        """
        Log.Engine(self.name).OnFrameEnd().call()
        for a_manager in self.managers:
            a_manager.on_frame_end()

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of a tick frame.
        """
        Log.Engine(self.name).OnFrameStart().call()
        for a_manager in self.managers:
            a_manager.on_frame_start()

    def on_graphical_cleanup(self):
        """on_graphical_cleanup cleans up all graphical resources.
        """
        Log.Engine(self.name).OnGraphicalCleanUp().call()

    def on_graphical_init(self):
        """on_graphical_init initialized all graphical resources.
        """
        Log.Engine(self.name).OnGraphicalInit().call()

    def on_init(self):
        """on_init initalizes all engine graphical and none graphical
        resources.
        """
        Log.Engine(self.name).OnInit().call()
        self.on_graphical_init()
        for a_manager in self.managers:
            a_manager.on_init()

    def on_run(self):
        """on_run proceeds to run the engine.
        """
        Log.Engine(self.name).OnRun().call()
        while self.active:
            self.on_frame_start()

            # process all graphical events.

            self.on_update()
            self.on_after_update()

            self.on_render()

            self.on_frame_end()

    def on_render(self):
        """on_render calls all on_render methods for every manager.
        """
        for a_manager in self.managers:
            a_manager.on_render()

    def on_start(self, the_scene):
        """on_start starts the engine. At this point all scenes and entities
        have been already registered to the engine.

        Args:
            the_scene (Scene): Initial scene instance to start the engine.
        """
        Log.Engine(self.name).OnStart().call()
        self.active = True
        for a_manager in self.managers:
            a_manager.on_start()
        # set the given scene as the active scene.
        self.scene_manager.set_active_scene(the_scene)

    def on_update(self):
        """on_update calls all on_update methods for every manager.
        """
        for a_manager in self.managers:
            a_manager.on_update()

    def run(self, the_scene):
        """run runs the engine and launches the give scene as the initial one.

        Args:
            the_scene (Scene): Initial scene instance to start the engine.
        """
        self.on_init()
        self.game_manager.create_assets()
        self.on_start(the_scene)
        self.on_run()
        self.on_cleanup()
