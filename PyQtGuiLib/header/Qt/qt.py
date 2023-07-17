# -*- coding:utf-8 -*-
# @time:2023/1/68:49
# @author:LX
# @file:qt.py
# @software:PyCharm
from PyQtGuiLib.header.versions import PYQT_VERSIONS
from PyQtGuiLib.header import Qt,QPainter,QStyle,QSizePolicy,QEasingCurve,QCompleter

if PYQT_VERSIONS in ["PySide2","PySide6"]:
    Tool = Qt.WindowType.Tool
    Popup = Qt.WindowType.Popup
    Dialog = Qt.WindowType.Dialog
    Window = Qt.WindowType.Window
    Widget = Qt.WindowType.Widget
    SubWindow = Qt.WindowType.SubWindow
    SplashScreen = Qt.WindowType.SplashScreen
    FramelessWindowHint = Qt.WindowType.FramelessWindowHint
    WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
    WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
    WindowTransparentForInput = Qt.WindowType.WindowTransparentForInput

    NonModal = Qt.WindowModality.NonModal
    WindowModal = Qt.WindowModality.WindowModal
    ApplicationModal = Qt.WindowModality.ApplicationModal

    WindingFill = Qt.FillRule.WindingFill
    OddEvenFill = Qt.FillRule.OddEvenFill

    NoContextMenu = Qt.ContextMenuPolicy.NoContextMenu
    CustomContextMenu = Qt.ContextMenuPolicy.CustomContextMenu
    PreventContextMenu = Qt.ContextMenuPolicy.PreventContextMenu
    ActionsContextMenu = Qt.ContextMenuPolicy.ActionsContextMenu
    DefaultContextMenu = Qt.ContextMenuPolicy.DefaultContextMenu

    ArrowCursor = Qt.CursorShape.ArrowCursor
    SizeHorCursor = Qt.CursorShape.SizeHorCursor
    SizeVerCursor = Qt.CursorShape.SizeVerCursor
    OpenHandCursor = Qt.CursorShape.OpenHandCursor
    SizeFDiagCursor = Qt.CursorShape.SizeFDiagCursor
    SizeBDiagCursor = Qt.CursorShape.SizeBDiagCursor

    WA_DeleteOnClose = Qt.WidgetAttribute.WA_DeleteOnClose
    WA_StyledBackground = Qt.WidgetAttribute.WA_StyledBackground
    WA_TranslucentBackground = Qt.WidgetAttribute.WA_TranslucentBackground

    DotLine = Qt.PenStyle.DotLine
    DashLine = Qt.PenStyle.DashLine
    SolidLine = Qt.PenStyle.SolidLine
    DashDotLine = Qt.PenStyle.DashDotLine
    DashDotDotLine = Qt.PenStyle.DashDotDotLine
    CustomDashLine = Qt.PenStyle.CustomDashLine
    NoPen = Qt.PenStyle.NoPen
    NoBrush = Qt.BrushStyle.NoBrush
    red = Qt.GlobalColor.red
    blue = Qt.GlobalColor.blue
    gray = Qt.GlobalColor.gray
    white = Qt.GlobalColor.white
    green = Qt.GlobalColor.green
    black = Qt.GlobalColor.black
    yellow = Qt.GlobalColor.yellow
    darkRed = Qt.GlobalColor.darkRed
    darkBlue = Qt.GlobalColor.darkBlue
    darkGray = Qt.GlobalColor.darkGray
    darkGreen = Qt.GlobalColor.darkGreen
    darkYellow = Qt.GlobalColor.darkYellow
    darkMagenta = Qt.GlobalColor.darkMagenta
    transparent = Qt.GlobalColor.transparent

    Antialiasing = QPainter.RenderHint.Antialiasing
    SmoothPixmapTransform = QPainter.RenderHint.SmoothPixmapTransform
    TextAntialiasing = QPainter.RenderHint.TextAntialiasing
    PE_Widget = QStyle.PrimitiveElement.PE_Widget

    KeepAspectRatio = Qt.AspectRatioMode.KeepAspectRatio
    IgnoreAspectRatio = Qt.AspectRatioMode.IgnoreAspectRatio
    KeepAspectRatioByExpanding = Qt.AspectRatioMode.KeepAspectRatioByExpanding

    FastTransformation = Qt.TransformationMode.FastTransformation
    SmoothTransformation = Qt.TransformationMode.SmoothTransformation

    Vertical = Qt.Orientation.Vertical
    Horizontal = Qt.Orientation.Horizontal

    PolicyMinimum = QSizePolicy.Policy.Minimum
    PolicyExpanding = QSizePolicy.Policy.Expanding

    AlignTop = Qt.AlignmentFlag.AlignTop
    AlignLeft = Qt.AlignmentFlag.AlignLeft
    AlignRight = Qt.AlignmentFlag.AlignRight
    AlignCenter = Qt.AlignmentFlag.AlignCenter
    AlignBottom = Qt.AlignmentFlag.AlignBottom
    AlignVCenter = Qt.AlignmentFlag.AlignVCenter
    AlignHCenter = Qt.AlignmentFlag.AlignHCenter
    AlignJustify = Qt.AlignmentFlag.AlignJustify
    AlignLeading = Qt.AlignmentFlag.AlignLeading
    AlignTrailing = Qt.AlignmentFlag.AlignTrailing

    LeftButton = Qt.MouseButton.LeftButton
    RightButton = Qt.MouseButton.RightButton
    MiddleButton = Qt.MouseButton.MiddleButton

    MoveAction = Qt.DropAction.MoveAction
    ActionMask = Qt.DropAction.ActionMask
    CopyAction = Qt.DropAction.CopyAction
    LinkAction = Qt.DropAction.LinkAction
    TargetMoveAction = Qt.DropAction.TargetMoveAction

    ScrollBarAlwaysOn = Qt.ScrollBarPolicy.ScrollBarAlwaysOn
    ScrollBarAsNeeded = Qt.ScrollBarPolicy.ScrollBarAsNeeded
    ScrollBarAlwaysOff = Qt.ScrollBarPolicy.ScrollBarAlwaysOff

    MatchWrap = Qt.MatchFlag.MatchWrap
    MatchExactly = Qt.MatchFlag.MatchExactly
    MatchContains = Qt.MatchFlag.MatchContains
    MatchWildcard = Qt.MatchFlag.MatchWildcard
    MatchEndsWith = Qt.MatchFlag.MatchEndsWith

    TextDontClip = Qt.TextFlag.TextDontClip
    TextWordWrap = Qt.TextFlag.TextWordWrap
    TextSingleLine = Qt.TextFlag.TextSingleLine
    TextExpandTabs = Qt.TextFlag.TextExpandTabs

    ElideLeft = Qt.TextElideMode.ElideLeft
    ElideNone = Qt.TextElideMode.ElideNone
    ElideRight = Qt.TextElideMode.ElideRight
    ElideMiddle = Qt.TextElideMode.ElideMiddle

    DisplayRole = Qt.ItemDataRole.DisplayRole
    DisplayPropertyRole = Qt.ItemDataRole.DisplayPropertyRole
    ToolTipPropertyRole = Qt.ItemDataRole.ToolTipPropertyRole
    StatusTipPropertyRole = Qt.ItemDataRole.StatusTipPropertyRole

    ToolButtonIconOnly = Qt.ToolButtonStyle.ToolButtonIconOnly
    ToolButtonTextOnly = Qt.ToolButtonStyle.ToolButtonTextOnly
    ToolButtonFollowStyle = Qt.ToolButtonStyle.ToolButtonFollowStyle
    ToolButtonTextUnderIcon = Qt.ToolButtonStyle.ToolButtonTextUnderIcon
    ToolButtonTextBesideIcon = Qt.ToolButtonStyle.ToolButtonTextBesideIcon




    PM_LayoutHorizontalSpacing = QStyle.PixelMetric.PM_LayoutHorizontalSpacing
    PM_LayoutVerticalSpacing = QStyle.PixelMetric.PM_LayoutVerticalSpacing

    NoFocus = Qt.FocusPolicy.NoFocus
    TabFocus = Qt.FocusPolicy.TabFocus
    InCurve = QEasingCurve.Type.InCurve
    ClickFocus = Qt.FocusPolicy.ClickFocus
    OutBounce = QEasingCurve.Type.OutBounce
    SineCurve = QEasingCurve.Type.SineCurve
    StrongFocus = Qt.FocusPolicy.StrongFocus
    CosineCurve = QEasingCurve.Type.CosineCurve

    Checked = Qt.CheckState.Checked
    Unchecked = Qt.CheckState.Unchecked
    PartiallyChecked = Qt.CheckState.PartiallyChecked

    AscendingOrder = Qt.SortOrder.AscendingOrder
    DescendingOrder = Qt.SortOrder.DescendingOrder

    PopupCompletion = QCompleter.CompletionMode.PopupCompletion
    InlineCompletion = QCompleter.CompletionMode.InlineCompletion
    UnfilteredPopupCompletion = QCompleter.CompletionMode.UnfilteredPopupCompletion

    Key_0 = Qt.Key.Key_0
    Key_1 = Qt.Key.Key_1
    Key_2 = Qt.Key.Key_2
    Key_3 = Qt.Key.Key_3
    Key_4 = Qt.Key.Key_4
    Key_5 = Qt.Key.Key_5
    Key_6 = Qt.Key.Key_6
    Key_7 = Qt.Key.Key_7
    Key_8 = Qt.Key.Key_8
    Key_9 = Qt.Key.Key_9
    Key_Up = Qt.Key.Key_Up
    Key_Alt = Qt.Key.Key_Alt
    Key_Tab = Qt.Key.Key_Tab
    Key_Down = Qt.Key.Key_Down
    Key_Enter = Qt.Key.Key_Enter
    Key_Return = Qt.Key.Key_Return
    Key_Backspace = Qt.Key.Key_Backspace

    ForbiddenCursor = Qt.CursorShape.ForbiddenCursor
    PointingHandCursor = Qt.CursorShape.PointingHandCursor
