# encoding: utf-8
print(__name__)
try:
    from . import config

    print(config.debug)
    del config
except ImportError:
    print('Relative import failed.')

try:
    import config

    print(config.debug)
except ModuleNotFoundError:
    print('Absolute import failed.')
