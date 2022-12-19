# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopwatch.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 110, 561, 111))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(200, 270, 89, 25))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStop = QtWidgets.QPushButton(Dialog)
        self.pushButtonStop.setGeometry(QtCore.QRect(300, 270, 89, 25))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.pushButtonReset = QtWidgets.QPushButton(Dialog)
        self.pushButtonReset.setGeometry(QtCore.QRect(200, 310, 89, 25))
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.pushButtonPause = QtWidgets.QPushButton(Dialog)
        self.pushButtonPause.setGeometry(QtCore.QRect(300, 310, 89, 25))
        self.pushButtonPause.setObjectName("pushButtonPause")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonStart.setText(_translate("Dialog", "START"))
        self.pushButtonStop.setText(_translate("Dialog", "STOP"))
        self.pushButtonReset.setText(_translate("Dialog", "RESET"))
        self.pushButtonPause.setText(_translate("Dialog", "PAUSE"))
