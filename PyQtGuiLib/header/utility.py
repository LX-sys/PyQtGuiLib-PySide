import platform
import math

from PyQtGuiLib.header import (
    PYQT_VERSIONS,
    sys,
    DesktopWidget,
    QApplication,
    QPoint,
    QSize,
    QFontMetrics,
    QFont,
    QWidget,
)

'''
QListWidget 在Pyqt5页面刷新的方式 update(),其他版本可以用repaint()来达到一样的效果
QListWidget 的update(item)需要传递一个参数
'''

is_win_sys = True if platform.system() in ["win32","Windows"] else False

is_mac_sys = True if platform.system() == "Darwin" else False


'''
    These several screen-related methods can only be called in the window,
    otherwise an error will be reported
'''


IS_QtIt = PYQT_VERSIONS in ["PySide6","PySide2"]


def getDesktopCount() -> int:
    return len(DesktopWidget.screens())


# Gets the size of a single desktop
def getDesktopSize() -> QSize:
    return DesktopWidget.primaryScreen().size()


# Total size of all screens
def getDesktopAllSize() -> QSize:
    size = desktopSize()
    return QSize(size.width()*desktopCount(),size.height())


# The desktop is in the middle
def getDesktopCenter(parent) -> QPoint:
    center = DesktopWidget.primaryScreen().availableGeometry().center()
    return QPoint(center.x()-parent.width()//2,center.y()-parent.height()//2)


def getTextSize(font:QFont,text:str) -> QSize:
    fs = QFontMetrics(font)
    if IS_QtIt:
        return QSize(fs.horizontalAdvance(text)+1, fs.height()+1) # +1 是为了补偿丢失的像素
    else:
        return QSize(0,0)


# 获取绘制文字位置
def getDrawTextPos(e,font:QFont,text:str,offsetX=0,offsetY=0)->QPoint:
    if IS_QtIt:
        e_widht = e.rect().size().width()
        e_height = e.rect().size().height()
        fs = QFontMetrics(font)
        size = QSize(fs.horizontalAdvance(text), fs.height())
        x = e_widht // 2 - size.width() // 2 + offsetX
        y = e_height // 2 - size.height() // 2 + fs.ascent() + offsetY
        return QPoint(x,y)
    else:
        return QPoint(0, 0)



def rgbToHsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx,mn = max(r, g, b),min(r, g, b)
    df = mx-mn
    h = 0
    if mx == mn:
        h = 0
    elif mx == r:h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:h = (60 * ((r-g)/df) + 240) % 360

    s = 0 if mx ==0 else df/mx

    v = mx
    return h, s, v


def loadUic(ui_path:str) -> QWidget:
    if PYQT_VERSIONS in ["PySide2","PySide6"]:
        from PyQtGuiLib.header import QFile,QUiLoader
        uif = QFile(ui_path)
        loader = QUiLoader()
        ui = loader.load(uif)
        uif.close()
        return ui

def hsvToRgb(h, s, v):
    h,s,v = float(h),float(s),float(v)

    h_60 = h / 60.0
    h_60f = math.floor(h_60)
    hi = int(h_60f) % 6
    f = h_60 - h_60f

    p,q,t = v * (1 - s),v * (1 - f * s),v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0

    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b
