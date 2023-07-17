# -*- coding:utf-8 -*-
# @time:2023/7/179:31
# @author:LX
# @file:test1.py
# @software:PyCharm
from PyQtGuiLib.header import (
    PYQT_VERSIONS,
    QApplication,
    sys,
    QWidget
)



class Test(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Test()
    win.show()

    if PYQT_VERSIONS in ["PyQt6","PySide6"]:
        sys.exit(app.exec())
    else:
        sys.exit(app.exec_())