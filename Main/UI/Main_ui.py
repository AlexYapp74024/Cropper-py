# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(886, 584)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionDiscard = QAction(MainWindow)
        self.actionDiscard.setObjectName(u"actionDiscard")
        self.actionNext_Image = QAction(MainWindow)
        self.actionNext_Image.setObjectName(u"actionNext_Image")
        self.actionPrevious_Image = QAction(MainWindow)
        self.actionPrevious_Image.setObjectName(u"actionPrevious_Image")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionFlip_Horizontal = QAction(MainWindow)
        self.actionFlip_Horizontal.setObjectName(u"actionFlip_Horizontal")
        self.actionFlip_Vertical = QAction(MainWindow)
        self.actionFlip_Vertical.setObjectName(u"actionFlip_Vertical")
        self.actionRotate_Clockwise = QAction(MainWindow)
        self.actionRotate_Clockwise.setObjectName(u"actionRotate_Clockwise")
        self.actionRotate_Conter_Clockwise = QAction(MainWindow)
        self.actionRotate_Conter_Clockwise.setObjectName(u"actionRotate_Conter_Clockwise")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 0, 6, 6)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pb_open = QPushButton(self.frame_4)
        self.pb_open.setObjectName(u"pb_open")
        icon = QIcon()
        icon.addFile(u":/buttons/Open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_open.setIcon(icon)
        self.pb_open.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pb_open)

        self.pb_save = QPushButton(self.frame_4)
        self.pb_save.setObjectName(u"pb_save")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/Save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save.setIcon(icon1)
        self.pb_save.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pb_save)

        self.pb_discard = QPushButton(self.frame_4)
        self.pb_discard.setObjectName(u"pb_discard")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/Discard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_discard.setIcon(icon2)
        self.pb_discard.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pb_discard)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.cb_dimension = QComboBox(self.frame_5)
        self.cb_dimension.addItem("")
        self.cb_dimension.setObjectName(u"cb_dimension")

        self.horizontalLayout_7.addWidget(self.cb_dimension)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pb_prev = QPushButton(self.frame_9)
        self.pb_prev.setObjectName(u"pb_prev")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/Prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_prev.setIcon(icon3)
        self.pb_prev.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pb_prev)

        self.pb_next = QPushButton(self.frame_9)
        self.pb_next.setObjectName(u"pb_next")
        icon4 = QIcon()
        icon4.addFile(u":/buttons/Next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_next.setIcon(icon4)
        self.pb_next.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pb_next)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cb_useDefaultSavePath = QCheckBox(self.frame_7)
        self.cb_useDefaultSavePath.setObjectName(u"cb_useDefaultSavePath")

        self.horizontalLayout_10.addWidget(self.cb_useDefaultSavePath)


        self.horizontalLayout_9.addWidget(self.frame_7)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pb_change_path = QPushButton(self.frame_8)
        self.pb_change_path.setObjectName(u"pb_change_path")
        self.pb_change_path.setCheckable(False)
        self.pb_change_path.setChecked(False)

        self.horizontalLayout_11.addWidget(self.pb_change_path)

        self.pb_delete_ori = QPushButton(self.frame_8)
        self.pb_delete_ori.setObjectName(u"pb_delete_ori")
        self.pb_delete_ori.setCheckable(True)
        self.pb_delete_ori.setChecked(False)

        self.horizontalLayout_11.addWidget(self.pb_delete_ori)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.groupBox = QGroupBox(self.frame_10)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(100, 0))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sb_x = QSpinBox(self.groupBox)
        self.sb_x.setObjectName(u"sb_x")
        self.sb_x.setMinimumSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.sb_x)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_10)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.sb_y = QSpinBox(self.groupBox_2)
        self.sb_y.setObjectName(u"sb_y")
        self.sb_y.setMinimumSize(QSize(0, 0))

        self.verticalLayout_6.addWidget(self.sb_y)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_10)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.sb_s = QDoubleSpinBox(self.groupBox_3)
        self.sb_s.setObjectName(u"sb_s")
        self.sb_s.setMinimumSize(QSize(0, 0))
        self.sb_s.setMinimum(1.000000000000000)
        self.sb_s.setSingleStep(0.010000000000000)
        self.sb_s.setValue(1.000000000000000)

        self.horizontalLayout_14.addWidget(self.sb_s)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_10)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_rotate_clockwise = QPushButton(self.groupBox_4)
        self.pb_rotate_clockwise.setObjectName(u"pb_rotate_clockwise")
        icon5 = QIcon()
        icon5.addFile(u":/buttons/Rotate 90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_rotate_clockwise.setIcon(icon5)
        self.pb_rotate_clockwise.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pb_rotate_clockwise, 0, 0, 1, 1)

        self.pb_rotate_counterClockwise = QPushButton(self.groupBox_4)
        self.pb_rotate_counterClockwise.setObjectName(u"pb_rotate_counterClockwise")
        icon6 = QIcon()
        icon6.addFile(u":/buttons/Rotate 270.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_rotate_counterClockwise.setIcon(icon6)
        self.pb_rotate_counterClockwise.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pb_rotate_counterClockwise, 0, 1, 1, 1)

        self.pb_flip_horizontal = QPushButton(self.groupBox_4)
        self.pb_flip_horizontal.setObjectName(u"pb_flip_horizontal")
        icon7 = QIcon()
        icon7.addFile(u":/buttons/Flip Horizontal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_flip_horizontal.setIcon(icon7)
        self.pb_flip_horizontal.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pb_flip_horizontal, 1, 0, 1, 1)

        self.pb_flip_vertical = QPushButton(self.groupBox_4)
        self.pb_flip_vertical.setObjectName(u"pb_flip_vertical")
        icon8 = QIcon()
        icon8.addFile(u":/buttons/Flip Vertical.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_flip_vertical.setIcon(icon8)
        self.pb_flip_vertical.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.pb_flip_vertical, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addWidget(self.frame_10)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_13.addWidget(self.line_2)

        self.groupBox_gv = QGroupBox(self.frame_3)
        self.groupBox_gv.setObjectName(u"groupBox_gv")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_gv.sizePolicy().hasHeightForWidth())
        self.groupBox_gv.setSizePolicy(sizePolicy1)
        self.groupBox_gv.setLayoutDirection(Qt.RightToLeft)
        self.groupBox_gv.setAlignment(Qt.AlignCenter)
        self.groupBox_gv.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.groupBox_gv)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gv_image = QGraphicsView(self.groupBox_gv)
        self.gv_image.setObjectName(u"gv_image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gv_image.sizePolicy().hasHeightForWidth())
        self.gv_image.setSizePolicy(sizePolicy2)
        self.gv_image.setMinimumSize(QSize(0, 0))
        self.gv_image.setMouseTracking(True)
        self.gv_image.setFrameShape(QFrame.NoFrame)
        self.gv_image.setFrameShadow(QFrame.Plain)
        self.gv_image.setLineWidth(0)
        self.gv_image.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gv_image.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gv_image.setCacheMode(QGraphicsView.CacheBackground)
        self.gv_image.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.gridLayout_3.addWidget(self.gv_image, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.groupBox_gv)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 886, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionDiscard)
        self.menuFile.addAction(self.actionNext_Image)
        self.menuFile.addAction(self.actionPrevious_Image)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFlip_Horizontal)
        self.menuEdit.addAction(self.actionFlip_Vertical)
        self.menuEdit.addAction(self.actionRotate_Clockwise)
        self.menuEdit.addAction(self.actionRotate_Conter_Clockwise)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionDiscard.setText(QCoreApplication.translate("MainWindow", u"Discard", None))
