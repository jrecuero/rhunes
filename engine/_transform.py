"""_transform.py contains static geometric information for any
entity in the game.
"""

from pygame import Rect
from pygame.math import Vector2


class Transform:
    """Transform class provides, position, rotation, scale and
    dimension.
    """

    def __init__(self, **kwargs):
        """__init__ initializes Transform instance.
        """
        self.position = kwargs.get("the_position", Vector2(0, 0))
        self.rotation = kwargs.get("the_rotation", Vector2(0, 0))
        self.scale = kwargs.get("the_scale", Vector2(1, 1))
        self.dim = kwargs.get("the_dim", Vector2(0, 0))

    def get_rect(self):
        """get_rect returns a rectangle for the position and dimensions.
        """
        return Rect(self.position.x, self.position.y, self.dim.x * self.scale.x, self.dim.y * self.scale.y)