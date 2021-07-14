"""_scene.py contais the Scene base class, used for any scene in the game.
"""

from ._loggar import Log
from ._eobject import EObject


class Scene(EObject):
    """Scene class identifies a scene.
    """

    def __init__(self, the_engine, the_name, **kwargs):
        """__init__ initialized the Scene instance.
        """
        super().__init__(the_engine, the_name)
        Log.Scene(self.name).New().call()
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
        the_entity.scene = self
        for a_entity_child in the_entity.children:
            self.add_entity(a_entity_child)
        return True

    def check_collisions(self):
        """check_collisions checks collisions between all entities in the
        scene.
        """
        pass

    def get_entity(self, the_entity_id):
        """get_entity retrieves an entity by the given entity ID.
        """
        for a_entity in self.entities:
            if a_entity.id == the_entity_id:
                return a_entity
        return None

    def get_entity_by_name(self, the_entity_name):
        """get_entity_by_name retrieves an entity by the given entity name.
        """
        for a_entity in self.entities:
            if a_entity.name == the_entity_name:
                return a_entity
        return None

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

    def on_destroy(self):
        """on_destroy calls all methods to clean up the scene.
        """
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

    def on_dump(self):
        """on_dump dumps all scene entites in JSON format.
        """
        Log.Scene(self.name).OnDump().call()

    def on_frame_end(self):
        """on_frame_end calls all methods to run at the end of tick frame.
        """
        for a_entity in self.entities:
            a_entity.on_frame_end()

    def on_frame_start(self):
        """on_frame_start calls all methods to run at the start of tick frame.
        """
        self.load_unloaded_entities()
        for a_entity in self.entities:
            a_entity.on_frame_start

    def remove_entity(self, the_entity):
        """remove_entity removes the given entity from the scene.
        """
        Log.Scene(self.name).RemoveEntity(the_entity.name).call()
        a_entity = self.get_entity(the_entity)
        if not a_entity:
            return False
        self.to_delete_entities.append(a_entity)
        # TODO: Remove collider from the collision collection, so there is not
        # more checks between this collider and other other one.

        # TODO: Trigger destroy delegate

        for a_entity_child in the_entity.children:
            self.remove_entity(a_entity_child)
        return True

