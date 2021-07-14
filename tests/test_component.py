import sure
from engine import Engine, Component

def test_component():
    a_engine = Engine()
    a_component = Component(a_engine, "test/component")
    a_component.should_not.be.none
    a_component.entity.should.be.none
    a_component.delegate.should.be.none
    a_component.callbacks.should.be.empty
    a_component.remove_on_destroy.should.be.true
    a_component.cache.should.be.empty
    Engine.delete()
