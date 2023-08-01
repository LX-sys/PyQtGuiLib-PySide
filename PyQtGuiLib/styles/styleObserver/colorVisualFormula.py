# -*- coding:utf-8 -*-
# @time:2023/8/19:54
# @author:LX
# @file:colorVisualFormula.py
# @software:PyCharm

from PyQtGuiLib.header import QColor

'''
    颜色 和 视觉
'''


# 通用颜色算法(不包含渐变)
class ColorAlgorithm:

    # 反转颜色 算法
    @staticmethod
    def colorReversal(color: QColor):
        return QColor(
            255 - color.red(),
            255 - color.green(),
            255 - color.blue()
        )

    # 颜色透明 算法
    @staticmethod
    def colorTranslucency(color: QColor):
        fc = QColor(*color.getRgb())
        fc.setAlpha(255 * 0.75)
        return fc

    # 原型 算法
    @staticmethod
    def origin(color: QColor):
        return QColor(*color.getRgb())

    # 高亮 算法
    @staticmethod
    def highlight(color: QColor):
        return QColor(color.hue(), 255, color.value())


# 前景色专用算法
class ForegroundVision(ColorAlgorithm):

    # 人眼容易感知的颜色 算法
    @staticmethod
    def humanVision(bg_color: QColor):
        gray_level = (0.299 * bg_color.red() + 0.587 * bg_color.green() + 0.144 * bg_color.blue()) / 255
        return QColor("black") if gray_level > 0.5 else QColor("white")
