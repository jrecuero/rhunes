"""_game_manager.py contains the GameManager base class, used to custom handle
any game application.
"""

from ._eobject import EObject
from ._loggar import Log


class GameManager(EObject):
    """GameManager class implements the base class for any custom game.
    """

    def __init__(self, the_name, the_engine=None):
        """__init__ initializes the GameManager instance.

        Args:
            the_name (str): String with the GameManager name.
        """
        super().__init__(the_name, the_engine)

    # def on_after_update(self):
    #     """on_after_update calls all on_after_update methods for every asset..
    #     """

    # def on_cleanup(self):
    #     """on_cleanup cleans up all assets.
    #     """

    # def on_create(self):
    #     """on_create creates all GameManager assets.
    #     """

    # def on_frame_end(self):
    #     """on_frame_end calls all methods to run at the end of a tick frame.
    #     """

    # def on_frame_start(self):
    #     """on_frame_start calls all methods to run at the start of a tick frame.
    #     """

    # def on_init(self):
    #     """on_init initalizes all GameManager assets and resources.
    #     """

    # def on_render(self):
    #     """on_render calls all on_render methods for every asset.
    #     """

    # def on_start(self):
    #     """on_render calls all on_start methods for every asset.
    #     """

    # def on_update(self):
    #     """on_update calls all on_update methods for every asset.
    #     """
