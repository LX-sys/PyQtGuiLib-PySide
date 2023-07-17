from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide6":
    from PySide6.QtGui import *
    from PySide6.QtGui import QGuiApplication as DesktopWidget
elif PYQT_VERSIONS == "PySide2":
    from PySide2.QtGui import *
    from PySide2.QtGui import QGuiApplication as DesktopWidget
