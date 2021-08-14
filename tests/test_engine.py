import sure
from engine import DelegateManager, Engine, GameManager, SceneManager


def test_engine():
    a_engine = Engine("test/engine", 640, 480)
    a_engine.should_not.be.none
    Engine.get().should.equal(a_engine)
    a_engine.name.should.equal("test/engine")
    a_engine.width.should.equal(640)
    a_engine.height.should.equal(480)
    a_engine.active.should.be.false
    a_engine.cursor_manager.should.be.none
    a_engine.delegate_manager.should.be.none
    a_engine.event_manager.should.be.none
    a_engine.font_manager.should.be.none
    a_engine.game_manager.should.be.none
    a_engine.resource_manager.should.be.none
    a_engine.scene_manager.should.be.none
    a_engine.sound_manager.should.be.none
    a_engine.frames.should.equal(0)
    a_engine.state.should.equal("created")
    Engine.delete()


def test_run():
    a_engine = Engine("test/engine", 800, 400, the_end_condition=lambda self: self.frames == 2)
    a_engine.delegate_manager = DelegateManager("delegate-manager")
    a_engine.game_manager = GameManager("game-manager")
    a_engine.scene_manager = SceneManager("scene-manager")
    a_engine.run(None)
    a_engine.state.should.equal("on-end")
    a_engine.delegate_manager.state.should.equal("on-end")
    a_engine.game_manager.state.should.equal("on-end")
    a_engine.scene_manager.state.should.equal("on-end")
    a_engine.frames.should.equal(2)
