# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fuelometer(object):
    def setupUi(self, Fuelometer):
        Fuelometer.setObjectName("Fuelometer")
        Fuelometer.resize(535, 113)
        Fuelometer.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(Fuelometer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setDate(QtCore.QDate(2018, 12, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        Fuelometer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fuelometer)
        QtCore.QMetaObject.connectSlotsByName(Fuelometer)

    def retranslateUi(self, Fuelometer):
        _translate = QtCore.QCoreApplication.translate
        Fuelometer.setWindowTitle(_translate("Fuelometer", "Fuelometer"))
        self.pushButton.setText(_translate("Fuelometer", "Insert"))
        self.pushButton_2.setText(_translate("Fuelometer", "Plot"))
        self.label.setText(_translate("Fuelometer", "Date"))
        self.label_2.setText(_translate("Fuelometer", "Mileage"))
        self.label_3.setText(_translate("Fuelometer", "Gallons"))
        self.label_4.setText(_translate("Fuelometer", "Price"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fuelometer = QtWidgets.QMainWindow()
    ui = Ui_Fuelometer()
    ui.setupUi(Fuelometer)
    Fuelometer.show()
    sys.exit(app.exec_())

