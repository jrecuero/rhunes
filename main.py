"""main.py runs the main application.
"""

import sys

from engine import (Component, DebugManager, DelegateManager, Engine, Entity,
                    GameManager, Log, Scene, SceneManager)

if __name__ == "__main__":
    # a_engine = Engine("main", 800, 400, the_end_condition=lambda self: self.frames == 2)
    a_engine = Engine("main", 800, 400)
    Log.Main().Engine(a_engine.name).call()
    a_engine.debug_manager = DebugManager("mgr/debug")
    a_engine.delegate_manager = DelegateManager("mgr/delegate")
    a_engine.game_manager = GameManager("mgr/game")
    a_engine.scene_manager = SceneManager("mgr/scene")
    a_engine.scene_manager.add_scene(Scene("Title Scene"))
    a_engine.scene_manager.add_scene(Scene("Play Scene"))
    a_engine.scene_manager.add_scene(Scene("Game Over Scene"))
    a_engine.scene_manager.assign_active_scene()
    a_player = Entity("Player")
    a_player.add_component(Component("Body"))
    a_engine.scene_manager.active_scene.scene.add_entity(a_player)
    a_engine.run()
    # sys.exit(0)
