"""_eobject extends IObject for any object making use of the Engine.
"""

from ._iobject import IObject
from ._loggar import Log


class EObject(IObject):
    """EObject extends IObject for any object using the Engine.
    """

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes an EObject instance.
        """
        super().__init__(the_name, **kwargs)
        Log.__getattr__(type(self).__name__)(self.name).New().call()
        self.engine = the_engine
        self.state = "created"
        self.cache = {}

    def get_cache(self, the_key):
        """get_cache retrieves instance data cache for the given key.
        """
        return self.cache.get(the_key, None)

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

    def set_cache(self, the_key, the_value):
        """set_cache sets a new cache entry for the given key and value.
        """
        self.cache[the_key] = the_value

    def on_active(self):
        """on_active calls all on_active methods.
        """
        self.active = True
        self.state = "on-active"
        Log.__getattr__(type(self).__name__)(self.name).OnActive(self.state).call()

    def on_after_update(self):
        """on_after_update calls all on_after_update methods.
        """
        self.state = "on-after-update"
        # Log.__getattr__(type(self).__name__)(self.name).OnAfterUpdate(self.state).call()

    def on_create(self):
        """on_create calls all on_create methods.
        """
        self.state = "on-create"
        Log.__getattr__(type(self).__name__)(self.name).OnCreate(self.state).call()

    def on_cleanup(self):
        """on_cleanup calls all on_cleanup methods.
        """
        self.state = "on-cleanup"
        Log.__getattr__(type(self).__name__)(self.name).OnCleanUp(self.state).call()

    def on_destroy(self):
        """on_destroy calls all on_destroy methods
        """
        self.state = "on-destroy"
        Log.__getattr__(type(self).__name__)(self.name).OnDestroy(self.state).call()

    def on_dump(self):
        """on_dump dumps all scene entites in JSON format.
        """
        self.state = "on-dump"
        Log.__getattr__(type(self).__name__)(self.name).OnDump(self.state).call()

    def on_end(self):
        """on_end ends instanve.
        """
        self.state = "on-end"
        Log.__getattr__(type(self).__name__)(self.name).OnEnd(self.state).call()

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of a tick frame.
        """
        self.state = "on-frame-end"
        # Log.__getattr__(type(self).__name__)(self.name).OnFrameEnd(self.state).call()

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of a tick frame.
        """
        self.state = "on-frame-start"
        # Log.__getattr__(type(self).__name__)(self.name).OnFrameStart(self.state).call()

    def on_graphical_cleanup(self):
        """on_graphical_cleanup cleans up all graphical resources.
        """
        self.state = "on-graphical-cleanup"
        Log.__getattr__(type(self).__name__)(self.name).OnGraphicalCleanUp(self.state).call()

    def on_graphical_init(self):
        """on_graphical_init initialized all graphical resources.
        """
        self.state = "on-graphical-init"
        Log.__getattr__(type(self).__name__)(self.name).OnGraphicalInit(self.state).call()

    def on_init(self):
        """on_init initalizes all engine graphical and none graphical
        resources.
        """
        self.state = "on-init"
        Log.__getattr__(type(self).__name__)(self.name).OnInit(self.state).call()

    def on_load(self):
        """on_load is called all on_load methods.
        """
        self.loaded = True
        self.state = "on-load"
        Log.__getattr__(type(self).__name__)(self.name).OnLoad(self.state).call()

    def on_run(self):
        """on_run proceeds to run the engine.
        """
        self.state = "on-run"
        Log.__getattr__(type(self).__name__)(self.name).OnRun(self.state).call()

    def on_render(self):
        """on_render calls all on_render methods.
        """
        self.state = "on-render"
        # Log.__getattr__(type(self).__name__)(self.name).OnRender(self.state).call()

    def on_start(self):
        """on_start calls start methods.
        """
        self.state = "on-start"
        Log.__getattr__(type(self).__name__)(self.name).OnStart(self.state).call()

    def on_swap_back(self):
        """on_swap_back calls all on_swap_back methods.
        """
        self.state = "on-swap-back"
        Log.__getattr__(type(self).__name__)(self.name).OnSwapBack(self.state).call()

    def on_swap_from(self):
        """on_swap_from calls all on_swap_from methods.
        """
        self.state = "on-swap-from"
        Log.__getattr__(type(self).__name__)(self.name).OnSwapFrom(self.state).call()

    def on_unload(self):
        """on_unload is called all on_unload methods.
        """
        self.state = "on-unload"
        Log.__getattr__(type(self).__name__)(self.name).OnUnlooad(self.state).call()

    def on_update(self):
        """on_update calls all on_update methods.
        """
        self.state = "on-update"
        # Log.__getattr__(type(self).__name__)(self.name).OnUpdate(self.state).call()
