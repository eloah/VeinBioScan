from PySide import QtCore, QtGui

class Ui_Reference(object):
    def setupUi(self, Reference):
        Reference.setObjectName("Reference")
        Reference.resize(1000, 600)
        Reference.setMinimumSize(QtCore.QSize(1000, 600))
        Reference.setStyleSheet("QDialog {background-color:#383838 ;}\n"
"QToolTip{padding:1px;}")
        self.projectReference = QtGui.QLabel(Reference)
        self.projectReference.setGeometry(QtCore.QRect(0, 0, 991, 71))
        self.projectReference.setStyleSheet("color:#ff6c00;background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"font-size: 32px")
        self.projectReference.setAlignment(QtCore.Qt.AlignCenter)
        self.projectReference.setObjectName("projectReference")
        self.groupBox = QtGui.QGroupBox(Reference)
        self.groupBox.setGeometry(QtCore.QRect(40, 80, 921, 391))
        self.groupBox.setStyleSheet("QGroupBox{border: 1px solid;\n"
"border-radius:10px;\n"
"border-color:#ff6c00;\n"
"color:#ff6c00;\n"
"background-color: transparent;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtGui.QWidget(Reference)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 501, 1001, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"    background: none;\n"
"    border: none;\n"
"    background-repeat: none;\n"
"    ")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Reference)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Reference.close)
        QtCore.QMetaObject.connectSlotsByName(Reference)

        self.refWindow = QtGui.QDialog()

    def retranslateUi(self, Reference):
        Reference.setWindowTitle(QtGui.QApplication.translate("Reference", "Πληροφορίες ", None, QtGui.QApplication.UnicodeUTF8))
        self.projectReference.setText(QtGui.QApplication.translate("Reference", "Πληροφορίες ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("Reference", "Κλείσιμο", None, QtGui.QApplication.UnicodeUTF8))




def openWindow():
    refWindow = QtGui.QDialog()
    ui = Ui_Reference()
    ui.setupUi(refWindow)
    refWindow.show()
    refWindow.exec_()
    refWindow.close()
