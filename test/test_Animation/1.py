# -*- coding:utf-8 -*-
# @time:2023/3/249:19
# @author:LX
# @file:1.py
# @software:PyCharm
import sys

from PyQt5.QtCore import QSize, QPoint,QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQtGuiLib.animation import Animation


class Test(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 600)

        self.btn = QPushButton("按钮", self)
        self.btn.move(50, 50)
        self.btn.resize(100, 60)
        self.btn.setStyleSheet('''
                QPushButton{
                    background-color:rgb(50,100,200);
                    color:rgb(255,0,0);
                }
                ''')

        self.start_btn = QPushButton("开始动画", self)
        self.start_btn.setGeometry(500, 50, 100, 60)
        self.start_btn_2 = QPushButton("修改动画", self)
        self.start_btn_2.setGeometry(500, 120, 100, 60)

        # 实例化动画类
        self.ani = Animation()
        # 设置动画时长
        self.ani.setDuration(2000)  # 2秒

        # 再添加一个移动的动画
        s = [(253, 298), (255, 298), (259, 300), (263, 303), (268, 309),
             (274, 317), (281, 326), (286, 336), (292, 346), (298, 352), (299, 354), (303, 359),
             (307, 365), (309, 368), (310, 369), (311, 371), (314, 371), (317, 371), (324, 371), (332, 369),
             (343, 366), (355, 360), (372, 352), (392, 344), (415, 335), (435, 326), (454, 319), (475, 310),
             (490, 303), (505, 295), (515,288), (525, 283), None]

        self.v = self.ani.createAniNumbers(253,298)

        # self.ani.addValuesAni({
        #     "propertyName":"value",
        #     "sv":self.v,
        #     "ev":
        # })


        # self.ani.start()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Test()
    win.show()
    sys.exit(app.exec())
