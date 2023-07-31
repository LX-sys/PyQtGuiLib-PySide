# -*- coding:utf-8 -*-
# @time:2023/7/3113:50
# @author:LX
# @file:listWidgetABC.py
# @software:PyCharm
from PyQtGuiLib.header import (
    QApplication,
    sys,
    QWidget,
    QAbstractItemView,
    QListView,
    QAbstractItemModel,
    QStandardItemModel,
    QStandardItem,
    QColor,
    QProxyStyle,
    QPainter,
    QStyleOption,
    qt,
    QStyledItemDelegate,
    QStyleOptionViewItem,
QModelIndex,QRect
)


from PyQtGuiLib.styles.styleObserver import StyleObserver


class CustomListViewStyle(QProxyStyle):


    def drawPrimitive(self, element, option:QStyleOption, painter:QPainter, widget:QWidget=None):
        pass
        # painter.setPen(qt.NoPen)
        # painter.setBrush(StyleObserver.ThemeColor)
        # rect = widget.rect()
        # painter.drawRoundedRect(rect,5,5)
        # super().drawPrimitive(element, option, painter, widget)

    # def drawItemText(self, painter:QPainter, rect, flags: int, pal, enabled: bool, text: str, textRole) -> None:
    #     pass

    def drawComplexControl(self, control, option, painterQPainter, widget) -> None:
        pass

    def drawItemText(self, painter, rect, enabled: bool, text: str, textRole) -> None:
        pass

class CustomListViewDelegate(QStyledItemDelegate):
    def paint(self, painter:QPainter, option:QStyleOptionViewItem, index:QModelIndex):
        # print(index.data(0))
        painter.setPen(qt.NoPen)
        painter.setBrush(StyleObserver.ThemeColor)

        rect = QRect(*option.rect.getRect())  # type:QRect
        painter.drawRoundedRect(5,5,rect.width()-10,40,5,5)
        painter.setPen(QColor("#fff"))
        print(index.row())
        painter.drawText(rect,qt.AlignCenter,index.data(0))
        # 自定义绘制选中项的背景颜色
        # if option.state & QListView.State_Selected:
        #     painter.save()
        #     painter.fillRect(option.rect, QColor("#99ccff"))
        #     painter.restore()
        #
        #调用基类方法绘制文本和图标
        # super().paint(painter, option, index)



class ListWidgetABC(QListView):
    def __init__(self,*args):
        super().__init__(*args)

        # self.setStyle(CustomListViewStyle())
        self.setItemDelegate(CustomListViewDelegate())

        model = QStandardItemModel()

        self.setModel(model)


        # model.setRowCount(10)
        item = QStandardItem()
        item.setText("测试")
        # item.setBackground(Theme.Default)
        # item.setForeground(QColor("#fff"))

        model.appendRow(item)

class TestShow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)

        self.listv = ListWidgetABC(self)
        self.listv.setGeometry(20,20,200,400)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TestShow()
    win.show()

    sys.exit(app.exec())