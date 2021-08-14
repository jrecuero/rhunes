"""_iobject contains the basic and generic object class most other classes
will derive.
"""

from ._ider import get_ider


class IObject:
    """IObject is the basic and generic object for any other class.
    """

    def __init__(self, the_name, **kwargs):
        """__init__ initializes the IObject instance.

        Args:
            the_name (str): IObject instance name.
        """
        self.id = get_ider()
        self.name = the_name
        self.loaded = kwargs.get("loaded", False)
        self.started = kwargs.get("started", False)
        self.active = kwargs.get("active", False)
        self.tag = kwargs.get("tag", None)
        self.dirty = kwargs.get("dirty", False)
        self.visible = kwargs.get("visible", True)

    @staticmethod
    def lookup_by_active(the_iter):
        """lookup_by_active returns a list of entries in the given iterable
        where all are active.
        """
        return [a_traverse for a_traverse in the_iter if a_traverse.active]

    @staticmethod
    def lookup_by_dirty(the_iter):
        """lookup_by_dirty returns a list of entries in the given iterable
        where all are dirty.
        """
        return [a_traverse for a_traverse in the_iter if a_traverse.dirty]

    @staticmethod
    def lookup_by_id(the_iter, the_id):
        """lookup_by_id returns an entry in the given iterable for the
        given id.
        """
        for a_traverse in the_iter:
            if a_traverse.id == the_id:
                return a_traverse
        return None

    @staticmethod
    def lookup_by_loaded(the_iter):
        """lookup_by_loaded returns a list of entries in the given iterable
        where all are loaded.
        """
        return [a_traverse for a_traverse in the_iter if a_traverse.loaded]

    @staticmethod
    def lookup_by_name(the_iter, the_name):
        """lookup_by_name returns an entry up in the given iteratble for the
        given name.
        """
        for a_traverse in the_iter:
            if a_traverse.name == the_name:
                return a_traverse
        return None

    @staticmethod
    def lookup_by_not_active(the_iter):
        """lookup_by_not_active returns a list of entries in the given iterable
        where all are not active.
        """
        return [a_traverse for a_traverse in the_iter if not a_traverse.active]

    @staticmethod
    def lookup_by_not_dirty(the_iter):
        """lookup_by_not_dirty returns a list of entries in the given iterable
        where all are not dirty.
        """
        return [a_traverse for a_traverse in the_iter if not a_traverse.dirty]

    @staticmethod
    def lookup_by_not_loaded(the_iter):
        """lookup_by_not_loaded returns a list of entries in the given iterable
        where all are not loaded.
        """
        return [a_traverse for a_traverse in the_iter if not a_traverse.loaded]

    @staticmethod
    def lookup_by_not_visible(the_iter):
        """lookup_by_not_visible returns a list of entries in the given iterable
        where all are not visible.
        """
        return [a_traverse for a_traverse in the_iter if not a_traverse.visible]

    @staticmethod
    def lookup_by_tag(the_iter, the_tag):
        """lookup_by_tag returns a list of entries in the given iterable for
        the given tag.
        """
        return [a_traverse for a_traverse in the_iter if a_traverse.tag == the_tag]

    @staticmethod
    def lookup_by_visible(the_iter):
        """lookup_by_visible returns a list of entries in the given iterable
        where all are visible.
        """
        return [a_traverse for a_traverse in the_iter if a_traverse.visible]
