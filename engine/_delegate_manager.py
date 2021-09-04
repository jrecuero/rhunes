"""_delegate_manager.py contains all logic delegate logic.
"""

from ._eobject import EObject
from ._iobject import IObject
from ._loggar import Log


class Delegate(IObject):
    """Delegate class.
    """

    def __init__(self, the_name, the_component_source, the_event_name):
        """__init__ initializes a Delegate instance.
        """
        super().__init__(the_name)
        Log.Delegate(self.name).New().call()
        self.component_source = the_component_source
        self.event_name = the_event_name


class Callback(IObject):
    """Callback class.
    """

    def __init__(self, the_name, the_component_to_register, the_entity, the_component, the_delegate, the_signature):
        """__init__ initializes a Callback instance.

        component_to_register: component where callback belongs
        entity: entity of the delegate component.
        component: delegate component.
        delegate: delegate where callback is registered.
        signature: callback signature.
        kwargs: parameters to be passed to the callback
        """
        super().__init__(the_name)
        self.callback_id = None
        self.component_to_register = the_component_to_register
        self.entity = the_entity
        self.component = the_component
        self.delegate = the_delegate
        self.signature = the_signature
        self.kwargs = {}


class DelegateManager(EObject):
    """DelegateManager class.
    """

    def __init__(self, the_name, the_engine=None):
        """__init__ initializes a DelegateManager instance.
        """
        super().__init__(the_name, the_engine)
        self.delegates = {}     # [delegate_id]delegate
        self.callbacks = {}     # [delegate_id]list(callback)
        self.to_be_called = []

    def create_delegate(self, the_component_source, the_event_name):
        """create_delegate creates and adds a new Delegate instance to the
        DelegateManager.
        """
        Log.DelegateManager(self.name).CreateDelegate(the_event_name).call()
        a_delegate = Delegate("{}/{}".format(self.name, the_event_name), the_component_source, the_event_name)
        self.delegates[a_delegate.id] = a_delegate
        return a_delegate

    def delete_delegate(self, the_delegate_id):
        """delete_delegate deletes the given delegate from the DelegateManager.
        """
        Log.DelegateManager(self.name).DeleteDelegate(the_delegate_id).call()
        a_delegate = self.delegates.get(the_delegate_id, None)
        if a_delegate is not None:
            del self.delegates[the_delegate_id]
        return a_delegate

    def deregister_callback_from_delegate(self, the_delegate_id, the_callback_id):
        """deregister_callback_from_delegate deregister the given callback
        from the delegate.
        """
        Log.DelegateManager(self.name).DeregisterCallback(the_delegate_id, the_callback_id).call()
        for index, a_callback in enumerate(self.delegates.get(the_delegate_id, [])):
            if a_callback.callback_id == the_callback_id:
                del self.callbacks[index]
                return True
        return False

    def on_init(self):
        """on_init initializes all DelegateManager resources.
        """
        super().on_init()
        return True

    # def on_start(self):
    #     """on_start initializes all DelegateManager resources.
    #     """

    def on_update(self):
        """on_update is called after all other on_update methods have been
        called for all entities, components and resources in the scene. It will
        execute all callbacks still pending.
        """
        super().on_update()
        for a_callback in self.to_be_called:
            a_callback.signature(**a_callback.kwargs)

    def register_callback_to_delegate(self, the_component_to_register, the_delegate, the_signature):
        """register_callback_to_delegate registers a new callback to the given
        delegate.
        """
        Log.DelegateManager(self.name).RegisterCallback(the_delegate.name).call()
        a_component = the_delegate.component_source
        a_callback_name = "{}/{}".format(the_component_to_register.name, a_component.name)
        a_callback = Callback(a_callback_name, the_component_to_register, a_component.entity, a_component, the_delegate, the_signature)
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
        Log.DelegateManager(self.name).TriggerDelegateFor(the_delegate_id).call()
        for a_callback in self.callbacks.get(the_delegate_id, []):
            # Check if the entity for the component in the callback belongs to
            # the active scene.
            if not self.get_scene_manager().is_active_scene(a_callback.component.entity.scene.id):
                continue
            if the_entities is not None and a_callback.component.entity not in the_entities:
                continue
            if the_now:
                a_callback.signature(**kwargs)
                return
            a_store_callback = Callback(a_callback.name,
                                        a_callback.component_to_register,
                                        a_callback.entity,
                                        a_callback.component,
                                        a_callback.delegate,
                                        a_callback.signature)
            a_store_callback.callback_id = a_callback.callback_id
            a_store_callback.kwargs = kwargs
            self.to_be_called.append(a_store_callback)
            return
