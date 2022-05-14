from factory.core import CreateCore


class TestCore:
    def test_should_the_class_start_and_stop(self):
        assert hasattr(CreateCore, 'start') and callable(CreateCore().start)
        assert hasattr(CreateCore, 'stop') and callable(CreateCore().stop)

