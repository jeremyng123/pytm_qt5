# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wdatastore.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Datastore(object):
    def setupUi(self, Datastore):
        Datastore.setObjectName("Datastore")
        Datastore.resize(400, 203)
        self.layoutWidget = QtWidgets.QWidget(Datastore)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 381, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(self.layoutWidget)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label2 = QtWidgets.QLabel(self.layoutWidget)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.boundaries = QtWidgets.QComboBox(self.layoutWidget)
        self.boundaries.setObjectName("boundaries")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.boundaries)
        self.label3 = QtWidgets.QLabel(self.layoutWidget)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.OS = QtWidgets.QComboBox(self.layoutWidget)
        self.OS.setObjectName("OS")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.OS.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.OS)
        self.label4 = QtWidgets.QLabel(self.layoutWidget)
        self.label4.setObjectName("label4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label4)
        self.isHardened = QtWidgets.QComboBox(self.layoutWidget)
        self.isHardened.setObjectName("isHardened")
        self.isHardened.addItem("")
        self.isHardened.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.isHardened)
        self.label5 = QtWidgets.QLabel(self.layoutWidget)
        self.label5.setObjectName("label5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label5)
        self.isSQL = QtWidgets.QComboBox(self.layoutWidget)
        self.isSQL.setObjectName("isSQL")
        self.isSQL.addItem("")
        self.isSQL.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.isSQL)
        self.label6 = QtWidgets.QLabel(self.layoutWidget)
        self.label6.setObjectName("label6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label6)
        self.inScope = QtWidgets.QComboBox(self.layoutWidget)
        self.inScope.setObjectName("inScope")
        self.inScope.addItem("")
        self.inScope.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inScope)

        self.retranslateUi(Datastore)
        QtCore.QMetaObject.connectSlotsByName(Datastore)

    def retranslateUi(self, Datastore):
        _translate = QtCore.QCoreApplication.translate
        Datastore.setWindowTitle(_translate("Datastore", "Form"))
        self.label1.setText(_translate("Datastore", "Name"))
        self.label2.setText(_translate("Datastore", "inBoundary"))
        self.label3.setText(_translate("Datastore", "OS"))
        self.OS.setItemText(0, _translate("Datastore", "Windows 10"))
        self.OS.setItemText(1, _translate("Datastore", "Windows 8"))
        self.OS.setItemText(2, _translate("Datastore", "Windows 7"))
        self.OS.setItemText(3, _translate("Datastore", "macOS"))
        self.OS.setItemText(4, _translate("Datastore", "Ubuntu"))
        self.OS.setItemText(5, _translate("Datastore", "CentOS"))
        self.OS.setItemText(6, _translate("Datastore", "Fedora"))
        self.OS.setItemText(7, _translate("Datastore", "Red Hat Linux"))
        self.OS.setItemText(8, _translate("Datastore", "Apple iOS"))
        self.OS.setItemText(9, _translate("Datastore", "Android"))
        self.label4.setText(_translate("Datastore", "isHardened"))
        self.isHardened.setItemText(0, _translate("Datastore", "True"))
        self.isHardened.setItemText(1, _translate("Datastore", "False"))
        self.label5.setText(_translate("Datastore", "isSQL"))
        self.isSQL.setItemText(0, _translate("Datastore", "True"))
        self.isSQL.setItemText(1, _translate("Datastore", "False"))
        self.label6.setText(_translate("Datastore", "inScope"))
        self.inScope.setItemText(0, _translate("Datastore", "True"))
        self.inScope.setItemText(1, _translate("Datastore", "False"))
