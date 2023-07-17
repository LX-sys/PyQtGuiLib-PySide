from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide6":
    from PySide6.QtWidgets import *
elif PYQT_VERSIONS == "PySide2":
    from PySide2.QtWidgets import *
    # from PySide2.QtWidgets import QDesktopWidget as DesktopWidget