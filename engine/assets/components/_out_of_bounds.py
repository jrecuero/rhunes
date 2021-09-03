"""out_of_bounds.py components control if the entity is going
out of bounds for the engine screen.
"""

from ..._component import Component


class OutOfBounds(Component):
    """OutOfBounds class is the component controlling out of bounds events.
    """

    OUT_OF_BOUNDS_EVENT_NAME = "out-of-bounds-event"

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes OutOfBounds instance.
        bounce means the instance is declared to be out of bounds when any
        sides reach bounds.

        if bounds is False, the instance has to be completely out of bounds.
        """
        super().__init__(the_name, the_engine, **kwargs)
        self.bounce = kwargs.get("the_bounce", False)

    def on_load(self):
        """on_load is called all on_load methods.
        """
        super().on_load()
        self.delegates[self.OUT_OF_BOUNDS_EVENT_NAME] = self.engine.delegate_manager.create_delegate(self, self.OUT_OF_BOUNDS_EVENT_NAME)

    def on_update(self):
        """on_update calls all on_update methods.
        """
        super().on_update()
        a_width = self.engine.width
        a_height = self.engine.height
        a_rect = self.entity.transform.get_rect()
        if self.bounce:
            test_left = a_rect.x < 0
            test_right = (a_rect.x + a_rect.w) > a_width
            test_top = a_rect.y < 0
            test_down = (a_rect.y + a_rect.h) > a_height
        else:
            test_left = (a_rect.x + a_rect.w) < 0
            test_right = a_rect.x > a_width
            test_top = (a_rect.y + a_rect.h) < 0
            test_down = a_rect.y > a_height
        if test_left:
            self.engine.delegate_manager.trigger_delegate(self.delegates[self.OUT_OF_BOUNDS_EVENT_NAME].id, True, the_entity=self.entity, the_location="left")
        if test_right:
            self.engine.delegate_manager.trigger_delegate(self.delegates[self.OUT_OF_BOUNDS_EVENT_NAME].id, True, the_entity=self.entity, the_location="right")
        if test_top:
            self.engine.delegate_manager.trigger_delegate(self.delegates[self.OUT_OF_BOUNDS_EVENT_NAME].id, True, the_entity=self.entity, the_location="top")
        if test_down:
            self.engine.delegate_manager.trigger_delegate(self.delegates[self.OUT_OF_BOUNDS_EVENT_NAME].id, True, the_entity=self.entity, the_location="down")
