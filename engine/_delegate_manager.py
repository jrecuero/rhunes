"""_delegate_manager.py contains all logic delegate logic.
"""

from ._loggar import Log
from ._iobject import IObject
from ._eobject import EObject


class Delegate(IObject):
    """Delegate class.
    """

    def __init__(self, the_name, the_source, the_event_name):
        """__init__ initializes a Delegate instance.
        """
        super().__init__(the_name)
        Log.Delegate(self.name).New().call()
        self.source = the_source
        self.event_name = the_event_name


class Callback(IObject):
    """Callback class.
    """

    def __init__(self, the_name, the_source, the_entity, the_component, the_delegate, the_signature):
        """__init__ initializes a Callback instance.
        """
        super().__init__(the_name)
        self.callback_id = None
        self.source = the_source
        self.entity = the_entity
        self.component = the_component
        self.delegate = the_delegate
        self.signature = the_signature
        self.kwargs = {}


class DelegateManager(EObject):
    """DelegateManager class.
    """
    ON_COLLISION_EVENT_NAME = "on-collision-event"
    ON_DESTROY_EVENT_NAME = "on-destroy-event"
    ON_LOAD_EVENT_NAME = "on-load_event"

    def __init__(self, the_engine, the_name):
        """__init__ initializes a DelegateManager instance.
        """
        super().__init__(the_engine, the_name)
        self.delegates = {}     # [delegate_id]delegate
        self.callbacks = {}     # [delegate_id]list(callback)
        self.defaults = {}
        self.to_be_called = []

    def create_delegate(self, the_source, the_event_name):
        """create_delegate creates and adds a new Delegate instance to the
        DelegateManager.
        """
        Log.DelegateManager(self.name).CreateDelegate(the_event_name).call()
        a_delegate = Delegate("{}/{}".format(self.name, the_event_name), the_source, the_event_name)
        self.delegates[a_delegate.id] = a_delegate
        return a_delegate

    @property
    def defaults_id(self):
        """defaults_id property returns a list with all DelegateManager defaults
        delegates id's.
        """
        return [x.id for x in self.defaults.values()]

    def delete_delegate(self, the_delegate_id):
        """delete_delegate deletes the given delegate from the DelegateManager.
        """
        Log.DelegateManager(self.name).DeleteDelegate(the_delegate_id).call()
        a_delegate = self.delegates.get(the_delegate_id, None)
        if a_delegate is not None:
            del self.delegates[the_delegate_id]
        return a_delegate

    def deregister_callback_from_delegate(self, the_delegate_id, the_callback_id):
        """deregister_callback_from_delegate unregisters the given callback
        from the delegate.
        """
        Log.DelegateManager(self.name).DeregisterCallback(the_delegate_id, the_callback_id).call()
        for index, a_callback in enumerate(self.delegates.get(the_delegate_id, [])):
            if a_callback.callback_id == the_callback_id:
                del self.callbacks[index]
                return True
        return False

    @property
    def on_collision_delegate(self):
        """on_collision_delegate returns the default on_collision event
        delegate.
        """
        return self.defaults.get(self.ON_COLLISION_EVENT_NAME, None)

    @property
    def on_destroy_delegate(self):
        """on_destroy_delegate returns the default on_destroy event
        delegate.
        """
        return self.defaults.get(self.ON_DESTROY_EVENT_NAME, None)

    def on_init(self):
        """on_init initializes all DelegateManager resources.
        """
        Log.DelegateManager(self.name).OnInit().call()
        self.defaults[self.ON_COLLISION_EVENT_NAME] = self.create_delegate(self, self.ON_COLLISION_EVENT_NAME)
        self.defaults[self.ON_DESTROY_EVENT_NAME] = self.create_delegate(self, self.ON_DESTROY_EVENT_NAME)
        self.defaults[self.ON_LOAD_EVENT_NAME] = self.create_delegate(self, self.ON_LOAD_EVENT_NAME)
        return True

    @property
    def on_load_delegate(self):
        """on_load_delegate returns the default on_load event delegate.
        """
        return self.defaults.get(self.ON_LOAD_EVENT_NAME, None)

    def on_start(self):
        """on_start initializes all DelegateManager resources.
        """
        Log.DelegateManager(self.name).OnStart().call()

    def on_update(self):
        """on_update is called after all other on_update methods have been
        called for all entities, components and resources in the scene. It will
        execute all callbacks still pending.
        """
        for a_callback in self.to_be_called:
            a_callback.signature(**a_callback.kwargs)

    def register_callback_to_delegate(self, the_source, the_delegate, the_signature):
        """register_callback_to_delegate registers a new callback to the given
        delegate.
        """
        Log.DelegateManager(self.name).RegisterCallback(the_delegate.name).call()
        a_callback = Callback("", the_source, None, None, the_delegate, the_signature)
        a_callback.callback_id = a_callback.id
        self.callbacks.setdefault(the_delegate.id, []).append(a_callback)
        return a_callback.callback_id, True

    def trigger_delegate(self, the_delegate_id, the_now, **kwargs):
        """trigger_delegate calls all callbacks registered to the given
        delegate.

        the_now boolean parameter identifies if the callbacks should run now
        or after all updates have finished.
        """
        self.trigger_delegate_for(the_delegate_id, None, the_now, **kwargs)

    def trigger_delegate_for(self, the_delegate_id, the_entities, the_now, **kwargs):
        """trigger_delegate_for calls all callbacks registered to the given
        delegate if callback entity is in the lis of entities given.
        """
        for a_callback in self.callbacks.get(the_delegate_id, []):
            # Check if the entity for the component in the callback belongs to
            # the active scene.
            if not get_scene_manager().is_active_scene(a_callback.component.entity.scene.id):
                continue
            if a_callback.component.entity not in the_entities:
                continue
            if the_now:
                a_callback.signature(**kwargs)
                return
            a_store_callback = Callback(a_callback.name,
                                        a_callback.source,
                                        a_callback.entity,
                                        a_callback.component,
                                        a_callback.delegate,
                                        a_callback.signature)
            a_store_callback.callback_id = a_callback.callback_id
            a_store_callback.kwargs = kwargs
            self.to_be_called.append(a_store_callback)
            return

