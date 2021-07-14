"""_game_manager.py contains the GameManager base class, used to custom handle
any game application.
"""

from ._loggar import Log
from ._iobject import IObject


class GameManager(IObject):
    """GameManager class implements the base class for any custom game.
    """

    def __init__(self, the_name):
        """__init__ initializes the GameManager instance.

        Args:
            the_name (str): String with the GameManager name.
        """
        super().__init__(the_name)
        Log.GameManager(self.name).New().call()

    def create_assets(self):
        """create_assets creates all GameManager assets.
        """
        Log.GameManager(self.name).CreateAssets().call()

    def on_after_update(self):
        """on_after_update calls all on_after_update methods for every asset..
        """

    def on_cleanup(self):
        """on_cleanup cleans up all assets.
        """
        Log.GameManager(self.name).OnCleanUp().call()

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of a tick frame.
        """
        Log.GameManager(self.name).OnFrameEnd().call()

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of a tick frame.
        """
        Log.GameManager(self.name).OnFrameStart().call()

    def on_init(self):
        """on_init initalizes all GameManager assets and resources.
        """
        Log.GameManager(self.name).OnInit().call()

    def on_render(self):
        """on_render calls all on_render methods for every asset.
        """

    def on_update(self):
        """on_update calls all on_update methods for every asset.
        """
