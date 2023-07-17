from PyQtGuiLib.header import (
    QWidget,
    QPainter,
    QPaintEvent,
    QPolygonF,
    QFont,
    QColor,
    QPointF,
    QBrush,
    getTextSize,
    QPainterPath,
    QRect,
    QPen,
    qt
)


class BubbleWidget(QWidget):

    # 方向
    Top = "top"
    Down = "Down"
    Left = "Left"
    Right = "Right"

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(100,60)

        # 箭头高度(三角形)
        self._arrows_h = 16

        # 文字
        self._text = ""
        self._font_size = 15
        self._radius = 10
        self._margin = 0

        self._bg_color = QColor(100, 130, 255, 200)

        # 追踪的控件
        self.trackWidget = None #type:QWidget

        self.__direction = BubbleWidget.Down

        #
        self.setText("气泡窗口")

    def setArrows(self,size:int):
        self._arrows_h = size

    def arrows(self) -> int:
        return self._arrows_h

    def setFontSize(self,size:int):
        self._font_size = size

    def fontSize(self) -> int:
        return self._font_size

    def setBgColor(self,color:QColor):
        self._bg_color = color

    def bgColor(self) -> QColor:
        return self._bg_color

    def setRadius(self,r:int):
        self._radius = r

    def radius(self) -> int:
        return self._radius
    
    def setMargin(self,m:int):
        self._margin = m
    
    def margin(self)->int:
        return self._margin
    
    # ----------------

    # 设置文字
    def setText(self,text:str):
        self._text = text
        self.textExtend()

    def text(self) -> str:
        return self._text

    # 文字扩展
    def textExtend(self):
        f = QFont()
        f.setPointSize(self.fontSize())
        # 文字大小
        fs = getTextSize(f, self.text())
        fw = fs.width()
        fh = fs.height()

        if self.__direction in [BubbleWidget.Top,BubbleWidget.Down]:
            self.resize(fw + 30, self.height())
        else:
            self.resize(fw + 30+self.arrows(), self.height())

        if fh >= self.height():
            self.resize(self.width(),self.height()+40)

        self.setTrack(self.trackWidget)

    # 设置气泡箭头方向
    def setDirection(self,d):
        self.__direction = d

    def direction(self) -> str:
        return self.__direction

    # 控件追踪
    def setTrack(self, widget: QWidget):
        if widget is None:
            return

        self.trackWidget = widget

        x,y = widget.x(),widget.y()
        w,h = widget.width(),widget.height()
        cx = widget.x()+w//2-self.width()//2  # x轴中心
        cy = widget.y()+h//2-self.height()//2

        if self.__direction == BubbleWidget.Top:
            self.move(cx,y+h)
        elif self.__direction == BubbleWidget.Left:
            self.move(x+w,cy)
        elif self.__direction == BubbleWidget.Right:
            self.move(x-self.width(),cy)
        else:
            self.move(cx,y-self.height())

    # 绘制气泡
    def drawBubble(self,painter:QPainter,ppath:QPainterPath):
        # 矩形高度
        rect_h = self.height() - self.arrows()
        rect_w = self.width() - self.arrows()
        # 画三角
        line_w = self.arrows()  # 线宽
        lien_x = self.width() // 2 - line_w // 2  # 线的位置-水平
        line_y = self.height()//2  # 线的位置-垂直

        # 绘制文字
        f = QFont()
        f.setPointSize(self.fontSize())
        painter.setFont(f)
        # 文字大小
        fs = getTextSize(f, self.text())
        fw = fs.width()
        fh = fs.height()

        self.textExtend()

        # 画刷
        bru = QBrush(self.bgColor())
        painter.setBrush(bru)

        # 画笔
        painter.setPen(qt.NoPen)

        if self.__direction == BubbleWidget.Top:
            # 画三角
            ploys = [QPointF(lien_x,self.arrows(),),QPointF(lien_x+line_w//2,1),
                     QPointF(lien_x+line_w,self.arrows())
                     ]
            # 画矩形
            rect = QRect(self.margin(),self.arrows()+self.margin(),self.width()-self.margin()*2,rect_h-self.margin()*2)
            # 文字位置
            x = self.width() // 2 - fw // 2
            y = rect_h//2 + fh//2+self.arrows()
        elif self.__direction == BubbleWidget.Left:
            # 画三角
            ploys = [QPointF(1,line_y),QPointF(self.arrows(),line_y-line_w//2),
                     QPointF(self.arrows(),line_y+line_w//2)
            ]
            rect = QRect(self.arrows()+self.margin(),self.margin(),rect_w-self.margin()*2,self.height()-self.margin()*2)
            # 文字位置
            x = self.width()//2-fw//2 + self.arrows()//2
            y = self.height()//2 + fh//2
        elif self.__direction == BubbleWidget.Right:
            # 画三角
            ploys =[QPointF(rect_w,line_y-line_w//2),QPointF(rect_w+self.arrows(),line_y),
                    QPointF(rect_w,line_y+line_w//2)
            ]
            rect = QRect(self.margin(),self.margin(),rect_w-self.margin()*2,self.height()-self.margin()*2)
            # 文字位置
            x = (self.width()-self.arrows())//2 - fw//2
            y = self.height()//2 + fh//2
        else: # Down
            rect = QRect(self.margin(),self.margin(),self.width()-self.margin()*2,rect_h-self.margin()*2)
            # 画三角
            ploys =[QPointF(lien_x,rect_h),
                    QPointF(lien_x+line_w//2,rect_h+self.arrows()),
                    QPointF(lien_x+line_w,rect_h)]
            # 文字位置
            x = self.width() // 2 - fw//2
            y = rect_h // 2 + fh//2
        # 绘制矩形
        painter.drawRoundedRect(rect, self.radius(), self.radius())
        # 绘制三角形
        ppath.addPolygon(QPolygonF(ploys))
        painter.fillPath(ppath, self.bgColor())
        # 绘制文字
        op = QPen()
        op.setColor(QColor(255, 255, 255))
        painter.setPen(op)
        painter.drawText(x,y, self.text())

    def paintEvent(self, e:QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHints(qt.Antialiasing | qt.SmoothPixmapTransform | qt.TextAntialiasing)

        ppath = QPainterPath()

        # 绘制气泡
        self.drawBubble(painter,ppath)

        painter.end()
