# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designFichierClients.ui',
# licensing of 'designFichierClients.ui' applies.
#
# Created: Mon Jul 22 16:04:22 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(989, 675)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWClients = QtWidgets.QListWidget(Form)
        self.listWClients.setObjectName("listWClients")
        self.verticalLayout.addWidget(self.listWClients)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.editName = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editName.sizePolicy().hasHeightForWidth())
        self.editName.setSizePolicy(sizePolicy)
        self.editName.setMinimumSize(QtCore.QSize(400, 0))
        self.editName.setObjectName("editName")
        self.horizontalLayout.addWidget(self.editName)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.editPrenom = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editPrenom.sizePolicy().hasHeightForWidth())
        self.editPrenom.setSizePolicy(sizePolicy)
        self.editPrenom.setMinimumSize(QtCore.QSize(400, 0))
        self.editPrenom.setObjectName("editPrenom")
        self.horizontalLayout_2.addWidget(self.editPrenom)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lTel = QtWidgets.QLabel(Form)
        self.lTel.setEnabled(True)
        self.lTel.setObjectName("lTel")
        self.horizontalLayout_3.addWidget(self.lTel)
        self.editTel = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editTel.sizePolicy().hasHeightForWidth())
        self.editTel.setSizePolicy(sizePolicy)
        self.editTel.setMinimumSize(QtCore.QSize(400, 0))
        self.editTel.setObjectName("editTel")
        self.horizontalLayout_3.addWidget(self.editTel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pBModif = QtWidgets.QPushButton(Form)
        self.pBModif.setObjectName("pBModif")
        self.horizontalLayout_4.addWidget(self.pBModif)
        self.pBAjout = QtWidgets.QPushButton(Form)
        self.pBAjout.setObjectName("pBAjout")
        self.horizontalLayout_4.addWidget(self.pBAjout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Liste Clients", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Nom :", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Prénom :", None, -1))
        self.lTel.setText(QtWidgets.QApplication.translate("Form", "Téléphone :", None, -1))
        self.pBModif.setText(QtWidgets.QApplication.translate("Form", "Modifier", None, -1))
        self.pBAjout.setText(QtWidgets.QApplication.translate("Form", "Ajouter", None, -1))
