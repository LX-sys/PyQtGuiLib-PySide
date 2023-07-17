from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide2":
    from PySide2.QtNetwork import *
elif PYQT_VERSIONS == "PySide6":
    from PySide6.QtNetwork import *