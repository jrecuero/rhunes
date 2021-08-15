"""_entity.py contains the Entity base class, used for any entity in the game.
"""

from ._eobject import EObject
from ._loggar import Log


class Entity(EObject):
    """Entity class identifies an entity.
    """

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initializes the Entity instance.
        """
        super().__init__(the_name, the_engine, **kwargs)
        self.layer = kwargs.get("layer", "middle")
        self.parent = kwargs.get("parent", None)
        self.children = list()
        self.scene = kwargs.get("scene", None)
        self.transform = kwargs.get("transform", None)
        self.components = list()
        self.loaded_components = list()
        self.unloaded_components = list()
        self.die_on_collision = kwargs.get("die_on_collision", False)
        self.die_on_out_of_bounds = kwargs.get("die_on_out_of_bounds", False)

    def add_child(self, the_child):
        """add_child adds a new child entity.
        """
        Log.Entity(self.name).AddChild(the_child.name).call()
        self.children.append(the_child)
        the_child.parent = self
        the_child.layer = self.layer
        return True

    def add_component(self, the_component):
        """add_component adds a new component to the entity.
        """
        Log.Entity(self.name).AddComponent(the_component.name).call()
        for a_component in self.components:
            if a_component.klass == the_component.klass:
                Log.Entity(self.name).Error("component type {} already exists".format(the_component.klass))
                raise Exception("component type {} already exists".format(the_component.klass))
        the_component.entity = self
        the_component.engine = self.engine
        self.components.append(the_component)
        self.unloaded_components.append(the_component)
        return self

    def delete_child(self, the_child_id):
        """delete_child removes a child from the entity children list using
        child ID.
        """
        Log.Entity(self.name).DeleteChild(the_child_id).call()
        a_child = self.lookup_by_id(self.children, the_child_id)
        if a_child:
            self.remove_child(a_child)
            return True
        return False

    def delete_child_by_name(self, the_child_name):
        """delete_child_by_name removes a child from the entity children list
        using child name.
        """
        Log.Entity(self.name).DeleteChildByName(the_child_name).call()
        a_child = self.lookup_by_name(self.children, the_child_name)
        if a_child:
            self.remove_child(a_child)
            return True
        return False

    def get_component(self, the_component_klass):
        """get_component returns the given component by the class.
        """
        for a_component in self.components:
            if a_component.klass == the_component_klass:
                return a_component
        return None

    def get_delegate_for_component(self, the_component_class):
        """get_delefate_for_component returns the delegate for the given
        component class.
        """
        a_component = self.get_component(the_component_class)
        if not a_component:
            return None
        return a_component.delegate

    def load_unloaded_components(self):
        """load_unloaded_components proceeds to load any unloaded component.
        """
        # Log.Entity(self.name).LoadUnloadedComoponents().call()
        a_unloaded_components = list()
        for a_component in self.unloaded_components:
            if not a_component.active:
                a_unloaded_components.append(a_component)
                continue
            a_component.on_load()
            self.loaded_components.append(a_component)
        self.unloaded_components = a_unloaded_components
        return True

    def on_destroy(self):
        """on_destroy calls all methods to clean up the entity.
        """
        super().on_destroy()
        for a_component in self.components:
            a_component.on_destroy()
        self.components = list()
        self.loaded_components = list()
        self.unloaded_components = list()

    # def on_dump(self):
    #     """on_dump dumps entity to JSON format.
    #     """
    #     super().on_dump()

    def on_end(self):
        """on_end calls all on_end methods for components in the entity.
        """
        super().on_end()
        for a_component in [x for x in self.loaded_components if x.active]:
            a_component.on_end()

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of a tick frame.
        """
        super().on_frame_end()
        self.load_unloaded_components()
        for a_component in [x for x in self.loaded_components if x.active]:
            a_component.on_frame_start()

    # def on_frame_start(self):
    #     """on_frame_start calls all methods to run at the start of a tick
    #     frame.
    #     """
    #     super().on_frame_start()

    # def on_load(self):
    #     """on_load is called when entity is loaded by the scene.
    #     """
    #     super().on_load()

    def on_render(self):
        """on_render is called every time the entity is called to be rendered.
        """
        super().on_render()
        if not self.visible:
            return
        for a_component in [x for x in self.loaded_components if x.active]:
            a_component.on_render()

    def on_start(self):
        """on_start is called the first time the entity starts.
        """
        super().on_start()
        for a_component in [x for x in self.loaded_components if x.active]:
            a_component.on_start()

    def on_update(self):
        """on_update is called every time the entity is called to be updated.
        """
        super().on_update()
        for a_component in [x for x in self.loaded_components if x.active]:
            a_component.on_update()

    def remove_child(self, the_child):
        """remove_child removes child from all entity attributes.
        """
        Log.Entity(self.name).RemoveChild(the_child.name).call()
        self.children.remove(the_child)

    def remove_component(self, the_component):
        """remove_component removes the given component.
        """
        Log.Entity(self.name).RemoveComponent(the_component.name).call()
        if the_component in self.components:
            the_component.on_unload()
            self.components.remove(the_component)
            if the_component in self.loaded_components:
                self.loaded_components.remove(the_component)
            if the_component in self.unloaded_components:
                self.unloaded_components.remove(the_component)
            return True
        return False

    def remove_components(self):
        """remove_components remove all components.
        """
        Log.Entity(self.name).RemoveComponents().call()
        for a_component in self.components:
            a_component.on_unload()
            a_component.entity = None
            a_component.engine = None
        self.components = list()
        self.loaded_components = list()
        self.unloaded_components = list()
        return True
