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
    QThread
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
        # painter.setRenderHints(qt.Antialiasing | qt.SmoothPixmapTransform | qt.TextAntialiasing)
        if element == QStyle.CE_PushButtonBevel:
            painter.setPen(qt.NoPen)
            painter.setBrush(QColor(85, 170, 255))
            painter.drawRoundedRect(widget.rect(),2,2)
            # interior = widget.rect() # type:QRect
            # interior.adjust(2,2,-2,-2)
            interior = QRect(2,2,self.w,26)
            painter.setBrush(QColor(57, 114, 171,200))
            painter.drawRoundedRect(interior, 2, 2)
            widget.update()

            # self.cth.start()

        elif element == QStyle.CE_PushButtonLabel:
            # 自定义按钮文本的样式
            # option = QStyleOptionButton(option)

            if option.state & QStyle.State_MouseOver:
                # 添加鼠标悬停状态
                pass

            if widget and widget.isDown():
                if not self.cth.isRunning():
                    self.cth.start()
            #     painter.eraseRect(widget.rect())
            #     h = widget.height()
            #     painter.setBrush(QColor(250, 0, 0))
            #     rect = QRect(widget.width()//2-h//2,0,h,h)
            #     painter.drawRoundedRect(rect, 20, 20)

            super().drawControl(element, option, painter, widget)
        else:
            # 使用默认样式绘制其他部分
            super().drawControl(element, option, painter, widget)


class DownButton(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(100,30)

        self.setStyle(MyStyleDelegate())
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
