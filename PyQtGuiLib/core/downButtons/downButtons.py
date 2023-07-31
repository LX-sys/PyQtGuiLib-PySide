# -*- coding:utf-8 -*-
# @time:2023/7/2016:35
# @author:LX
# @file:downButtons.py
# @software:PyCharm
from PyQtGuiLib.header import (
    QApplication,
    QWidget,
    qt,
    QPushButton,
    sys,
    QPainter,
    QPoint,
    QColor,
    QProxyStyle,
    QStyleOptionButton,
    QStyle,
    QRect,
    QPen,
    Signal,
    QThread,
    QPropertyAnimation
)

class ColorTh(QThread):
    numbered = Signal(int)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def run(self) -> None:
        n = 0
        while n != 96:
            print(n)
            self.numbered.emit(n)
            self.msleep(100)
            n+=1


class MyStyleDelegate(QProxyStyle):
    def __init__(self):
        super().__init__()
        self.cth = ColorTh()
        self.w = 0
        self.cth.numbered.connect(self.setw)

    def setw(self,w):
        self.w = w

    def drawControl(self, element, option, painter:QPainter, widget:QPushButton=None):
        painter.setPen(qt.NoPen)
        if element == QStyle.CE_PushButtonBevel:
            painter.setBrush(QColor(85, 170, 255))
            painter.drawRoundedRect(widget.rect(),2,2)
            if self.w != 0:
                option.text = "{}%".format(self.w)
            interior = QRect(2,2,self.w,widget.height()-2)
            painter.setBrush(QColor(57, 114, 171,200))
            painter.drawRoundedRect(interior, 2, 2)
            widget.update()
        elif element == QStyle.CE_PushButtonLabel:
            if option.state & QStyle.State_MouseOver:
                # 添加鼠标悬停状态
                painter.setBrush(qt.NoBrush)
                # painter.eraseRect(widget.rect())
                painter.setPen(QColor(30, 61, 91))
                r = widget.rect()
                r.adjust(1,1,-1,-1)
                painter.drawRoundedRect(r, 2, 2)
            if widget and widget.isDown():
                if not self.cth.isRunning():
                    self.cth.start()
            super().drawControl(element, option, painter, widget)
        else:
            # 使用默认样式绘制其他部分
            super().drawControl(element, option, painter, widget)


class MyStyleDelegate2(QProxyStyle):
    def __init__(self):
        super().__init__()
        self.cth = ColorTh()
        self.w = 0
        self.cth.numbered.connect(self.setw)

    def setw(self,w):
        self.w = w

    def drawControl(self, element, option, painter:QPainter, widget:QPushButton=None):
        painter.setPen(qt.NoPen)
        if element == QStyle.CE_PushButtonBevel:
            painter.setBrush(QColor(85, 170, 255))
            # painter.drawRoundedRect(widget.rect(),2,2)
            h = widget.height()
            h2 = widget.height()//2
            interior = QRect(widget.width()//2-h2,0,h,h)
            painter.drawRoundedRect(interior,h2,h2)

        elif element == QStyle.CE_PushButtonLabel:
            if option.state & QStyle.State_MouseOver:
                # 添加鼠标悬停状态
                pass
            if widget and widget.isDown():
               pass
            super().drawControl(element, option, painter, widget)
        else:
            # 使用默认样式绘制其他部分
            super().drawControl(element, option, painter, widget)


class DownButton(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(160,60)

        self.setStyle(MyStyleDelegate2())
        self.setText("你好")



class Test(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(800,600)

        self.btn = DownButton(self)
        self.btn.move(100,100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Test()
    win.show()

    sys.exit(app.exec())
