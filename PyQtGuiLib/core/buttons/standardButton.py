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
    QIcon
)

from PyQtGuiLib.core.buttons.buttonABC import ButtonABC

from PyQtGuiLib.header.utility import getTextSize, getDrawTextPos

from PyQtGuiLib.styles.styleObserver import StyleObserver, ControlTheme


class StandardButton(ButtonABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.setIconSize(QSize(50,50))
        self.setIcon(r"D:\pySave\PyQtGuiLib-PySide\PyQtGuiLib\styles\styleObserver\EmojiTabSymbols_black.svg")

    def paint(self, painter: QPainter, e):
        rect = e.rect()  # type:QRect

        if not self.isEnabled():
            bg = ControlTheme.Background.EnabledColor
            fc = StyleObserver.foregroundColor()
        else:
            bg = StyleObserver.backgroundColor()
            fc = StyleObserver.foregroundColor()

        painter.setPen(fc)
        painter.setBrush(bg)
        painter.drawRoundedRect(rect, 5, 5)

        if self.isDown():
            fc = StyleObserver.foregroundColor().getRgb()
            fc = QColor(*fc)
            fc.setAlpha(180)
            color = fc
        else:
            color = StyleObserver.foregroundColor()
            if StyleObserver.backgroundColor().name() == ControlTheme.Background.White.name():
                color = ControlTheme.Foreground.Black

        if not self.isEnabled():
            color = ControlTheme.Foreground.EnabledColor
        painter.setPen(color)

        font = QFont()
        font.setPointSize(13)
        painter.setFont(font)

        pos = getDrawTextPos(e, font, self.text())

        x = self.width() // 2 - self.iconSize().width() // 2
        y = self.height() // 2 - self.iconSize().height() // 2
        if self.text():
            x = pos.x() - self.iconSize().width()-10
            y = pos.y()-self.iconSize().height()+self.iconSize().height()//4
        painter.drawPixmap(x,y,self.icon().pixmap(self.iconSize()))

        # print(pos)
        # painter.drawText(getDrawTextPos(e, font, self.text()), self.text())
        if self.text():
            painter.drawText(e.rect(), qt.AlignCenter, self.text())


class ShadowButton(StandardButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(StyleObserver.backgroundColor())
        self.setGraphicsEffect(self.shadow)

    def paint(self, painter: QPainter, e):
        super().paint(painter, e)
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
        self.combox.addItems(["默认", "红色", "绿色", "白色", "黑色"])
        self.combox.currentTextChanged.connect(self.changeTheme)

        self.btn = StandardButton(self)
        # self.btn.setEnabled(False)
        # self.btn.setText("Hello Wrold")
        self.btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.btn.setGeometry(100, 100, 140, 50)

        self.sbtn = ShadowButton(self)
        # self.sbtn.setEnabled(False)
        self.sbtn.setText("带阴影")
        self.sbtn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.vlay.addWidget(self.combox)
        self.vlay.addWidget(self.btn)
        self.vlay.addWidget(self.sbtn)

    def changeTheme(self, text):
        if text == "默认":
            StyleObserver.setThemeColor(ControlTheme.Background.Default)
        elif text == "红色":
            StyleObserver.setThemeColor(ControlTheme.Background.Red)
        elif text == "绿色":
            StyleObserver.setThemeColor(ControlTheme.Background.Green)
        elif text == "白色":
            StyleObserver.setThemeColor(ControlTheme.Background.White)
        elif text == "黑色":
            StyleObserver.setThemeColor(ControlTheme.Background.Black)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TestShow()
    win.show()

    sys.exit(app.exec())
