from factory.core import CreateCore


class CreateMock:
    def __init__(self):
        ...

    @staticmethod
    def start():
        ...

    @staticmethod
    def stop():
        ...


class TestCore:
    def test_should_the_class_start_and_stop(self):
        assert hasattr(CreateCore, 'start') and callable(CreateCore().start)
        assert hasattr(CreateCore, 'stop') and callable(CreateCore().stop)

    def test_should_return_phrase(self):
        core = CreateCore(database_connection=CreateMock(), webserver=CreateMock())
        assert isinstance(core, CreateCore)
        assert hasattr(core, 'start') and callable(core.start)
        assert hasattr(core, 'stop') and callable(core.stop)
