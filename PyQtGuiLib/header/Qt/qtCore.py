from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide2":
    from PySide2.QtCore import *
    from PySide2.QtCore import Property as pyqtProperty
elif PYQT_VERSIONS == "PySide6":
    from PySide6.QtCore import *
    from PySide6.QtCore import Property as pyqtProperty
