"""main.py runs the main application.
"""

import sys
import pygame
from pygame.constants import K_RIGHT

from engine import (Component, DebugManager, DelegateManager, Engine, Entity,
                    GameManager, Log, Scene, SceneManager, Transform)
from engine.assets.components import Box, Collider2D, KeyController, MoveTo, SceneHandler, OutOfBounds


# class Box(Component):

#     def on_render(self):
#         pygame.draw.rect(self.engine.screen, (0, 0, 255), [50, 50, 150, 150], False)

def move_to_keyboard_callback(self):
    def _move_to_keyboard_callback(the_key):
        a_table = {
            pygame.K_UP: pygame.Vector2(0, -2), 
            pygame.K_DOWN: pygame.Vector2(0, 2), 
            pygame.K_LEFT: pygame.Vector2(-2, 0), 
            pygame.K_RIGHT: pygame.Vector2(2, 0),
        }
        self.speed = a_table[the_key]
    return _move_to_keyboard_callback


def move_to_out_of_bounds_callback(self):
    def _move_to_out_of_bounds_callback(the_entity, the_location):
        self.speed *= -1
        pass
    return _move_to_out_of_bounds_callback

def move_to_on_collision_callback(self):
    def _move_to_on_collision_callback(the_one_entity, the_other_entity):
        print("collision callback between {} and {}".format(the_one_entity.name, the_other_entity.name))
    return _move_to_on_collision_callback

if __name__ == "__main__":
    # a_engine = Engine("main", 800, 400, the_end_condition=lambda self: self.frames == 2)
    a_engine = Engine("main", 800, 400)
    Log.Main().Engine(a_engine.name).call()
    # a_engine.debug_manager = DebugManager("mgr/debug")
    a_engine.delegate_manager = DelegateManager("mgr/delegate")
    a_engine.game_manager = GameManager("mgr/game")
    a_engine.scene_manager = SceneManager("mgr/scene")
    a_engine.scene_manager.add_scene(Scene("Title Scene"))
    a_engine.scene_manager.add_scene(Scene("Play Scene"))
    a_engine.scene_manager.add_scene(Scene("Game Over Scene"))
    a_engine.scene_manager.assign_active_scene()
    a_player = a_engine.new_entity(Entity("Player"))
    a_player.transform = Transform(the_position=pygame.Vector2(50, 50), the_dim=pygame.Vector2(10, 10))
    # a_player.add_component(Box("Body", the_color='blue', the_rect=pygame.Rect(50, 50, 100, 100)))
    a_player.add_component(KeyController("ArrowController"))
    a_player.add_component(Box("Player/Body", the_color='blue'))
    a_player.add_component(OutOfBounds("Player/OutOfBounds", the_bounce=True))
    a_player.add_component(Collider2D("Player/Collider"))
    a_behavior = {
        "component:KeyController": move_to_keyboard_callback,
        "component:OutOfBounds": move_to_out_of_bounds_callback,
        "scene:{}:on-collision-event".format(Scene.SCENE_HANDLER_ENTITY_NAME): move_to_on_collision_callback,
        # "KeyController": lambda self : lambda the_key : print(self.speed.x, self.speed.y, the_key),
            # pygame.K_UP: pygame.Vector2(0, -2), 
            # pygame.K_DOWN: pygame.Vector2(0, 2), 
            # pygame.K_LEFT: pygame.Vector2(-2, 0), 
            # pygame.K_RIGHT: pygame.Vector2(2, 0),
        # },
    }
    a_player.add_component(MoveTo("Player/Move", the_speed = pygame.Vector2(2, 0), the_behavior=a_behavior))
    a_rock = a_engine.new_entity(Entity("Rock"))
    a_rock.transform = Transform(the_position=pygame.Vector2(200, 50), the_dim=pygame.Vector2(10, 10))
    a_rock.add_component(Box("Rock/Body", the_color="red"))
    a_rock.add_component(Collider2D("Rock/Collider"))
    a_scene_handler = a_engine.new_entity(Entity(Scene.SCENE_HANDLER_ENTITY_NAME))
    a_scene_handler.add_component(SceneHandler(Scene.SCENE_HANDLER_COMPONENT_NAME))
    a_engine.scene_manager.active_scene.scene.add_entity(a_scene_handler)
    a_engine.scene_manager.active_scene.scene.add_entity(a_player)
    a_engine.scene_manager.active_scene.scene.add_entity(a_rock)
    a_engine.run()
    # sys.exit(0)
