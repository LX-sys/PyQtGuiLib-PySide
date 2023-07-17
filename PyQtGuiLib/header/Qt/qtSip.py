from PyQtGuiLib.header.versions import PYQT_VERSIONS

if PYQT_VERSIONS == "PySide2":
    try:
        from PySide2.sip import delete
    except:
        pass

if PYQT_VERSIONS == "PySide6":
    try:
        from PySide6.sip import delete
    except:
        pass