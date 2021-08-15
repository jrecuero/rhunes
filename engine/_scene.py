"""_scene.py contais the Scene base class, used for any scene in the game.
"""

from ._eobject import EObject
from ._loggar import Log


class Scene(EObject):
    """Scene class identifies a scene.
    """
    LAYERS = ["background", "middle", "top"]

    def __init__(self, the_name, the_engine=None, **kwargs):
        """__init__ initialized the Scene instance.
        """
        super().__init__(the_name, the_engine)
        self.entities = list()
        self.to_delete_entities = list()
        self.loaded_entities = list()
        self.unloaded_entities = list()
        self.layers = dict()
        self.scene_code = None
        self.tag = kwargs.get("tag", None)
        self.collision_mode = kwargs.get("collision_mode", "collision-mode:circle")
        self.collision_check = kwargs.get("collision_check", True)
        self.collision_collection = list()

    def add_entity(self, the_entity):
        """add_entity adds a new entity to the scene. If the entity has
        children entities, all children are being added at this time in a
        recursive way.
        """
        Log.Scene(self.name).AddEntity(the_entity.name).call()
        self.entities.append(the_entity)
        self.unloaded_entities.append(the_entity)
        the_entity.engine = self.engine
        the_entity.scene = self
        for a_entity_child in the_entity.children:
            self.add_entity(a_entity_child)
        return True

    def check_collisions(self):
        """check_collisions checks collisions between all entities in the
        scene.
        """

    def load_unloaded_entities(self):
        """load_unloaded_entities proceeds to load any unloaded entity.
        """
        a_unloaded_entities = list()
        for a_entity in self.unloaded_entities:
            if not a_entity.active:
                a_unloaded_entities.append(a_entity)
                continue
            a_entity.on_load()
            self.loaded_entities.append(a_entity)
            layer = a_entity.layer
            self.layers[layer].append(a_entity)
            for a_component in a_entity.components:
                if not a_component.active:
                    continue
                # TODO: check component collision collider

            # TODO: trigger load delegate

        self.unloaded_entities = a_unloaded_entities

    def on_active(self):
        """on_active calls all loaded entities on_active methods.
        """
        super().on_active()
        for a_entity in self.loaded_entities:
            a_entity.on_active()

    def on_after_update(self):
        """on_after_update executes after all on_update calls have been
        executed and before on_render.
        """
        super().on_after_update()
        for a_entity in self.to_delete_entities:
            self.entities.remove(a_entity)
            if a_entity in self.loaded_entities:
                self.loaded_entities.remove(a_entity)
            if a_entity in self.unloaded_entities:
                self.unloaded_entities.remove(a_entity)
            # TODO: remove entity form self.layers
            a_entity.on_unload()
            a_entity.on_destroy()
        self.to_delete_entities = list()

    def on_destroy(self):
        """on_destroy calls all methods to clean up the scene.
        """
        super().on_destroy()
        Log.Scene(self.name).OnDestroy().call()
        self.loaded = False
        for a_entity in self.entities:
            a_entity.on_destroy()
        self.entities = list()
        self.loaded_entities = list()
        self.unloaded_entities = list()
        self.to_delete_entities = list()
        self.collision_collection = list()
        self.layers = dict()

    # def on_dump(self):
    #     """on_dump dumps all scene entites in JSON format.
    #     """
    #     super().on_dump()

    def on_end(self):
        """on_end calls all on_end methods for entities in the scene.
        """
        super().on_end()
        for a_entity in self.loaded_entities:
            a_entity.on_end()

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of tick frame.
        """
        super().on_frame_end()
        for a_entity in self.loaded_entities:
            a_entity.on_frame_end()

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of tick frame.
        """
        super().on_frame_start()
        self.load_unloaded_entities()
        for a_entity in self.entities:
            a_entity.on_frame_start()

    def on_init(self):
        """on_init initalizes all scene resources.
        resources.
        """
        for a_layer in Scene.LAYERS:
            self.layers[a_layer] = list()

    def on_load(self):
        """on_load is called when scene is loaded by the engine.
        """
        super().on_load()
        self.load_unloaded_entities()

    def on_render(self):
        """on_render calls all loaded entities on_render methods. It call
        entities using layers, calling from backgroud to top layer.
        """
        super().on_render()
        for _, a_entities_in_layer in self.layers.items():
            for a_entity in a_entities_in_layer:
                a_entity.on_render()

    def on_start(self):
        """on_start calls all loaded entities on_start methods.
        """
        super().on_start()
        for a_entity in self.loaded_entities:
            a_entity.on_start()

    def on_swap_back(self):
        """on_swap_back is called when scene is swap back.
        """
        super().on_swap_back()
        self.load_unloaded_entities()

    def on_swap_from(self):
        """on_swap_from is called when scene is swap from, but it is not
        unloaded.
        """
        super().on_swap_from()
        for a_entity in self.loaded_entities:
            a_entity.on_unload()
        self.loaded_entities = list()
        self.unloaded_entities = list(self.entities)
        self.collision_collection = list()
        self.to_delete_entities = list()
        self.layers = dict()

    def on_unload(self):
        """on_unload is called when scene is unloaded from the scene manager.
        """
        super().on_unload()
        self.loaded = False
        for a_entity in self.loaded_entities:
            a_entity.on_unload()
        self.entities = list()
        self.loaded_entities = list()
        self.unloaded_entities = list()
        self.collision_collection = list()
        self.to_delete_entities = list()
        self.layers = list()

    def on_update(self):
        """on_update calls all loaded entities on_update methods.
        """
        super().on_update()
        for a_entity in self.loaded_entities:
            a_entity.on_update()

    def remove_entity(self, the_entity):
        """remove_entity removes the given entity from the scene.
        """
        Log.Scene(self.name).RemoveEntity(the_entity.name).call()
        a_entity = self.lookup_by_id(self.entities, the_entity.id)
        if not a_entity:
            return False
        self.to_delete_entities.append(a_entity)
        # TODO: Remove collider from the collision collection, so there is not
        # more checks between this collider and other other one.

        # TODO: Trigger destroy delegate

        for a_entity_child in the_entity.children:
            self.remove_entity(a_entity_child)

        a_entity.scene = None
        a_entity.engine = None
        return True
