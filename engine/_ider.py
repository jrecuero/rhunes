"""_ider.py generates unique identifications to be used by the
application.
"""


class Ider:
    """Ider class contains a unique identification generator.
    """

    def __init__(self):
        """__init__ initializes the Ider instance.
        """
        self._ider = 0

    def reset(self):
        """reset resets the identification to zero.
        """
        self._ider = 0

    def next(self):
        """next returns the next identification.
        """
        self._ider += 1
        return str(self._ider)


# _ider contains the Ider singleton.
_IDER = None


def get_ider():
    """get_ider returns the Ider singleton.

    Returns:
        Ider : Ider instance.
    """
    global _IDER
    if _IDER is None:
        _IDER = Ider()
    return _IDER

