# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 779)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"width:100px;height:30px;\n"
"border: 1px 1px 1px 1px solid #FFFFFF;\n"
"background:white;\n"
"-webkit-transition-duration: 0.4s; /* Safari */\n"
"transition-duration: 0.4s;\n"
"cursor: pointer;\n"
"border-width: 1.5px;\n"
"border-radius: 2px;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"}\n"
"QTabBar::tab:selected{\n"
"border-style: solid; \n"
"border-width: 1px 1px 1px 1px;\n"
"border-bottom-color:white;\n"
"background:white;\n"
"color:#000000;\n"
"border-width: 1.5px;\n"
"border-radius: 2px;\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cameraLabel = QtWidgets.QLabel(self.widget)
        self.cameraLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cameraLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.verticalLayout_2.addWidget(self.cameraLabel)
        self.camerawidget = QtWidgets.QWidget(self.widget)
        self.camerawidget.setAutoFillBackground(False)
        self.camerawidget.setObjectName("camerawidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.camerawidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.camerawidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_2.addWidget(self.camerawidget)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/img/harm-before.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/img/kitchen-before.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/pic/img/other-before.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/img/recycle-before.png"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_4.addWidget(self.progressBar, 0, 1, 1, 1)
        self.pro_label1 = QtWidgets.QLabel(self.widget_4)
        self.pro_label1.setText("")
        self.pro_label1.setObjectName("pro_label1")
        self.gridLayout_4.addWidget(self.pro_label1, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_4.addWidget(self.progressBar_2, 1, 1, 1, 1)
        self.pro_label2 = QtWidgets.QLabel(self.widget_4)
        self.pro_label2.setText("")
        self.pro_label2.setObjectName("pro_label2")
        self.gridLayout_4.addWidget(self.pro_label2, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setFormat("")
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_4.addWidget(self.progressBar_3, 2, 1, 1, 1)
        self.pro_label3 = QtWidgets.QLabel(self.widget_4)
        self.pro_label3.setText("")
        self.pro_label3.setObjectName("pro_label3")
        self.gridLayout_4.addWidget(self.pro_label3, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setFormat("")
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_4.addWidget(self.progressBar_4, 3, 1, 1, 1)
        self.pro_label4 = QtWidgets.QLabel(self.widget_4)
        self.pro_label4.setText("")
        self.pro_label4.setObjectName("pro_label4")
        self.gridLayout_4.addWidget(self.pro_label4, 3, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 6)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout_3.setStretch(0, 2)
        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/img/rec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, -543, 852, 1200))
        self.scrollAreaWidgetContents_4.setMinimumSize(QtCore.QSize(0, 1200))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plot_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.plot_widget.setObjectName("plot_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.plot_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Acc_label = QtWidgets.QLabel(self.plot_widget)
        self.Acc_label.setText("")
        self.Acc_label.setObjectName("Acc_label")
        self.horizontalLayout_2.addWidget(self.Acc_label)
        self.Loss_label = QtWidgets.QLabel(self.plot_widget)
        self.Loss_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Loss_label.setText("")
        self.Loss_label.setObjectName("Loss_label")
        self.horizontalLayout_2.addWidget(self.Loss_label)
        self.verticalLayout.addWidget(self.plot_widget)
        self.log_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.log_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.log_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.log_widget.setObjectName("log_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.log_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.train_scrollArea = QtWidgets.QScrollArea(self.log_widget)
        self.train_scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.train_scrollArea.setSizeIncrement(QtCore.QSize(0, 0))
        self.train_scrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.train_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.train_scrollArea.setWidgetResizable(True)
        self.train_scrollArea.setObjectName("train_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 797, 30036))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 2, 1, 1)
        self.train_log_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.train_log_label.setMinimumSize(QtCore.QSize(0, 30000))
        self.train_log_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.train_log_label.setFrameShape(QtWidgets.QFrame.Box)
        self.train_log_label.setText("")
        self.train_log_label.setTextFormat(QtCore.Qt.AutoText)
        self.train_log_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.train_log_label.setObjectName("train_log_label")
        self.gridLayout_6.addWidget(self.train_log_label, 1, 0, 1, 1)
        self.val_log_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.val_log_label.setMinimumSize(QtCore.QSize(0, 0))
        self.val_log_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.val_log_label.setFrameShape(QtWidgets.QFrame.Box)
        self.val_log_label.setText("")
        self.val_log_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.val_log_label.setObjectName("val_log_label")
        self.gridLayout_6.addWidget(self.val_log_label, 1, 1, 1, 1)
        self.test_log_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.test_log_label.setMinimumSize(QtCore.QSize(0, 0))
        self.test_log_label.setFrameShape(QtWidgets.QFrame.Box)
        self.test_log_label.setText("")
        self.test_log_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.test_log_label.setObjectName("test_log_label")
        self.gridLayout_6.addWidget(self.test_log_label, 1, 2, 1, 1)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 12)
        self.train_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.train_scrollArea)
        self.verticalLayout.addWidget(self.log_widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_7.addWidget(self.scrollArea_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/img/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(300, 310, 611, 341))
        self.scrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.search_edit.setObjectName("search_edit")
        self.gridLayout_2.addWidget(self.search_edit, 0, 0, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.search_button.setObjectName("search_button")
        self.gridLayout_2.addWidget(self.search_button, 0, 1, 1, 1)
        self.defination_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.defination_label.setFrameShape(QtWidgets.QFrame.Box)
        self.defination_label.setText("")
        self.defination_label.setAlignment(QtCore.Qt.AlignCenter)
        self.defination_label.setWordWrap(True)
        self.defination_label.setObjectName("defination_label")
        self.gridLayout_2.addWidget(self.defination_label, 1, 0, 1, 2)
        self.spacing_label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.spacing_label1.setFrameShape(QtWidgets.QFrame.Box)
        self.spacing_label1.setText("")
        self.spacing_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.spacing_label1.setWordWrap(True)
        self.spacing_label1.setObjectName("spacing_label1")
        self.gridLayout_2.addWidget(self.spacing_label1, 2, 0, 1, 2)
        self.content_label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.content_label1.setFrameShape(QtWidgets.QFrame.Box)
        self.content_label1.setText("")
        self.content_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label1.setWordWrap(True)
        self.content_label1.setObjectName("content_label1")
        self.gridLayout_2.addWidget(self.content_label1, 3, 0, 1, 2)
        self.spacing_label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.spacing_label2.setFrameShape(QtWidgets.QFrame.Box)
        self.spacing_label2.setText("")
        self.spacing_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.spacing_label2.setWordWrap(True)
        self.spacing_label2.setObjectName("spacing_label2")
        self.gridLayout_2.addWidget(self.spacing_label2, 4, 0, 1, 2)
        self.content_label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.content_label2.setFrameShape(QtWidgets.QFrame.Box)
        self.content_label2.setText("")
        self.content_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label2.setWordWrap(True)
        self.content_label2.setObjectName("content_label2")
        self.gridLayout_2.addWidget(self.content_label2, 5, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_2.setRowStretch(1, 20)
        self.gridLayout_2.setRowStretch(2, 3)
        self.gridLayout_2.setRowStretch(3, 10)
        self.gridLayout_2.setRowStretch(4, 3)
        self.gridLayout_2.setRowStretch(5, 10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(301, 9, 611, 302))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/pic/img/pic2.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 852, 1024))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(0, 1024))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelfeature_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_1.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_1.setText("")
        self.labelfeature_1.setPixmap(QtGui.QPixmap(":/pic/img/f1_conv1.png"))
        self.labelfeature_1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_1.setObjectName("labelfeature_1")
        self.gridLayout_5.addWidget(self.labelfeature_1, 0, 0, 1, 1)
        self.labelfeature_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_2.setText("")
        self.labelfeature_2.setPixmap(QtGui.QPixmap(":/pic/img/f2_layer1.png"))
        self.labelfeature_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_2.setObjectName("labelfeature_2")
        self.gridLayout_5.addWidget(self.labelfeature_2, 0, 1, 1, 1)
        self.labelfeature_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_3.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_3.setText("")
        self.labelfeature_3.setPixmap(QtGui.QPixmap(":/pic/img/f3_layer2.png"))
        self.labelfeature_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_3.setObjectName("labelfeature_3")
        self.gridLayout_5.addWidget(self.labelfeature_3, 1, 0, 1, 1)
        self.labelfeature_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_4.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_4.setText("")
        self.labelfeature_4.setPixmap(QtGui.QPixmap(":/pic/img/f4_layer3.png"))
        self.labelfeature_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_4.setObjectName("labelfeature_4")
        self.gridLayout_5.addWidget(self.labelfeature_4, 1, 1, 1, 1)
        self.labelfeature_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_5.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_5.setText("")
        self.labelfeature_5.setPixmap(QtGui.QPixmap(":/pic/img/f5_layer4.png"))
        self.labelfeature_5.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_5.setObjectName("labelfeature_5")
        self.gridLayout_5.addWidget(self.labelfeature_5, 2, 0, 1, 1)
        self.labelfeature_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_6.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_6.setText("")
        self.labelfeature_6.setPixmap(QtGui.QPixmap(":/pic/img/f6_avgpool.png"))
        self.labelfeature_6.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_6.setObjectName("labelfeature_6")
        self.gridLayout_5.addWidget(self.labelfeature_6, 2, 1, 1, 1)
        self.labelfeature_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_7.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_7.setText("")
        self.labelfeature_7.setPixmap(QtGui.QPixmap(":/pic/img/f7_fc.png"))
        self.labelfeature_7.setAlignment(QtCore.Qt.AlignCenter)
        self.labelfeature_7.setObjectName("labelfeature_7")
        self.gridLayout_5.addWidget(self.labelfeature_7, 3, 0, 1, 1)
        self.labelfeature_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelfeature_8.setFrameShape(QtWidgets.QFrame.Box)
        self.labelfeature_8.setText("")
        self.labelfeature_8.setObjectName("labelfeature_8")
        self.gridLayout_5.addWidget(self.labelfeature_8, 3, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_6.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action0_1 = QtWidgets.QAction(MainWindow)
        self.action0_1.setObjectName("action0_1")
        self.action0_01 = QtWidgets.QAction(MainWindow)
        self.action0_01.setObjectName("action0_01")
        self.action0_001 = QtWidgets.QAction(MainWindow)
        self.action0_001.setObjectName("action0_001")
        self.feature_action = QtWidgets.QAction(MainWindow)
        self.feature_action.setObjectName("feature_action")
        self.menu.addAction(self.action0_1)
        self.menu.addAction(self.action0_01)
        self.menu.addAction(self.action0_001)
        self.menu_2.addAction(self.feature_action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "开始检测"))
        self.label_9.setText(_translate("MainWindow", "有害垃圾"))
        self.label_10.setText(_translate("MainWindow", "厨余垃圾"))
        self.label_11.setText(_translate("MainWindow", "其他垃圾"))
        self.label_12.setText(_translate("MainWindow", "可回收垃圾"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "垃圾识别"))
        self.label_6.setText(_translate("MainWindow", "训练集日志"))
        self.label_7.setText(_translate("MainWindow", "验证集日志"))
        self.label_8.setText(_translate("MainWindow", "测试集日志"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "工作日志"))
        self.search_button.setText(_translate("MainWindow", "查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "特征图"))
        self.menu.setTitle(_translate("MainWindow", "学习率选项"))
        self.menu_2.setTitle(_translate("MainWindow", "特征图"))
        self.action0_1.setText(_translate("MainWindow", "0.1"))
        self.action0_01.setText(_translate("MainWindow", "0.01"))
        self.action0_001.setText(_translate("MainWindow", "0.001"))
        self.feature_action.setText(_translate("MainWindow", "显示特征图"))


import source_rc
