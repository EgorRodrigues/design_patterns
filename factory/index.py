from factory.core import CreateCore


core = CreateCore()

try:
    core.start()
    core.stop()
except TypeError:
    print('[index] Uncaught error!')
    print(TypeError)
