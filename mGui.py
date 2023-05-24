#Smart FVR - Smart Finger Vein Recognizer
#Application with GUI PySide, running on Raspberry Pi with PiCamera, Matrix of Infrared LEDs 8x2 870nm
#Utilizes ski-image and scikit-learn packages for machine learning
#Using KNN Classification of recognizing finger veins of people, 10 of which data is stored to sqlite database
#pygame library used for camera preview 


from PySide import QtCore, QtGui
import sys, time, pygame, pygame.camera
import Ref
import numpy as np
from PySide import QtCore, QtGui
from KNNClassifier import *
from DBManager import *
from pygame.locals import *
from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import *
from skimage import color, io, transform  
from imageProcessing import *

name = ""
pin = 0
choice = 0 

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        mainWindow.resize(1000, 600)
        mainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        mainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setToolTip("")
        
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("QMainWindow {background-color:#383838 ;}\n"
"QToolTip{padding:1px;}\n"
"QMessageBox{background-color:#383838 ;\n"
"color:#ff6c00;\n"
"font-size:14px;}\n"
"\n"
"")
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 500, 961, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.refBtn = QtGui.QPushButton(self.layoutWidget)
        self.refBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.refBtn.setStyleSheet("QPushButton{background-color: transparent;\n"
"    background: none;\n"
"    background-repeat: none;\n"
"    border:none;}\n"
"QPushButton:hover{\n"
"    \n"
"    }    ")
        self.refBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/refer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refBtn.setIcon(icon1)
        self.refBtn.setIconSize(QtCore.QSize(60, 60))
        self.refBtn.setObjectName("refBtn")
        self.horizontalLayout.addWidget(self.refBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.photoLabel = QtGui.QLabel(self.layoutWidget)
        self.photoLabel.setMinimumSize(QtCore.QSize(80, 80))
        self.photoLabel.setMaximumSize(QtCore.QSize(80, 80))
        self.photoLabel.setText("")
        self.photoLabel.setObjectName("photoLabel")
        self.horizontalLayout.addWidget(self.photoLabel)
        self.nameLabel = QtGui.QLabel(self.layoutWidget)
        self.nameLabel.setMinimumSize(QtCore.QSize(200, 80))
        self.nameLabel.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"color:#ff6c00;\n"
"    ")
        self.nameLabel.setText("")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.closeBtn = QtGui.QPushButton(self.layoutWidget) 
        self.closeBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.closeBtn.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.closeBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QtCore.QSize(60, 60))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(19, 10, 961, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.Title = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        #font.setPointSize(-1)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:#ff6c00;background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"font-size: 32px")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.horizontalLayout_3.addWidget(self.Title)
        spacerItem5 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(22, 80, 951, 392))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Settings = QtGui.QGroupBox(self.layoutWidget2)
        self.Settings.setMinimumSize(QtCore.QSize(460, 390))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Settings.setFont(font)
        self.Settings.setCursor(QtCore.Qt.ArrowCursor)
        self.Settings.setStyleSheet("QGroupBox{border: 1px solid;\n"
"border-radius:10px;\n"
"border-color:#ff6c00;\n"
"color:#ff6c00;\n"
"background-color: transparent;}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; \n"
"}\n"
"\n"
"    ")
        self.Settings.setTitle("")
        self.Settings.setObjectName("Settings")
        self.layoutWidget3 = QtGui.QWidget(self.Settings)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 330, 441, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.resetBtn = QtGui.QPushButton(self.layoutWidget3)
        self.resetBtn.setEnabled(False)
        self.resetBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.resetBtn.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.resetBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetBtn.setIcon(icon3)
        self.resetBtn.setIconSize(QtCore.QSize(45, 45))
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout_5.addWidget(self.resetBtn)
        spacerItem7 = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.startBtn = QtGui.QPushButton(self.layoutWidget3)
        self.startBtn.setEnabled(False)
        self.startBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.startBtn.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.startBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startBtn.setIcon(icon4)
        self.startBtn.setIconSize(QtCore.QSize(45, 45))
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_5.addWidget(self.startBtn)
        spacerItem8 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.Step1 = QtGui.QLabel(self.Settings)
        self.Step1.setGeometry(QtCore.QRect(30, 20, 421, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step1.setFont(font)
        self.Step1.setStyleSheet("color:#ff6c00;background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.Step1.setObjectName("Step1")
        self.layoutWidget4 = QtGui.QWidget(self.Settings)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 70, 421, 42))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clfChoice = QtGui.QComboBox(self.layoutWidget4)
        self.clfChoice.setMinimumSize(QtCore.QSize(360, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clfChoice.setFont(font)
        self.clfChoice.setStyleSheet("QComboBox {\n"
"    border: 1px solid ;\n"
"    border-radius: 10px;\n"
"border-color:#ff6c00;\n"
"background-color:white;\n"
"    }\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 10px;\n"
"    /*border-left-color: darkgray;\n"
"    /*border-left-style: solid; /* just a single line */\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(/home/pi/Desktop/New/FVR/Icons/drops.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: #ff6c00;\n"
"    background-color:transparent;\n"
"        \n"
"}")
        self.clfChoice.setObjectName("clfChoice")
        self.clfChoice.addItem("")
        self.clfChoice.setItemText(0, "")
        self.clfChoice.addItem("")
        self.clfChoice.addItem("")
        self.horizontalLayout_6.addWidget(self.clfChoice)
        self.clfCheck = QtGui.QPushButton(self.layoutWidget4)
        self.clfCheck.setEnabled(False)
        self.clfCheck.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.clfCheck.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clfCheck.setIcon(icon5)
        self.clfCheck.setIconSize(QtCore.QSize(21, 21))
        self.clfCheck.setObjectName("clfCheck")
        self.horizontalLayout_6.addWidget(self.clfCheck)
        self.Step2 = QtGui.QLabel(self.Settings)
        self.Step2.setGeometry(QtCore.QRect(30, 140, 421, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step2.setFont(font)
        self.Step2.setStyleSheet("color:#ff6c00;background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.Step2.setObjectName("Step2")
        self.layoutWidget5 = QtGui.QWidget(self.Settings)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 190, 419, 42))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dbChoice = QtGui.QComboBox(self.layoutWidget5)
        self.dbChoice.setEnabled(False)
        self.dbChoice.setMinimumSize(QtCore.QSize(360, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dbChoice.setFont(font)
        self.dbChoice.setStyleSheet("QComboBox {\n"
"    border: 1px solid ;\n"
"    border-radius: 10px;\n"
"border-color:#ff6c00;\n"
"background-color:white;\n"
"    }\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 10px;\n"
"    /*border-left-color: darkgray;\n"
"    /*border-left-style: solid; /* just a single line */\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(/home/pi/Desktop/New/FVR/Icons/drops.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: #ff6c00;\n"
"    background-color:transparent;\n"
"        \n"
"}")
        self.dbChoice.setObjectName("dbChoice")
        self.dbChoice.addItem("")
        self.dbChoice.setItemText(0, "")
        self.dbChoice.addItem("")
        self.dbChoice.addItem("")
        self.horizontalLayout_7.addWidget(self.dbChoice)
        self.dbCheck = QtGui.QPushButton(self.layoutWidget5)
        self.dbCheck.setEnabled(False)
        self.dbCheck.setMinimumSize(QtCore.QSize(51, 21))
        self.dbCheck.setMaximumSize(QtCore.QSize(51, 21))
        self.dbCheck.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.dbCheck.setText("")
        self.dbCheck.setIcon(icon5)
        self.dbCheck.setIconSize(QtCore.QSize(21, 21))
        self.dbCheck.setObjectName("dbCheck")
        self.horizontalLayout_7.addWidget(self.dbCheck)
        self.Step3 = QtGui.QLabel(self.Settings)
        self.Step3.setGeometry(QtCore.QRect(30, 260, 421, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step3.setFont(font)
        self.Step3.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"color:#ff6c00;\n"
"    ")
        self.Step3.setObjectName("Step3")
        self.horizontalLayout_4.addWidget(self.Settings)
        spacerItem9 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.cameraView = QtGui.QGroupBox(self.layoutWidget2)
        self.cameraView.setMinimumSize(QtCore.QSize(460, 390))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cameraView.setFont(font)
        self.cameraView.setStyleSheet("QGroupBox{border: 1px solid;\n"
"border-radius:10px;\n"
"border-color:#ff6c00;\n"
"color:#ff6c00;\n"
"background-color: transparent;}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"}\n"
"\n"
"    ")
        self.cameraView.setTitle("")
        self.cameraView.setObjectName("cameraView")
        self.layoutWidget6 = QtGui.QWidget(self.cameraView)
        self.layoutWidget6.setGeometry(QtCore.QRect(0, 10, 459, 371))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.Camera = QtGui.QLabel(self.layoutWidget6)
        self.Camera.setMinimumSize(QtCore.QSize(387, 310))
        self.Camera.setMaximumSize(QtCore.QSize(387, 310))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.Camera.setFont(font)
        self.Camera.setText("")
        self.Camera.setObjectName("Camera")
        self.horizontalLayout_8.addWidget(self.Camera)
        spacerItem11 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.photoBtn = QtGui.QPushButton(self.layoutWidget6)
        self.photoBtn.setEnabled(False)
        self.photoBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.photoBtn.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.photoBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoBtn.setIcon(icon6)
        self.photoBtn.setIconSize(QtCore.QSize(45, 45))
        self.photoBtn.setObjectName("photoBtn")
        self.horizontalLayout_2.addWidget(self.photoBtn)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.cancelBtn = QtGui.QPushButton(self.layoutWidget6)
        self.cancelBtn.setEnabled(False)
        self.cancelBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.cancelBtn.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.cancelBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelBtn.setIcon(icon7)
        self.cancelBtn.setIconSize(QtCore.QSize(45, 45))
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.cameraView)
        self.animLabel = QtGui.QLabel(self.centralwidget)
        self.animLabel.setGeometry(QtCore.QRect(460, 490, 85, 85))
        self.animLabel.setMinimumSize(QtCore.QSize(85, 85))
        self.animLabel.setMaximumSize(QtCore.QSize(85, 85))
        self.animLabel.setText("")
        self.animLabel.setObjectName("animLabel")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


        self.refMsgBox = QtGui.QMessageBox()
        
        self.refMsgBox.setText("Smart FVR Project\n""")
        self.refMsgBox.setWindowTitle("Πληροφορίες")
        self.refMsgBox.setStyleSheet("QMessageBox{background-color:#383838 ;}\n"
                                    "QMessageBox QLabel{color:#ff6c00;\n"
                                    "text-align:center;\n"
                                    "font-size:16px;}\n")
        ic1 = QtGui.QIcon()
        ic1.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refMsgBox.setWindowIcon(ic1)
        self.refMsgBoxBtnYes = self.refMsgBox.addButton(QtGui.QMessageBox.Ok)
        self.refMsgBoxBtnYes.setCursor(QtCore.Qt.PointingHandCursor)
        self.refMsgBoxBtnYes.setText("")
        self.refMsgBoxBtnYes.setIconSize(QtCore.QSize(45, 45))
        self.refMsgBoxBtnYes.setToolTip(QtGui.QApplication.translate("mainWindow", "Ok!", None, QtGui.QApplication.UnicodeUTF8))
        self.refMsgBoxBtnYes.setStyleSheet("QPushButton{"
                                         "qproperty-icon: url(/home/pi/Desktop/New/FVR/Icons/ok.png);\n"
                                         "background: none;\n"
                                         "border: none;\n"
                                         "background - repeat: none;\n}")
        
        self.clMsgBox = QtGui.QMessageBox()
        self.clMsgBox.setText("Do ypu want to close the app?")
        self.clMsgBox.setWindowTitle("Κλείσιμο εφαρμογής")
        self.clMsgBox.setStyleSheet("QMessageBox{background-color:#383838 ;}\n"
                                    "QMessageBox QLabel{color:#ff6c00;\n"
                                    "text-align:center;\n"
                                    "font-size:16px;}\n")
        ic = QtGui.QIcon()
        ic.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clMsgBox.setWindowIcon(ic)

        self.clMsgBoxBtnYes = self.clMsgBox.addButton(QtGui.QMessageBox.Ok)
        self.clMsgBoxBtnYes.setCursor(QtCore.Qt.PointingHandCursor)
        self.clMsgBoxBtnYes.setText("")
        self.clMsgBoxBtnYes.setIconSize(QtCore.QSize(45, 45))
        self.clMsgBoxBtnYes.setToolTip(QtGui.QApplication.translate("mainWindow", "Close ", None, QtGui.QApplication.UnicodeUTF8))
        self.clMsgBoxBtnYes.setStyleSheet("QPushButton{"
                                         "qproperty-icon: url(/home/pi/Desktop/New/FVR/Icons/ok.png);\n"
                                         "background: none;\n"
                                         "border: none;\n"
                                         "background - repeat: none;\n}")

        self.clMsgBoxBtnNo = self.clMsgBox.addButton(QtGui.QMessageBox.Abort)
        self.clMsgBoxBtnNo.setStyleSheet("QPushButton{background:transparent;\n"
                                          "qproperty-icon: url(/home/pi/Desktop/New/FVR/Icons/cancel.png);\n"
                                          "background: none;\n"
                                          "border: none;\n"
                                          "background - repeat: none;\n}")
        self.clMsgBoxBtnNo.setCursor(QtCore.Qt.PointingHandCursor)
        self.clMsgBoxBtnNo.setText("")
        self.clMsgBoxBtnNo.setIconSize(QtCore.QSize(45, 45))
        self.clMsgBoxBtnNo.setToolTip(QtGui.QApplication.translate("mainWindow", "Cancel ", None, QtGui.QApplication.UnicodeUTF8))
        
        
        
 



        self.notMsgBox = QtGui.QMessageBox()
        self.notMsgBox.setText("User is not found! Please, try again")
        self.notMsgBox.setWindowTitle("Ταυτοποίηση")
        self.notMsgBox.setStyleSheet("QMessageBox{background-color:#383838 ;}\n"
                                    "QMessageBox QLabel{color:#ff6c00;\n"
                                    "text-align:center;\n"
                                    "font-size:16px;}\n")
        ic = QtGui.QIcon()
        ic.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notMsgBox.setWindowIcon(ic)

        self.notMsgBoxBtnYes = self.notMsgBox.addButton(QtGui.QMessageBox.Ok)
        self.notMsgBoxBtnYes.setCursor(QtCore.Qt.PointingHandCursor)
        self.notMsgBoxBtnYes.setText("")
        self.notMsgBoxBtnYes.setIconSize(QtCore.QSize(45, 45))
        self.notMsgBoxBtnYes.setToolTip(QtGui.QApplication.translate("mainWindow", "Ok ", None, QtGui.QApplication.UnicodeUTF8))
        self.notMsgBoxBtnYes.setStyleSheet("QPushButton{"
                                         "qproperty-icon: url(/home/pi/Desktop/New/FVR/Icons/ok.png);\n"
                                         "background: none;\n"
                                         "border: none;\n"
                                         "background - repeat: none;\n}")

        self.notMsgBoxBtnNo = self.notMsgBox.addButton(QtGui.QMessageBox.Abort)
        self.notMsgBoxBtnNo.setStyleSheet("QPushButton{background:transparent;\n"
                                          "qproperty-icon: url(/home/pi/Desktop/New/FVR/Icons/cancel.png);\n"
                                          "background: none;\n"
                                          "border: none;\n"
                                          "background - repeat: none;\n}")
        self.notMsgBoxBtnNo.setCursor(QtCore.Qt.PointingHandCursor)
        self.notMsgBoxBtnNo.setText("")
        self.notMsgBoxBtnNo.setIconSize(QtCore.QSize(45, 45))
        self.notMsgBoxBtnNo.setToolTip(QtGui.QApplication.translate("mainWindow", "Cancel ", None, QtGui.QApplication.UnicodeUTF8))
        

        self.foundMsgBox = QtGui.QMessageBox()
        self.foundMsgBox.setText("")
        self.foundMsgBox.resize(400,300)
        self.foundMsgBox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.foundMsgBox.setWindowTitle("Βρέθηκε!")
        self.foundMsgBox.setStyleSheet("QMessageBox{background-color:#383838 ;}\n"
                                    "QMessageBox QLabel{color:#ff6c00;\n"
                                    "text-align:center;\n"
                                    "font-size:24px;}\n")
        ic = QtGui.QIcon()
        ic.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.foundMsgBox.setWindowIcon(ic)

        self.foundMsgBoxBtnYes = self.foundMsgBox.addButton(QtGui.QMessageBox.Ok)
        self.foundMsgBoxBtnYes.setCursor(QtCore.Qt.PointingHandCursor)
        self.foundMsgBoxBtnYes.setText("")
        self.foundMsgBoxBtnYes.setIconSize(QtCore.QSize(45, 45))
        self.foundMsgBoxBtnYes.setToolTip(QtGui.QApplication.translate("mainWindow", "Ok ", None, QtGui.QApplication.UnicodeUTF8))
        self.foundMsgBoxBtnYes.setStyleSheet("QPushButton{"
                                         "qproperty-icon: url(/home/pi/Desktop/New/FVR/Icons/ok.png);\n"
                                         "background: none;\n"
                                         "border: none;\n"
                                         "background - repeat: none;\n}")

        """self.foundMsgBoxBtnNo = self.foundMsgBox.addButton(QtGui.QMessageBox.Abort)
        self.foundMsgBoxBtnNo.setStyleSheet("QPushButton{background:transparent;\n"
                                          "qproperty-icon: url(/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/cancel.png);\n"
                                          "background: none;\n"
                                          "border: none;\n"
                                          "background - repeat: none;\n}")
        self.foundMsgBoxBtnNo.setCursor(QtCore.Qt.PointingHandCursor)
        self.foundMsgBoxBtnNo.setText("")
        self.foundMsgBoxBtnNo.setIconSize(QtCore.QSize(45, 45))
        self.foundMsgBoxBtnNo.setToolTip(QtGui.QApplication.translate("mainWindow", "Ακύρωση ", None, QtGui.QApplication.UnicodeUTF8))"""


        
        self.closeBtn.clicked.connect(self.exitApp)
        self.clfChoice.activated[str].connect(self.chooseClf)
        self.dbChoice.activated[str].connect(self.chooseDb)
        self.resetBtn.clicked.connect(self.reset)
        self.refBtn.clicked.connect(Ref.openRefWindow)
        self.startBtn.clicked.connect(self.startVideoCapture)
        self.photoBtn.clicked.connect(self.takePhoto)
        self.cancelBtn.clicked.connect(self.cancelPhotoCapture)
        
        
        
        #self.workThread = Thread()
        self.knnClassifier = knnClassifier()
        gif = "/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/loader.gif"
        self.movie = QtGui.QMovie(gif) 
        self.movie.setCacheMode(QtGui.QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        self.animLabel.setMovie(self.movie)


    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Smart FVR", None, QtGui.QApplication.UnicodeUTF8))
        self.refBtn.setToolTip(QtGui.QApplication.translate("mainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.closeBtn.setToolTip(QtGui.QApplication.translate("mainWindow", "Close ", None, QtGui.QApplication.UnicodeUTF8))
        self.Title.setText(QtGui.QApplication.translate("mainWindow", "Smart FVR", None, QtGui.QApplication.UnicodeUTF8))
        self.resetBtn.setToolTip(QtGui.QApplication.translate("mainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.startBtn.setToolTip(QtGui.QApplication.translate("mainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.Step1.setText(QtGui.QApplication.translate("mainWindow", "Step 1   Choose the procedure", None, QtGui.QApplication.UnicodeUTF8))
        self.clfChoice.setItemText(1, QtGui.QApplication.translate("mainWindow", "   Identification", None, QtGui.QApplication.UnicodeUTF8))
        self.clfChoice.setItemText(2, QtGui.QApplication.translate("mainWindow", "   Confirmation", None, QtGui.QApplication.UnicodeUTF8))
        self.Step2.setText(QtGui.QApplication.translate("mainWindow", "Step 2   Choose a Database", None, QtGui.QApplication.UnicodeUTF8))
        self.dbChoice.setItemText(1, QtGui.QApplication.translate("mainWindow", "   Database", None, QtGui.QApplication.UnicodeUTF8))
        self.dbChoice.setItemText(2, QtGui.QApplication.translate("mainWindow", "   DataB", None, QtGui.QApplication.UnicodeUTF8))
        self.Step3.setText(QtGui.QApplication.translate("mainWindow", "Step 3   Press \"Start\" for launch", None, QtGui.QApplication.UnicodeUTF8))
        self.photoBtn.setToolTip(QtGui.QApplication.translate("mainWindow", "Photo", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setToolTip(QtGui.QApplication.translate("mainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))


    def chooseClf(self):
        global choice
        text = self.clfChoice.currentText()
        if text == "   Identification":
            self.clfCheck.setEnabled(True)
            self.dbChoice.setEnabled(True)
            self.clfChoice.setEnabled(False)
            self.resetBtn.setEnabled(True)
            choice = 1
            
                    
                 
        elif text == "   Confirmation":
            self.resetBtn.setEnabled(True)
            self.dbChoice.setEnabled(True)
            self.clfChoice.setEnabled(False)
            self.clfCheck.setEnabled(True)
            choice = 2
                               
        return 

    def chooseDb(self):
        global choice
        text = self.dbChoice.currentText()
        if text == "   Database" and choice == 1:
            self.knnClassifier.trainKnn()
            self.dbCheck.setEnabled(True)
            self.dbChoice.setEnabled(False)
            self.startBtn.setEnabled(True)
                 
            
                 
        elif text == "   DataB" and choice == 2:
            self.resetBtn.setEnabled(True)
            self.dbChoice.setEnabled(True)
            self.clfChoice.setEnabled(False)
            self.dbCheck.setEnabled(True)
            self.userVerify()    
             
        return         
            

    def reset(self):
        global choice
        global pin
        global name
        choice = 0
        pin = 0 
        name = ""
        self.clfCheck.setEnabled(False)
        self.dbChoice.setEnabled(False)
        self.clfChoice.setEnabled(True)
        self.resetBtn.setEnabled(False)
        self.dbCheck.setEnabled(False)
        self.startBtn.setEnabled(False)
        self.clfChoice.setCurrentIndex(0)
        self.dbChoice.setCurrentIndex(0)
        #self.Camera.clear()
        self.photoBtn.setEnabled(False)
        self.cancelBtn.setEnabled(False)
        self.cancelPhotoCapture()
        self.Timer.stop()
        return


    def startVideoCapture(self):
        
        
        self.startBtn.setEnabled(False)
        self.photoBtn.setEnabled(True)
        self.cancelBtn.setEnabled(True)
        self.camera = PiCamera()
        self.camera.resolution = (1920, 1080)
        self.camera.saturation = -100
        self.camera.contrast = 30
        self.capture = True
        time.sleep(0.1)
        self.camera.start_preview(fullscreen=False, window = (950, 300, 440, 360))
        return
          
    def takePhoto(self):
        global name
        self.camera.capture('/home/pi/Desktop/New/FVR/Temp/temp.png')
        #pygame.image.save(screen, "/home/pi/Desktop/New/Finger-Vein Recognizer/Temp/temp.png" )
        """img = '/home/pi/Desktop/New/Finger-Vein Recognizer/Temp/temp.png'
        img = QtGui.QImage(img)
        self.Camera.setPixmap(QtGui.QPixmap.fromImage(img))"""
         
        self.capture = False
        self.camera.stop_preview()
        self.camera.close()
        #self.Camera.clear()
        self.photoBtn.setEnabled(False)
        self.cancelBtn.setEnabled(False)
        global choice
        if choice == 1:
            #self.playGif()     
            prediction, distance = self.knnClassifier.classify()
            print(prediction)
            dist = dbReadDist(prediction)
            print(dist)
            if distance<=dist:
                #elf.stopGif()
                #userFound.openWindow()
                #userFound.showUser(prediction)
                self.foundMsgBox.setText(prediction)        
                self.foundMsgBox.exec_()
                if self.foundMsgBox.clickedButton() == self.foundMsgBoxBtnYes:
                    self.reset() 
                #Ui_userFound.showUser()
                #openFoundWindow()   
                
            else:
                #self.stopGif()
                self.notFoundKnn()             
        
        elif choice == 2:
            distance = passVerify(name)
            print(distance)     
            dist = dbReadDist(name)
            print(dist)      
            if distance<=dist:
                #userFound.openWindow()
                #userFound.showUser(prediction)
                self.foundMsgBox.setText(name)        
                self.foundMsgBox.exec_()
                if self.foundMsgBox.clickedButton() == self.foundMsgBoxBtnYes:
                    self.reset()
                #openFoundWindow()    
            else:
                self.notFoundPass()             
        #self.facePhoto()
        #image = '/home/pi/Desktop/New/Finger-Vein Recognizer/Images/'+str(self.pred)+'.png'
        #img = QtGui.QImage(image)
        #self.photoView.setPixmap(QtGui.QPixmap.fromImage(img))
        
        #self.Timer.timeout.connect(self.updLabels)
        
        #self.Camera.setPixmap(QtGui.QPixmap.fromImage(img))
        
        return

    def userVerify(self):
        openPassWindow()
        global pin
        global name
        pin = int(pin)
        if pin:
            for i in range(1, 6): 
                p = dbReadPass(i)   
                if p == pin:
                    name = dbReadPass1(p)
                    print(name)
                    break         
            if name:
                self.startVideoCapture()
                
                #self.foundMsgBox.exec_()
            else:
                self.notFoundPass() 
        return

    def facePhoto(self):
        res = (640, 480)
        pygame.init()
        pygame.camera.init()
        camlist = pygame.camera.list_cameras()
        display = pygame.display.set_mode(res, 0)
        camera = pygame.camera.Camera(camlist[0], res)
        camera.start()
        screen = pygame.surface.Surface(res, 0, display)
        capture = True
        image = camera.get_image(screen)
        while capture:
            image = camera.get_image(image)
            image = pygame.transform.scale(image,(640,480))
            display.blit(screen, (0,0))
            pygame.display.flip()
            
            #img = QtGui.QImage(image, image.size[1], image.size[0], QtGui.QImage.Format_ARGB32)

            #self.Camera.setPixmap(QtGui.QPixmap.fromImage(img)) 
            for e in pygame.event.get():
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    capture = False
                    camera.stop()
                    pygame.quit()
                elif e.type == KEYDOWN and e.key == K_SPACE:
                    pygame.image.save(screen, '/home/pi/Desktop/New/Finger-Vein Recognizer/Images/'+str(self.pred)+'.png')
                    capture = False
                    camera.stop()
                    pygame.quit()
        self.convert2Grey()
            
            
        #rawCapture = PiRGBArray(self.camera, size=(1920,1080))
        
        """while self.capture:
            time.sleep(0.5)
            #for frame in self.camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
                #image = frame.array
                
                #image = Image.fromarray(image.astype(np.uint8))
                
                #img = QtGui.QImage(image, image.size[0], image.size[1], QtGui.QImage.Format_ARGB32)
                #img = ImageQt.ImageQt(image)
                #self.Camera.setPixmap(QtGui.QPixmap.fromImage(img))
            rawCapture.truncate(0)
            if self.capture == False:
                break"""
       
    def cancelPhotoCapture(self):
        self.capture = False
        self.camera.stop_preview()
        self.camera.close()
        self.Camera.clear()
        self.photoBtn.setEnabled(False)
        self.cancelBtn.setEnabled(False)
    
    def convert2Grey(self):
        image = io.imread('/home/pi/Desktop/New/FVR/Images/'+str(self.pred)+'.png')
        image = transform.resize(image, (90,90))
        image = color.rgb2gray(image)
        io.imsave('/home/pi/Desktop/New/Finger-Vein Recognizer/Images/'+str(self.pred)+'.png',image)
        return
    
    def insertUser(self):
        text, ok = QtGui.QInputDialog.getText(None, 'User is not found!', 'Press the name of new User\n') 
        if ok: 
            print('User regs')
        else:
            print('No way!')                
    
    def playGif(self):
        self.workThread.start()
        self.movie.start()
        return
        
    def stopGif(self):
        self.workThread.start()
        self.movie.stop()
        
        return
        
    def exitApp(self):
        self.clMsgBox.exec_()
        if self.clMsgBox.clickedButton() == self.clMsgBoxBtnYes:
            sys.exit()
    
    def notFoundKnn(self):
        self.notMsgBox.exec_()
        if self.notMsgBox.clickedButton() == self.notMsgBoxBtnYes:
            self.startVideoCapture()    
            
        elif self.notMsgBox.clickedButton() == self.notMsgBoxBtnNo:
            self.reset()    
        return
    
    def notFoundPass(self):
        self.notMsgBox.exec_()
        if self.notMsgBox.clickedButton() == self.notMsgBoxBtnYes:
            self.userVerify()
        elif self.notMsgBox.clickedButton() == self.notMsgBoxBtnNo:
            #self.notMsgBox.close()
            self.reset()
    
#-----------------------------------------------------------------------


class workingThread(QtCore.QThread):
    
    def __init__(self, parent=None):
        super(workingThread, self).__init__(parent)
    
    def run(self):
        
        for i in range(5):
            print("good thread")
            time.sleep(2)
    
class Thread(QtCore.QThread):

    def run(self):
        print("started")
        
        return
    
        
#-----------------------------------------------------------------------


class Ui_newUser(object):
    
    #save = QtCore.Signal(int)
    def setupUi(self, newUser):
        newUser.setObjectName("newUser")
        newUser.resize(400, 170)
        newUser.setMinimumSize(QtCore.QSize(400, 170))
        newUser.setMaximumSize(QtCore.QSize(400, 170))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        newUser.setWindowIcon(icon)
        newUser.setStyleSheet("QLabel{color:red}\n"
"QDialog{background-color:#383838 ;}")
        self.newUserName = QtGui.QLineEdit(newUser)
        self.newUserName.setGeometry(QtCore.QRect(60, 50, 271, 40))
        self.newUserName.setMinimumSize(QtCore.QSize(271, 40))
        self.newUserName.setMaximumSize(QtCore.QSize(271, 40))
        self.newUserName.setStyleSheet(" border: 1px solid ;\n"
"    border-radius: 10px;\n"
"border-color:#ff6c00;\n"
"background-color:white;")
        self.newUserName.setObjectName("newUserName")
        self.newUserName.setMaxLength(4)
        self.newUserLabel = QtGui.QLabel(newUser)
        self.newUserLabel.setGeometry(QtCore.QRect(40, 10, 323, 31))
        self.newUserLabel.setMinimumSize(QtCore.QSize(323, 31))
        self.newUserLabel.setMaximumSize(QtCore.QSize(291, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.newUserLabel.setFont(font)
        self.newUserLabel.setStyleSheet("color:#ff6c00;background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;")
        self.newUserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newUserLabel.setObjectName("newUserLabel")
        self.newUserSaveBtn = QtGui.QPushButton(newUser)
        self.newUserSaveBtn.setGeometry(QtCore.QRect(120, 110, 49, 45))
        self.newUserSaveBtn.setMinimumSize(QtCore.QSize(49, 45))
        self.newUserSaveBtn.setMaximumSize(QtCore.QSize(49, 45))
        self.newUserSaveBtn.setStyleSheet("QPushButton{background-color: transparent;\n"
"    background: none;\n"
"    background-repeat: none;\n"
"    border:none;}\n"
"    ")
        self.newUserSaveBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newUserSaveBtn.setIcon(icon1)
        self.newUserSaveBtn.setIconSize(QtCore.QSize(45, 45))
        self.newUserSaveBtn.setObjectName("newUserSaveBtn")
        self.newUserSaveBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.newUserCnlBtn = QtGui.QPushButton(newUser)
        self.newUserCnlBtn.setGeometry(QtCore.QRect(220, 110, 49, 45))
        self.newUserCnlBtn.setMinimumSize(QtCore.QSize(49, 45))
        self.newUserCnlBtn.setMaximumSize(QtCore.QSize(49, 45))
        self.newUserCnlBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.newUserCnlBtn.setStyleSheet("QPushButton{background-color: transparent;\n"
"    background: none;\n"
"    background-repeat: none;\n"
"    border:none;}\n"
"    \n"
"    ")
        self.newUserCnlBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/FVR/Icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newUserCnlBtn.setIcon(icon2)
        self.newUserCnlBtn.setIconSize(QtCore.QSize(45, 45))
        self.newUserCnlBtn.setObjectName("newUserCnlBtn")

        self.retranslateUi(newUser)
        QtCore.QMetaObject.connectSlotsByName(newUser)
        
        
        
        self.newUserCnlBtn.clicked.connect(newUser.close)
        self.newUserSaveBtn.clicked.connect(self.acceptPass)
        self.newUserSaveBtn.clicked.connect(newUser.close)
        

    def retranslateUi(self, newUser):
        newUser.setWindowTitle(QtGui.QApplication.translate("newUser", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.newUserLabel.setText(QtGui.QApplication.translate("newUser", "Press a personal code", None, QtGui.QApplication.UnicodeUTF8))
        self.newUserSaveBtn.setToolTip(QtGui.QApplication.translate("newUser", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.newUserCnlBtn.setToolTip(QtGui.QApplication.translate("newUser", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
    
    
    def acceptPass(self):
        global pin
        pin = self.newUserName.text()
        if pin:
            print(pin)
                
        return 

def openPassWindow():
    newUser = QtGui.QDialog()
    ui = Ui_newUser()
    ui.setupUi(newUser)
    #newUser.show()
    newUser.exec_()
    #newUser.close()
    return

#-----------------------------------------------------------------------

                              

#-----------------------------------------------------------------------

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_mainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())