# -*- coding:utf-8 -*-
# @time:2023/7/319:27
# @author:LX
# @file:standardButton.py
# @software:PyCharm
from PyQtGuiLib.header import (
    QApplication,
    sys,
    QPushButton,
    QAbstractButton,
    QPainter,
    QColor,
    QBrush,
    QRect,
    QSize,
    QPoint,
    QWidget,
    qt,
    QFont,
    QTextOption,
    QVBoxLayout,
    QSizePolicy,
    QFontMetrics,
    QPaintEvent,
    QComboBox,
    QGraphicsDropShadowEffect,
    QListWidget,
    QIcon,
    QLinearGradient
)

from PyQtGuiLib.core.buttons.buttonABC import ButtonABC

from PyQtGuiLib.header.utility import getTextSize, getDrawTextPos

from PyQtGuiLib.styles.styleObserver import StyleObserver, ControlTheme
from PyQtGuiLib.styles.styleObserver.controlTheme import UniversalTheme


# 具有文字图标的按钮
class TextButton(ButtonABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paint(self, painter: QPainter, e):
        if self.isDown():
            fc = StyleObserver.foregroundColor().getRgb()
            fc = QColor(*fc)
            fc.setAlpha(180)
            color = fc
        else:
            color = StyleObserver.foregroundColor()

        if not self.isEnabled():
            color = ControlTheme.Foreground.EnabledColor
        painter.setPen(color)

        painter.setFont(self.font())

        pos = getDrawTextPos(e, self.font(), self.text())

        x = self.width() // 2 - self.iconSize().width() // 2
        y = self.height() // 2 - self.iconSize().height() // 2
        if self.text():
            x = pos.x() - self.iconSize().width() - 10
            y = pos.y() - self.iconSize().height() + self.iconSize().height() // 4
        painter.drawPixmap(x, y, self.icon().pixmap(self.iconSize()))

        # print(pos)
        # painter.drawText(getDrawTextPos(e, font, self.text()), self.text())
        if self.text():
            painter.drawText(e.rect(), qt.AlignCenter, self.text())

    def drawCustomGraphStyle(self, painter: QPainter,e):
        raise NotImplementedError("Customize the graphic style")


class StandardButton(TextButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.setIconSize(QSize(50,50))
        self.setIcon(r"../../styles/styleObserver/EmojiTabSymbols_black.svg")

    # 绘制自定义风格(默认风格按钮风格)
    def drawCustomGraphStyle(self, painter: QPainter,e):
        painter.drawRoundedRect(e.rect(), 5, 5)

    def backgroundOption(self,painter: QPainter):
        if not self.isEnabled():
            bg = ControlTheme.Background.EnabledColor
            fc = qt.NoPen
        else:
            bg = StyleObserver.backgroundColor()
            fc = qt.NoPen

        painter.setPen(fc)
        painter.setBrush(bg)

    def drawForeground(self):
        pass

    def paint(self, painter: QPainter, e):
        self.backgroundOption(painter)
        self.drawCustomGraphStyle(painter,e)

        super().paint(painter,e)


class GradientButton(TextButton):

    def drawCustomGraphStyle(self, painter: QPainter, e):
        painter.drawRoundedRect(e.rect(),5,5)

    def paint(self, painter: QPainter, e):
        linearGrad = QLinearGradient(QPoint(0,0), QPoint(self.width(),self.height()))
        linearGrad.setColorAt(0, qt.black)
        linearGrad.setColorAt(1, qt.white)

        painter.setPen(qt.NoPen)
        painter.setBrush(linearGrad)

        self.drawCustomGraphStyle(painter,e)
        super().paint(painter,e)


class ShadowButton(StandardButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._offx = 0
        self._offy = 0
        self._blueradius = 15

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(self._offx,self._offy)
        self.shadow.setBlurRadius(self._blueradius)
        # self.shadow.setColor(StyleObserver.backgroundColor())
        self.shadow.setColor(ControlTheme.Background.Red)
        self.setGraphicsEffect(self.shadow)

    def hover(self,event):
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(ControlTheme.Background.Red)

    def leave(self,event):
        self.shadow.setBlurRadius(10)

    def press(self,e):
        pass

    def release(self,e):
        pass

    def paint(self, painter: QPainter, e):
        super().paint(painter, e)
        if self.isHover():
            pass
        else:
            r,g,b,a = StyleObserver.backgroundColor().getRgb()
            # print(r,g,b,a)
            value = int((255*0.299)+(g*0.587)+(b*0.114))
            # print(value)
            s_r = min(255, max(0, r + (0 - r)*(value-value)/(0-255)))
            s_g = min(255, max(0, g + (0 - g)*(value-value)/(0-255)))
            s_b = min(255, max(0, b + (0 - b)*(value-value)/(0-255)))
            # print(s_r,s_g,s_b)
            # self.shadow.setColor(QColor(s_r,s_g,s_b,255))
            self.shadow.setColor(
                            ControlTheme.Background.EnabledColor
                            if not self.isEnabled() else
                            StyleObserver.backgroundColor())
        self.update()


class TestShow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)

        # self.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.vlay = QVBoxLayout(self)
        self.vlay.setSpacing(10)
        self.combox = QComboBox()
        self.combox.addItems(UniversalTheme.allColorNames())
        self.combox.currentTextChanged.connect(self.changeTheme)

        self.btn = StandardButton()
        # self.btn.setEnabled(False)
        # self.btn.setText("Hello Wrold")
        self.btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.btn.setGeometry(100, 100, 140, 50)

        self.sbtn = ShadowButton()
        # self.sbtn.setEnabled(False)
        self.sbtn.setText("带阴影")
        self.sbtn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.gradbtn = GradientButton()
        self.gradbtn.setText("渐变效果")
        self.gradbtn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.vlay.addWidget(self.combox)
        # self.vlay.addWidget(self.btn)
        self.vlay.addWidget(self.sbtn)
        # self.vlay.addWidget(self.gradbtn)

    def changeTheme(self, s_color):
        StyleObserver.setThemeColor(UniversalTheme.getColor(s_color))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TestShow()
    win.show()

    sys.exit(app.exec())
