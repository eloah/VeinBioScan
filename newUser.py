from PySide import *
import sys
import mainGui  

class Ui_newUser(object):
    
    #save = QtCore.Signal(int)
    def setupUi(self, newUser):
        newUser.setObjectName("newUser")
        newUser.resize(400, 170)
        newUser.setMinimumSize(QtCore.QSize(400, 170))
        newUser.setMaximumSize(QtCore.QSize(400, 170))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/veins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("/home/pi/Desktop/New/Finger-Vein Recognizer/Icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newUserCnlBtn.setIcon(icon2)
        self.newUserCnlBtn.setIconSize(QtCore.QSize(45, 45))
        self.newUserCnlBtn.setObjectName("newUserCnlBtn")

        self.retranslateUi(newUser)
        QtCore.QMetaObject.connectSlotsByName(newUser)
        
        
        
        self.newUserCnlBtn.clicked.connect(newUser.close)
        self.newUserSaveBtn.clicked.connect(speak)
        #self.save.connect(mainGui.done)
    def retranslateUi(self, newUser):
        newUser.setWindowTitle(QtGui.QApplication.translate("newUser", "Επιβεβαίωση", None, QtGui.QApplication.UnicodeUTF8))
        self.newUserLabel.setText(QtGui.QApplication.translate("newUser", "Πληκτρολογίστε τον προσωπικό κωδικό", None, QtGui.QApplication.UnicodeUTF8))
        self.newUserSaveBtn.setToolTip(QtGui.QApplication.translate("newUser", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.newUserCnlBtn.setToolTip(QtGui.QApplication.translate("newUser", "Ακύρωση", None, QtGui.QApplication.UnicodeUTF8))
    
    
    def acceptNewUser(self):
        self.save.emit(self.newUserName.text())
        
       

    

def openWindow():
    newUser = QtGui.QDialog()
    ui = Ui_newUser()
    ui.setupUi(newUser)
    newUser.show()
    newUser.exec_()
    #newUser.close()
    return

def speak():
    sp = Send()
    sp.speakPass.connect(mainGui.Ui_mainWindow.done)
    sp.speakPass.emit(newUser.Ui_newUser.newUserName.text())
    
