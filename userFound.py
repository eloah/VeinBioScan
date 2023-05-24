from PySide import QtCore, QtGui

class Ui_userFound(object):
    def setupUi(self, userFound):
        userFound.setObjectName("userFound")
        userFound.resize(400, 170)
        userFound.setMinimumSize(QtCore.QSize(400, 170))
        userFound.setMaximumSize(QtCore.QSize(400, 170))
        userFound.setWindowTitle("Ο χρήστης βρέθηκε!")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        userFound.setWindowIcon(icon)
        userFound.setStyleSheet("QLabel{color:red}\n"
"QDialog{background-color:#383838 ;}")
        self.userFoundOkBtn = QtGui.QPushButton(userFound)
        self.userFoundOkBtn.setGeometry(QtCore.QRect(180, 110, 49, 45))
        self.userFoundOkBtn.setMinimumSize(QtCore.QSize(49, 45))
        self.userFoundOkBtn.setMaximumSize(QtCore.QSize(49, 45))
        self.userFoundOkBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.userFoundOkBtn.setStyleSheet("QPushButton{background-color: transparent;\n"
"    background: none;\n"
"    background-repeat: none;\n"
"    border:none;}\n"
"    ")
        self.userFoundOkBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userFoundOkBtn.setIcon(icon1)
        self.userFoundOkBtn.setIconSize(QtCore.QSize(45, 45))
        self.userFoundOkBtn.setObjectName("userFoundOkBtn")
        self.photoView = QtGui.QLabel(userFound)
        self.photoView.setGeometry(QtCore.QRect(30, 20, 81, 81))
        self.photoView.setText("")
        self.photoView.setObjectName("photoView")
        self.nameView = QtGui.QLabel(userFound)
        self.nameView.setGeometry(QtCore.QRect(130, 20, 241, 81))
        self.nameView.setText("")
        self.nameView.setAlignment(QtCore.Qt.AlignCenter)
        self.nameView.setObjectName("nameView")

        self.retranslateUi(userFound)
        QtCore.QMetaObject.connectSlotsByName(userFound)

        self.userFoundOkBtn.clicked.connect(userFound.close)
        

    def retranslateUi(self, userFound):
        self.userFoundOkBtn.setToolTip(QtGui.QApplication.translate("userFound", "Ok!", None, QtGui.QApplication.UnicodeUTF8))
    
    def showUser(self):
        global name
        if name:
            self.nameView.setText(""+str(name)+"")
            img = '/home/pi/Desktop/New/Finger-Vein Recognizer/Images/'+str(name)+'.png'
            img = QtGui.QImage(img)
            self.photoView.setPixmap(QtGui.QPixmap.fromImage(img)) 
        return
         
def openFoundWindow():
    
    userFound = QtGui.QDialog()
    ui = Ui_userFound()
    ui.setupUi(userFound)
    #userFound.show()
    userFound.exec_()
    #userFound.close()
    
    return 
