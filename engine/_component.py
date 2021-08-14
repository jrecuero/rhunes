"""_component.py contains the Component base class, used for any component
in the game.
"""

from ._loggar import Log
from ._eobject import EObject
from ._delegate_manager import Callback


class Component(EObject):
    """Component class identifies a component.
    """

    def __init__(self, the_engine, the_name, **kwargs):
        """__init__ initializes the Component instance.
        """
        super().__init__(the_engine, the_name, **kwargs)
        Log.Component(self.name).New().call()
        self.entity = kwargs.get("entity", None)
        self.delegate = kwargs.get("delegate", None)
        self.callbacks = []
        self.remove_on_destroy = kwargs.get("remove_on_destroy", True)

    def add_delegate_to_callback(self, the_delegate, the_entity, the_component, the_signature):
        """add_delegate_to_callback adds a new delegate that component should callback.
        """
        Log.Component(self.name).AddDelegateToCallback(the_delegate, the_entity, the_component).call()
        a_callback = Callback("component-callback", self, the_entity, the_component, the_delegate, the_signature)
        self.callbacks.append(a_callback)
        return self

    def default_add_delegate_to_callback(self):
        """default_add_delegate_to_callback adds default delegate to callback
        for the component.
        """
        pass
    
    @property
    def klass(self):
        """klass returns component class name.
        """
        return type(self).__name__

    def on_active(self):
        """on_active is called every time the component is set to active.
        """
        Log.Component(self.name).OnActive().call()
        self.active = True

    def on_collision_callback(self, **kwargs):
        """on_collision_callback is the component default callback when
        on_collision delegate is triggered.
        """
        return True

    def on_destroy(self):
        """on_destroy calls all methods to clean up the component.
        """
        Log.Component(self.name).OnDestroy().call()
        for a_callback in self.callbacks:
            self.get_delegate_manager().deregister_from_delegate(a_callback.callback)
            a_callback.delegate = None
        if self.delegate:
            self.get_delegate_manager().delete_delegate(self.delegate)
        self.callbacks = []
        self.delegate = None
        self.loaded = False
        self.started = False

    def on_destroy_callback(self, **kwargs):
        """on_destroy_callback is the component default callback when on_destroy
        delegate is triggered.
        """
        return True

    def on_dump(self):
        """on_dump dumps component to JSON format.
        """
        pass

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of a tick frame.
        """
        pass

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of a tick
        frame.
        """
        return self.started

    def on_load(self):
        """on_load is called when component is loaded by the entity.
        """
        Log.Component(self.name).OnLoad().call()
        return self.loaded

    def on_load_callback(self, **kwargs):
        """on_load_callback is the component default callback when on_load
        delegate is triggered.
        """
        return True

    def on_render(self):
        """on_render is called every time the component is rendered.
        """
        pass

    def on_start(self):
        """on_start is called the first time the component starts.
        """
        Log.Component(self.name).OnStart().call()
        if self.started:
            return
        for a_callback in self.callbacks:
            a_delegate = a_callback.delegate
            if a_delegate is None:
                a_entity = a_callback.entity if a_callback.entity else self.entity
                a_component = a_entity.get_component(a_callback.component)
                if a_component and a_component.delegate:
                    a_callback.delegate = a_delegate
            else:
                a_callback_id, a_ok = self.get_delegate_manager().register_callback_to_delegate(self, a_delegate, a_callback.signature)
                if a_ok:
                    a_callback.callback_id = a_callback_id
        self.started = True

    def on_unload(self):
        """on_unload is called when component is unloaded by the entity. If
        this method is overwritten in any derived class, Component method has
        to be called because it is in charge to deregister all delegates and
        callbacks.
        """
        Log.Component(self.name).OnUnload().call()
        for a_callback in self.callbacks:
            self.get_delegate_manager().deregister_from_delegate(a_callback.callback_id)
            # Callback is created based on delegates for those belonging to
            # the DelegateManager. Those are unchanged and delegate does not
            # to be cleared.
            if a_callback.delegate and a_callback.delegate.id not in self.get_delegate_manager().defaults_id:
                a_callback.delegate = None
        if self.delegate:
            self.get_delegate_manager().delete_delegate(self.delegate)
        self.loaded = False
        self.started = False

    def on_update(self):
        """on_updaate is called every time component is updated.
        """
        pass

    def remove_delegate_to_callback(self, the_delegate, the_entity, the_component):
        """remove_delegate_to_callback removes a callback for the given
        delegate in delegate handler. Callback is being removed from the
        component too.
        """
        pass
