# -*- coding:utf-8 -*-
# @time:2023/7/3111:13
# @author:LX
# @file:styleObserver.py
# @software:PyCharm
from PyQtGuiLib.header import (
    QColor
)

from PyQtGuiLib.styles.styleObserver.controlTheme import ControlTheme
from PyQtGuiLib.styles.styleObserver.colorVisualFormula import ColorAlgorithm,ForegroundVision

from typing import Callable


class StyleObserver:
    '''
        样式观察者
    '''
    _ThemeBGColor = ControlTheme.Background.Default
    # _ThemeFColor = ControlTheme.Foreground.Default

    _ColorForegroundFun = ForegroundVision.humanVision
    _ColorBackgroundFun = ForegroundVision.origin

    @staticmethod
    def colorFAlgorithm(algorithm:Callable = None):
        '''通过改函数,可以修改前景色的计算 算法,默认算法返回 黑/白 两色'''
        StyleObserver._ColorForegroundFun = algorithm if algorithm else ForegroundVision.humanVision

    @staticmethod
    def colorBGAlgorithm(algorithm:Callable = None):
        '''
            通过改函数,可以修改背景色的计算 算法,默认算法返回 原型
        '''
        StyleObserver._ColorBackgroundFun = algorithm if algorithm else ColorAlgorithm.origin

    @staticmethod
    def setThemeColor(bg_color:QColor):
        StyleObserver._ThemeBGColor = StyleObserver._ColorBackgroundFun(bg_color)

    @staticmethod
    def backgroundColor():
        return StyleObserver._ThemeBGColor

    @staticmethod
    def foregroundColor():
        return StyleObserver._ColorForegroundFun(StyleObserver._ThemeBGColor)
