"""_iobject contains the basic and generic object class most other classes
will derive.
"""

from ._ider import get_ider


class IObject:
    """IObject is the basic and generic object for any other class.
    """

    def __init__(self, the_name):
        """__init__ initializes the IObject instance.

        Args:
            the_name (str): IObject instance name.
        """
        self.id = get_ider()
        self.name = the_name
        self.loaded = False
        self.started = False
        self.enabled = False
        self.active = False
        self.dirty = False
