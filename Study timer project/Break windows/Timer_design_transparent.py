# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Timer_design_transparent.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 364)
        self.SaveButton = QtWidgets.QPushButton(Dialog)
        self.SaveButton.setGeometry(QtCore.QRect(130, 270, 81, 41))
        self.SaveButton.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(66, 91, 255, 50);\n"
"border-radius: 15;")
        self.SaveButton.setObjectName("SaveButton")
        self.Work = QtWidgets.QPushButton(Dialog)
        self.Work.setGeometry(QtCore.QRect(310, 270, 81, 41))
        self.Work.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(66, 91, 255, 40);\n"
"border-radius: 15;")
        self.Work.setObjectName("Work")
        self.Clock = QtWidgets.QLCDNumber(Dialog)
        self.Clock.setGeometry(QtCore.QRect(140, 40, 241, 91))
        self.Clock.setStyleSheet("background-color: rgba(66, 91, 255, 70);\n"
"border-radius: 10;")
        self.Clock.setObjectName("Clock")
        self.Background = QtWidgets.QWidget(Dialog)
        self.Background.setGeometry(QtCore.QRect(10, 10, 441, 341))
        self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.057, y1:0.943182, x2:0.857955, y2:0.125, stop:0 rgba(250, 75, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 15;")
        self.Background.setObjectName("Background")
        self.BreakTool = QtWidgets.QToolButton(Dialog)
        self.BreakTool.setGeometry(QtCore.QRect(320, 140, 51, 21))
        self.BreakTool.setStyleSheet("background-color: rgba(66, 91, 255, 0);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.BreakTool.setObjectName("BreakTool")
        self.HideTool = QtWidgets.QToolButton(Dialog)
        self.HideTool.setGeometry(QtCore.QRect(240, 240, 41, 21))
        self.HideTool.setStyleSheet("background-color: rgba(66, 91, 255, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.HideTool.setObjectName("HideTool")
        self.SavedSessions = QtWidgets.QPushButton(Dialog)
        self.SavedSessions.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.SavedSessions.setStyleSheet("border-image: url(:/newPrefix/Save_button_pic.png);\n"
"background:transparent")
        self.SavedSessions.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Save_button_pic.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SavedSessions.setIcon(icon)
        self.SavedSessions.setIconSize(QtCore.QSize(40, 40))
        self.SavedSessions.setObjectName("SavedSessions")
        self.Summary = QtWidgets.QPushButton(Dialog)
        self.Summary.setGeometry(QtCore.QRect(30, 70, 31, 41))
        self.Summary.setStyleSheet("border-image: url(:/newPrefix/SummaryButton.png);")
        self.Summary.setText("")
        self.Summary.setObjectName("Summary")
        self.Theme = QtWidgets.QPushButton(Dialog)
        self.Theme.setGeometry(QtCore.QRect(20, 120, 41, 41))
        self.Theme.setStyleSheet("border-image: url(:/newPrefix/Theme Button.png);")
        self.Theme.setText("")
        self.Theme.setObjectName("Theme")
        self.Settings = QtWidgets.QPushButton(Dialog)
        self.Settings.setGeometry(QtCore.QRect(20, 160, 51, 41))
        self.Settings.setStyleSheet("image: url(:/newPrefix/Settings Button.png);")
        self.Settings.setText("")
        self.Settings.setObjectName("Settings")
        self.Play = QtWidgets.QPushButton(Dialog)
        self.Play.setGeometry(QtCore.QRect(160, 180, 191, 51))
        self.Play.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(66, 91, 255, 50);\n"
"border-radius: 15;")
        self.Play.setObjectName("Play")
        self.Background.raise_()
        self.SaveButton.raise_()
        self.Work.raise_()
        self.Clock.raise_()
        self.BreakTool.raise_()
        self.HideTool.raise_()
        self.Summary.raise_()
        self.Theme.raise_()
        self.Settings.raise_()
        self.Play.raise_()
        self.SavedSessions.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SaveButton.setText(_translate("Dialog", "Save"))
        self.Work.setText(_translate("Dialog", "Work"))
        self.BreakTool.setText(_translate("Dialog", "Break"))
        self.HideTool.setText(_translate("Dialog", "Hide"))
        self.Play.setText(_translate("Dialog", "Play"))
#import image study timer_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
