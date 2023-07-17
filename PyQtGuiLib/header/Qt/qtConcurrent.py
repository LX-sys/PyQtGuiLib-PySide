from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide2":
    from PySide2.QtConcurrent import *
elif PYQT_VERSIONS == "PySide6":
    from PySide6.QtConcurrent import *