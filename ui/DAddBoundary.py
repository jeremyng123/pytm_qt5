# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dadd_boundary.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DAddBoundary(object):
    def setupUi(self, DAddBoundary):
        DAddBoundary.setObjectName("DAddBoundary")
        DAddBoundary.resize(400, 200)
        self.layoutWidget = QtWidgets.QWidget(DAddBoundary)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 341, 163))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.allComponents = QtWidgets.QListWidget(self.layoutWidget)
        self.allComponents.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.allComponents.setProperty("showDropIndicator", False)
        self.allComponents.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.allComponents.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.allComponents.setObjectName("allComponents")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.allComponents)

        self.retranslateUi(DAddBoundary)
        self.buttonBox.accepted.connect(DAddBoundary.accept)
        self.buttonBox.rejected.connect(DAddBoundary.reject)
        QtCore.QMetaObject.connectSlotsByName(DAddBoundary)

    def retranslateUi(self, DAddBoundary):
        _translate = QtCore.QCoreApplication.translate
        DAddBoundary.setWindowTitle(_translate("DAddBoundary", "Dialog"))
        self.label.setText(_translate("DAddBoundary", "Name"))
        self.label_2.setText(_translate("DAddBoundary", "Components"))
        self.allComponents.setSortingEnabled(True)