#if QT_CONFIG(shortcut)
        self.actionDiscard.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Image.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Image.setShortcut(QCoreApplication.translate("MainWindow", u">", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Image.setText(QCoreApplication.translate("MainWindow", u"Previous Image", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Image.setShortcut(QCoreApplication.translate("MainWindow", u"<", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionFlip_Horizontal.setText(QCoreApplication.translate("MainWindow", u"Flip Horizontal", None))
#if QT_CONFIG(shortcut)
        self.actionFlip_Horizontal.setShortcut(QCoreApplication.translate("MainWindow", u"A, D", None))
#endif // QT_CONFIG(shortcut)
        self.actionFlip_Vertical.setText(QCoreApplication.translate("MainWindow", u"Flip Vertical", None))
#if QT_CONFIG(shortcut)
        self.actionFlip_Vertical.setShortcut(QCoreApplication.translate("MainWindow", u"W, S", None))
#endif // QT_CONFIG(shortcut)
        self.actionRotate_Clockwise.setText(QCoreApplication.translate("MainWindow", u"Rotate Clockwise", None))
#if QT_CONFIG(shortcut)
        self.actionRotate_Clockwise.setShortcut(QCoreApplication.translate("MainWindow", u"W, D", None))
#endif // QT_CONFIG(shortcut)
        self.actionRotate_Conter_Clockwise.setText(QCoreApplication.translate("MainWindow", u"Rotate Conter Clockwise", None))
#if QT_CONFIG(shortcut)
        self.actionRotate_Conter_Clockwise.setShortcut(QCoreApplication.translate("MainWindow", u"W, A", None))
#endif // QT_CONFIG(shortcut)
        self.pb_open.setText("")
        self.pb_save.setText("")
        self.pb_discard.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dimension:", None))
        self.cb_dimension.setItemText(0, QCoreApplication.translate("MainWindow", u"1920 x 1080", None))

        self.pb_prev.setText("")
        self.pb_next.setText("")
        self.cb_useDefaultSavePath.setText(QCoreApplication.translate("MainWindow", u"Use Default Save Path", None))
        self.pb_change_path.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.pb_delete_ori.setText(QCoreApplication.translate("MainWindow", u"Delete Original", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"X Position", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Y Position", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Image Scale", None))
        self.groupBox_4.setTitle("")
        self.pb_rotate_clockwise.setText("")
        self.pb_rotate_counterClockwise.setText("")
        self.pb_flip_horizontal.setText("")
        self.pb_flip_vertical.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

