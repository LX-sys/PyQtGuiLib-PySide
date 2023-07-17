import importlib

# The current version of python qt used
PYQT_VERSIONS = None

VERSIONS = ["PySide6","PySide2"]

for module in VERSIONS:
    try:
        importlib.import_module(module)
        PYQT_VERSIONS = module
        break
    except:
        pass

if PYQT_VERSIONS is None:
    raise ModuleNotFoundError("Module not found,support:PySide6,PySide2")
