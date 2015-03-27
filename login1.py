# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\user.ui'
#
# Created: Mon Mar 16 22:11:01 2015
# by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import os

from PySide import QtCore, QtGui
from PySide.QtGui import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        #login screen, checks user credentials
        def start():
            if self.lineEdit_usrname.text() == 'username' and self.lineEdit_psswrd.text() == 'password':
                os.system('checkbox1.py')
                QtCore.QCoreApplication.instance().quit()
                #print user, pwd
            else:
                QMessageBox.information(None, 'INVALID USER', 'Please try again...')

        Dialog.resize(400, 300)
        self.lineEdit_usrname = QtGui.QLineEdit(Dialog)
        self.lineEdit_usrname.setGeometry(QtCore.QRect(200, 120, 113, 20))
        #self.lineEdit_usrname.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_usrname.setObjectName("lineEdit_usrname")

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(13)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 170, 61, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit_psswrd = QtGui.QLineEdit(Dialog)
        self.lineEdit_psswrd.setGeometry(QtCore.QRect(200, 170, 113, 20))
        self.lineEdit_psswrd.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_psswrd.setObjectName("lineEdit_psswrd")

        self.btn_login = QtGui.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(160, 240, 91, 31))
        self.btn_login.setObjectName("btn_login")
        QtCore.QObject.connect(self.btn_login, QtCore.SIGNAL('clicked()'), start)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("Dialog", "All Things Come To Parse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "user name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "password:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_login.setText(QtGui.QApplication.translate("Dialog", "Log In", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

