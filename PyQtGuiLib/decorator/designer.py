# -*- coding:utf-8 -*-
# @time:2023/7/2014:24
# @author:LX
# @file:designer.py
# @software:PyCharm
from PyQtGuiLib.header import (
    QDrag,
    qt,
    QPainter,
    QPixmap,
    QMimeData
)
'''
    给 设计师 自定义组件设计的装饰器,
    使控件可以在设计师进行拖拽
'''


def libMouseEvent(func):
    def wrapper(self,event,*args,**kwargs):
        if self.pyqtguilib_isp:
            drag = QDrag(self)
            self.hide()

            t_pix = QPixmap(self.grab().size())
            t_pix.fill(qt.transparent)
            painter = QPainter(t_pix)
            painter.setOpacity(0.6)
            painter.drawPixmap(0, 0, self.grab())
            painter.end()
            drag.setPixmap(t_pix)

            mime_data = QMimeData()
            drag.setMimeData(mime_data)
            spot = event.pos()
            self.pyqtguilib_spot = spot
            drag.setHotSpot(spot)
            drag.exec_(qt.MoveAction)
        func(self,event)
    return wrapper


def libPressEvent(func):
    def wrapper(self,event,*args,**kwargs):
        if event.button() == qt.LeftButton:
            self.pyqtguilib_isp = True
        func(self,event)
    return wrapper