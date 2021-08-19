import sure
from engine import (Component, DelegateManager, Engine, Entity, GameManager,
                    Scene, SceneManager)


def test_engine():
    a_engine = Engine("test/engine", 640, 480)
    a_engine.should_not.be.none
    Engine.get().should.equal(a_engine)
    a_engine.name.should.equal("test/engine")
    a_engine.width.should.equal(640)
    a_engine.height.should.equal(480)
    a_engine.active.should.be.true
    a_engine.running.should.be.false
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
    # setup
    a_engine = Engine("test/engine", 800, 400, the_end_condition=lambda self: self.frames == 2)
    a_engine.delegate_manager = DelegateManager("delegate-manager")
    a_engine.game_manager = GameManager("game-manager")
    a_engine.scene_manager = SceneManager("scene-manager")
    a_engine.scene_manager.add_scene(Scene("test-scene"))
    a_engine.scene_manager.assign_active_scene()
    a_player = Entity("player")
    a_component = Component("Body")
    a_player.add_component(a_component)
    a_engine.scene_manager.active_scene.scene.add_entity(a_player)
    a_engine.run()
    # validations
    a_engine.state.should.equal("on-end")
    a_engine.delegate_manager.state.should.equal("on-end")
    a_engine.game_manager.state.should.equal("on-end")
    a_engine.scene_manager.state.should.equal("on-end")
    a_engine.scene_manager.active_scene.scene.state.should.equal("on-end")
    a_player.state.should.equal("on-end")
    a_component.state.should.equal("on-end")
    a_engine.frames.should.equal(2)
    Engine.delete()
