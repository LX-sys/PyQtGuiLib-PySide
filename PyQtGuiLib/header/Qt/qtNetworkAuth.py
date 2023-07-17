from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide2":
    from PySide2.QtNetworkAuth import *
elif PYQT_VERSIONS == "PySide6":
    from PySide6.QtNetworkAuth import *