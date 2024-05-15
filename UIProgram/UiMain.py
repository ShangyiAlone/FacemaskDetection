# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 830))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/目标检测.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 100, 791, 711))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 771, 481))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_show = QtWidgets.QLabel(self.frame_2)
        self.label_show.setGeometry(QtCore.QRect(0, 0, 770, 480))
        self.label_show.setMinimumSize(QtCore.QSize(770, 480))
        self.label_show.setMaximumSize(QtCore.QSize(770, 480))
        self.label_show.setStyleSheet("border-image: url(:/icons/ui_imgs/11.png);")
        self.label_show.setText("")
        self.label_show.setObjectName("label_show")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 480, 771, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 10, 771, 221))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 751, 181))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(810, 100, 431, 711))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.groupBox = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 431, 171))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.PiclineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.PiclineEdit.setGeometry(QtCore.QRect(70, 40, 311, 31))
        self.PiclineEdit.setInputMask("")
        self.PiclineEdit.setObjectName("PiclineEdit")
        self.VideolineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.VideolineEdit.setGeometry(QtCore.QRect(70, 80, 311, 31))
        self.VideolineEdit.setObjectName("VideolineEdit")
        self.CapBtn = QtWidgets.QPushButton(self.groupBox)
        self.CapBtn.setGeometry(QtCore.QRect(30, 120, 30, 30))
        self.CapBtn.setStyleSheet("border-image: url(:/icons/ui_imgs/icons/camera.png);")
        self.CapBtn.setText("")
        self.CapBtn.setObjectName("CapBtn")
        self.PicBtn = QtWidgets.QPushButton(self.groupBox)
        self.PicBtn.setGeometry(QtCore.QRect(30, 40, 30, 30))
        self.PicBtn.setStyleSheet("border-image: url(:/icons/ui_imgs/icons/img.png);")
        self.PicBtn.setText("")
        self.PicBtn.setObjectName("PicBtn")
        self.VideoBtn = QtWidgets.QPushButton(self.groupBox)
        self.VideoBtn.setGeometry(QtCore.QRect(30, 80, 30, 30))
        self.VideoBtn.setStyleSheet("border-image: url(:/icons/ui_imgs/icons/video.png);")
        self.VideoBtn.setText("")
        self.VideoBtn.setObjectName("VideoBtn")
        self.CaplineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CaplineEdit.setGeometry(QtCore.QRect(70, 120, 311, 31))
        self.CaplineEdit.setObjectName("CaplineEdit")
        self.FilesBtn = QtWidgets.QPushButton(self.groupBox)
        self.FilesBtn.setGeometry(QtCore.QRect(390, 40, 30, 30))
        self.FilesBtn.setStyleSheet("border-image: url(:/icons/ui_imgs/icons/folder.png);")
        self.FilesBtn.setText("")
        self.FilesBtn.setObjectName("FilesBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 180, 431, 371))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_6.setGeometry(QtCore.QRect(0, 190, 431, 171))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 161, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_xmin = QtWidgets.QLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_xmin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_xmin.setFont(font)
        self.label_xmin.setText("")
        self.label_xmin.setObjectName("label_xmin")
        self.horizontalLayout.addWidget(self.label_xmin)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 60, 161, 37))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_ymin = QtWidgets.QLabel(self.layoutWidget1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_ymin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ymin.setFont(font)
        self.label_ymin.setText("")
        self.label_ymin.setObjectName("label_ymin")
        self.horizontalLayout_2.addWidget(self.label_ymin)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 120, 161, 37))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_xmax = QtWidgets.QLabel(self.layoutWidget2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_xmax.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_xmax.setFont(font)
        self.label_xmax.setText("")
        self.label_xmax.setObjectName("label_xmax")
        self.horizontalLayout_3.addWidget(self.label_xmax)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget3.setGeometry(QtCore.QRect(210, 120, 161, 37))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_ymax = QtWidgets.QLabel(self.layoutWidget3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_ymax.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ymax.setFont(font)
        self.label_ymax.setText("")
        self.label_ymax.setObjectName("label_ymax")
        self.horizontalLayout_4.addWidget(self.label_ymax)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(208, 40, 211, 37))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_nums = QtWidgets.QLabel(self.layoutWidget4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_nums.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_nums.setFont(font)
        self.label_nums.setText("")
        self.label_nums.setObjectName("label_nums")
        self.horizontalLayout_5.addWidget(self.label_nums)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 90, 291, 38))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget5)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 40, 171, 37))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.time_lb = QtWidgets.QLabel(self.layoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.time_lb.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time_lb.setFont(font)
        self.time_lb.setText("")
        self.time_lb.setObjectName("time_lb")
        self.horizontalLayout_7.addWidget(self.time_lb)
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget6.setGeometry(QtCore.QRect(210, 140, 191, 41))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.label_conf = QtWidgets.QLabel(self.layoutWidget6)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_conf.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_conf.setFont(font)
        self.label_conf.setText("")
        self.label_conf.setObjectName("label_conf")
        self.horizontalLayout_8.addWidget(self.label_conf)
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 140, 191, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_13.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.type_lb = QtWidgets.QLabel(self.layoutWidget_3)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.type_lb.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.type_lb.setFont(font)
        self.type_lb.setText("")
        self.type_lb.setObjectName("type_lb")
        self.horizontalLayout_9.addWidget(self.type_lb)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 560, 431, 141))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.SaveBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.SaveBtn.setGeometry(QtCore.QRect(30, 50, 151, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveBtn.setIcon(icon1)
        self.SaveBtn.setIconSize(QtCore.QSize(30, 30))
        self.SaveBtn.setObjectName("SaveBtn")
        self.ExitBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.ExitBtn.setGeometry(QtCore.QRect(250, 50, 151, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitBtn.setIcon(icon2)
        self.ExitBtn.setIconSize(QtCore.QSize(30, 30))
        self.ExitBtn.setObjectName("ExitBtn")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 1231, 91))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(270, 0, 811, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 311, 21))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QPushButton(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(1070, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于深度学习的人脸佩戴口罩检测系统"))
        self.groupBox_3.setTitle(_translate("MainWindow", "检测结果与位置信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件路径"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "类别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "置信度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "坐标位置"))
        self.groupBox.setTitle(_translate("MainWindow", "文件导入"))
        self.PiclineEdit.setPlaceholderText(_translate("MainWindow", "请选择图片文件"))
        self.VideolineEdit.setPlaceholderText(_translate("MainWindow", "请选择视频文件"))
        self.CaplineEdit.setPlaceholderText(_translate("MainWindow", "摄像头未开启"))
        self.groupBox_2.setTitle(_translate("MainWindow", "检测结果"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">目标位置：</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">xmin:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">ymin：</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">xmax：</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">ymax：</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">目标数目：</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">目标选择：</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">用时：</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">置信度：</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">类型：</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "操作"))
        self.SaveBtn.setText(_translate("MainWindow", "保存"))
        self.ExitBtn.setText(_translate("MainWindow", "退出"))
        self.label_3.setText(_translate("MainWindow", "基于深度学习的人脸佩戴口罩检测系统"))
        # self.label_2.setText(_translate("MainWindow", "公众号：阿旭算法与机器学习"))
        self.label_12.setText(_translate("MainWindow", "数据导出"))
import ui_sources_rc
