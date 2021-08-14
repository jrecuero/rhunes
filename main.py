"""main.py runs the main application.
"""

from engine import DelegateManager, Engine, GameManager, Log, SceneManager

if __name__ == "__main__":
    a_engine = Engine("main", 800, 400, the_end_condition=lambda self: self.frames == 2)
    Log.Main().Engine(a_engine.name).call()
    a_engine.delegate_manager = DelegateManager("delegate-manager")
    a_engine.game_manager = GameManager("game-manager")
    a_engine.scene_manager = SceneManager("scene-manager")
    a_engine.run(None)
