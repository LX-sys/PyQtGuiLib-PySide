# -*- coding:utf-8 -*-
# @time:2023/7/3111:13
# @author:LX
# @file:styleObserver.py
# @software:PyCharm
from PyQtGuiLib.header import (
    QColor
)

from PyQtGuiLib.styles.styleObserver.controlTheme import ControlTheme


class StyleObserver:
    '''
        样式观察者
    '''
    _ThemeBGColor = ControlTheme.Background.Default
    _ThemeFGColor = ControlTheme.Foreground.White

    @staticmethod
    def setThemeColor(bg_color:QColor,fg_color=None):
        StyleObserver._ThemeBGColor = bg_color
        if fg_color:
            StyleObserver._ThemeFGColor = fg_color

    @staticmethod
    def backgroundColor():
        return StyleObserver._ThemeBGColor

    @staticmethod
    def foregroundColor():
        return StyleObserver._ThemeFGColor