"""_collider2d file contains the component that implements a basic collider.
"""

import pygame
from ..._component import Component


class Collider2D(Component):
    """Collider2D class implements a 2D collider component.
    """

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes Collider2d instance.
        """
        super().__init__(the_name, the_engine, **kwargs)
        self.collider = True

    def get_collider_rect(self):
        """get_collider_rect returns the rectangle used to check collisions.
        """
        return self.entity.transform.get_rect()