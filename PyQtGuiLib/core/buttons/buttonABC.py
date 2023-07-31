# -*- coding:utf-8 -*-
# @time:2023/7/3110:54
# @author:LX
# @file:buttonABC.py
# @software:PyCharm

from PyQtGuiLib.header import (
    QAbstractButton,
    QSize,
    QPainter,
    qt
)

class ButtonABC(QAbstractButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sizeHint(self) -> QSize:
        return QSize(20, 20)

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