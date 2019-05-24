# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stiffener.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Stiffener(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(317, 231)
        self.txt_stiffnrHeight = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrHeight.setGeometry(QtCore.QRect(179, 27, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrHeight.setFont(font)
        self.txt_stiffnrHeight.setReadOnly(True)
        self.txt_stiffnrHeight.setObjectName("txt_stiffnrHeight")
        self.plateHeight = QtWidgets.QLabel(Dialog)
        self.plateHeight.setGeometry(QtCore.QRect(9, 27, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plateHeight.setFont(font)
        self.plateHeight.setObjectName("plateHeight")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(9, 70, 85, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_stiffnrLength = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrLength.setGeometry(QtCore.QRect(179, 70, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrLength.setFont(font)
        self.txt_stiffnrLength.setReadOnly(True)
        self.txt_stiffnrLength.setObjectName("txt_stiffnrLength")
        self.label_163 = QtWidgets.QLabel(Dialog)
        self.label_163.setGeometry(QtCore.QRect(9, 110, 104, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_163.setFont(font)
        self.label_163.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_163.setObjectName("label_163")
        self.txt_stiffnrThickness = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrThickness.setGeometry(QtCore.QRect(179, 110, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrThickness.setFont(font)
        self.txt_stiffnrThickness.setReadOnly(True)
        self.txt_stiffnrThickness.setObjectName("txt_stiffnrThickness")
        self.txt_stiffnrThickness_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrThickness_2.setGeometry(QtCore.QRect(180, 150, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrThickness_2.setFont(font)
        self.txt_stiffnrThickness_2.setReadOnly(True)
        self.txt_stiffnrThickness_2.setObjectName("txt_stiffnrThickness_2")
        self.label_164 = QtWidgets.QLabel(Dialog)
        self.label_164.setGeometry(QtCore.QRect(10, 150, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_164.setFont(font)
        self.label_164.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_164.setObjectName("label_164")
        self.txt_stiffnrThickness_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_stiffnrThickness_3.setGeometry(QtCore.QRect(180, 190, 118, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_stiffnrThickness_3.setFont(font)
        self.txt_stiffnrThickness_3.setReadOnly(True)
        self.txt_stiffnrThickness_3.setObjectName("txt_stiffnrThickness_3")
        self.label_165 = QtWidgets.QLabel(Dialog)
        self.label_165.setGeometry(QtCore.QRect(10, 190, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_165.setFont(font)
        self.label_165.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_165.setObjectName("label_165")
        self.txt_stiffnrHeight.raise_()
        self.plateHeight.raise_()
        self.label_2.raise_()
        self.txt_stiffnrLength.raise_()
        self.label_163.raise_()
        self.txt_stiffnrThickness.raise_()
        self.txt_stiffnrThickness_2.raise_()
        self.txt_stiffnrThickness_3.raise_()
        self.label_165.raise_()
        self.label_164.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stiffener"))
        self.plateHeight.setText(_translate("Dialog", "Height (mm)"))
        self.label_2.setText(_translate("Dialog", "Length (mm)"))
        self.label_163.setText(_translate("Dialog", "<html><head/><body><p>Thickness (mm)</p></body></html>"))
        self.label_164.setText(_translate("Dialog", "<html><head/><body><p>Moment demand (kNm)</p></body></html>"))
        self.label_165.setText(_translate("Dialog", "<html><head/><body><p>Moment capacity (kNm)</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

