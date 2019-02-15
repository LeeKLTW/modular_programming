# encoding: utf-8
#relative import
try:
    from ..editor import slider
    print(slider.debug)
    del slider
except ValueError as e:
    print('ValueError')
    print(e)
except ImportError:
    print('Relative import failed.')

#absolute import
try:
    from program.gui.widgetseditor import slider
    print(slider.debug)
    del slider
except ModuleNotFoundError:
    print('Absolute import failed.')

