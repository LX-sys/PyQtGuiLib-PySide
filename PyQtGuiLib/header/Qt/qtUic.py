from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide6":
    from PySide6.QtCore import QFile
    from PySide6.QtUiTools import QUiLoader
elif PYQT_VERSIONS == "PySide2":
    from PySide2.QtCore import QFile
    from PySide2.QtUiTools import QUiLoader

