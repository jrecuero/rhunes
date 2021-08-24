"""main.py runs the main application.
"""

import sys
import pygame

from engine import (Component, DebugManager, DelegateManager, Engine, Entity,
                    GameManager, Log, Scene, SceneManager, Transform)
from engine.assets.components import Box, KeyController


# class Box(Component):

#     def on_render(self):
#         pygame.draw.rect(self.engine.screen, (0, 0, 255), [50, 50, 150, 150], False)


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
    a_player.transform = Transform(the_position=pygame.Vector2(50, 50), the_dim=pygame.Vector2(100, 100))
    # a_player.add_component(Box("Body", the_color='blue', the_rect=pygame.Rect(50, 50, 100, 100)))
    a_player.add_component(KeyController("ArrowController"))
    a_player.add_component(Box("Body", the_color='blue'))
    a_engine.scene_manager.active_scene.scene.add_entity(a_player)
    a_engine.run()
    # sys.exit(0)
