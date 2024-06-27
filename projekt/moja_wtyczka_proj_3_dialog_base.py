# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moja_wtyczka_proj_3_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Projekt_3DialogBase(object):
    def setupUi(self, Projekt_3DialogBase):
        Projekt_3DialogBase.setObjectName("Projekt_3DialogBase")
        Projekt_3DialogBase.resize(604, 368)
        self.button_box = QtWidgets.QDialogButtonBox(Projekt_3DialogBase)
        self.button_box.setGeometry(QtCore.QRect(380, 430, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(Projekt_3DialogBase)
        self.label.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Projekt_3DialogBase)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.label_2 = QtWidgets.QLabel(Projekt_3DialogBase)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 231, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Projekt_3DialogBase)
        self.label_3.setGeometry(QtCore.QRect(470, 40, 55, 20))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(Projekt_3DialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(400, 70, 191, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Projekt_3DialogBase)
        self.pushButton.setGeometry(QtCore.QRect(400, 310, 191, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Projekt_3DialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 191, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Projekt_3DialogBase)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 191, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Projekt_3DialogBase)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 371, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Projekt_3DialogBase)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 341, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Projekt_3DialogBase)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 320, 271, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Projekt_3DialogBase)
        self.button_box.accepted.connect(Projekt_3DialogBase.accept)
        self.button_box.rejected.connect(Projekt_3DialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(Projekt_3DialogBase)
   
    def retranslateUi(self, Projekt_3DialogBase):
        _translate = QtCore.QCoreApplication.translate
        Projekt_3DialogBase.setWindowTitle(_translate("Projekt_3DialogBase", "Wtyczka do Qgis"))
        self.label.setText(_translate("Projekt_3DialogBase", "Polecenie:"))
        self.radioButton_4.setText(_translate("Projekt_3DialogBase", "metry kwadratowe"))
        self.radioButton_3.setText(_translate("Projekt_3DialogBase", "ary"))
        self.radioButton_5.setText(_translate("Projekt_3DialogBase", "hektary"))
        self.label_2.setText(_translate("Projekt_3DialogBase", "Wybór jednostek pola powierchnii:"))
        self.label_3.setText(_translate("Projekt_3DialogBase", "Wyniki:"))
        self.pushButton.setText(_translate("Projekt_3DialogBase", "Wyczyść okno"))
        self.pushButton_2.setText(_translate("Projekt_3DialogBase", "Oblicz przewyższenie"))
        self.pushButton_3.setText(_translate("Projekt_3DialogBase", "Oblicz pole powierzchni"))
        self.label_4.setText(_translate("Projekt_3DialogBase", "Przeliczanie różnicy wysokości między punktami PKT1 a PKT2:"))
        self.label_5.setText(_translate("Projekt_3DialogBase", "Obliczanie pola powierzchnii metodą Gaussa:"))
        self.pushButton_4.setText(_translate("Projekt_3DialogBase", "Pokaż liczbe zaznaczonych obiektów"))

