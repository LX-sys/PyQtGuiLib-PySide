# -*- coding:utf-8 -*-
# @time:2023/7/3115:51
# @author:LX
# @file:controlTheme.py
# @software:PyCharm

'''
    控件颜色
'''
from PyQtGuiLib.header import QColor


class BackgroundTheme:
    Default = QColor("#80A0E8")
    Red = QColor("red")
    Green = QColor("green")
    White = QColor("#fff")
    Black = QColor("#000")

    # -- 控件被禁用时的颜色
    EnabledColor = QColor("#cccccc")


class ForegroundTheme:
    White = QColor("#fff")
    Black = QColor("#000")

    EnabledColor = QColor("#787878")


class ControlTheme:
    Background = BackgroundTheme
    Foreground = ForegroundTheme
