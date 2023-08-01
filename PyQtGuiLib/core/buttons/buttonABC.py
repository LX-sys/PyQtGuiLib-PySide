# -*- coding:utf-8 -*-
# @time:2023/7/3110:54
# @author:LX
# @file:buttonABC.py
# @software:PyCharm

from PyQtGuiLib.header import (
    QAbstractButton,
    QSize,
    QPainter,
    qt,
    QIcon,
    QFont
)

from typing import Union


class ButtonABC(QAbstractButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init()

    def init(self):
        font = QFont()
        font.setPointSize(13)
        self.setFont(font)

        self.setIconSize(QSize(24, 24))

    def sizeHint(self) -> QSize:
        return QSize(20, 20)
    
    def setIcon(self, icon:Union[str,QIcon], PySide6_QtGui_QIcon=None, PySide6_QtGui_QPixmap=None):
        if isinstance(icon,str):
            super().setIcon(QIcon(icon))
        else:
            super().setIcon(icon)

    def setText(self, text: str):
        super().setText(self.tr(text))

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHints(qt.Antialiasing | qt.SmoothPixmapTransform | qt.TextAntialiasing)

        self.paint(painter,e)

        painter.end()

    def paint(self,painter:QPainter,e):
        raise NotImplementedError("Subclasses must implement the paint() method")