# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class Ui_Fuelometer(object):
    def setupUi(self, Fuelometer):
        Fuelometer.setObjectName("Fuelometer")
        Fuelometer.resize(537, 111)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/gas-pump-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Fuelometer.setWindowIcon(icon)
        Fuelometer.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(Fuelometer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.gridLayout.addWidget(self.label_date, 0, 0, 1, 1)
        self.label_mileage = QtWidgets.QLabel(self.centralwidget)
        self.label_mileage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mileage.setObjectName("label_mileage")
        self.gridLayout.addWidget(self.label_mileage, 0, 1, 1, 1)
        self.label_gallons = QtWidgets.QLabel(self.centralwidget)
        self.label_gallons.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gallons.setObjectName("label_gallons")
        self.gridLayout.addWidget(self.label_gallons, 0, 2, 1, 1)
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price.setObjectName("label_price")
        self.gridLayout.addWidget(self.label_price, 0, 3, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setDate(QtCore.QDate(datetime.date.today()))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.mileageEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mileageEdit.setClearButtonEnabled(False)
        self.mileageEdit.setObjectName("mileageEdit")
        self.gridLayout.addWidget(self.mileageEdit, 1, 1, 1, 1)
        self.fuelEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fuelEdit.setObjectName("fuelEdit")
        self.gridLayout.addWidget(self.fuelEdit, 1, 2, 1, 1)
        self.priceEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.priceEdit.setObjectName("priceEdit")
        self.gridLayout.addWidget(self.priceEdit, 1, 3, 1, 1)
        self.label_AM_Value = QtWidgets.QLabel(self.centralwidget)
        self.label_AM_Value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_AM_Value.setObjectName("label_AM_Value")
        self.gridLayout.addWidget(self.label_AM_Value, 2, 0, 1, 1)
        self.vDBButton = QtWidgets.QPushButton(self.centralwidget)
        self.vDBButton.setObjectName("vDBButton")
        self.gridLayout.addWidget(self.vDBButton, 2, 1, 1, 1)
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setDefault(False)
        self.plotButton.setFlat(False)
        self.plotButton.setObjectName("plotButton")
        self.gridLayout.addWidget(self.plotButton, 2, 2, 1, 1)
        self.insertButton = QtWidgets.QPushButton(self.centralwidget)
        self.insertButton.setObjectName("insertButton")
        self.gridLayout.addWidget(self.insertButton, 2, 3, 1, 1)
        Fuelometer.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fuelometer)
        QtCore.QMetaObject.connectSlotsByName(Fuelometer)
        Fuelometer.setTabOrder(self.mileageEdit, self.fuelEdit)
        Fuelometer.setTabOrder(self.fuelEdit, self.priceEdit)
        Fuelometer.setTabOrder(self.priceEdit, self.dateEdit)
        Fuelometer.setTabOrder(self.dateEdit, self.insertButton)
        Fuelometer.setTabOrder(self.insertButton, self.plotButton)

    def retranslateUi(self, Fuelometer):
        _translate = QtCore.QCoreApplication.translate
        Fuelometer.setWindowTitle(_translate("Fuelometer", "Fuelometer"))
        self.label_date.setText(_translate("Fuelometer", "Date"))
        self.label_mileage.setText(_translate("Fuelometer", "Mileage"))
        self.label_gallons.setText(_translate("Fuelometer", "Gallons"))
        self.label_price.setText(_translate("Fuelometer", "Price"))
        self.label_AM_Value.setText(_translate("Fuelometer", "TextLabel"))
        self.vDBButton.setText(_translate("Fuelometer", "View Database"))
        self.plotButton.setText(_translate("Fuelometer", "Plot"))
        self.insertButton.setText(_translate("Fuelometer", "Insert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fuelometer = QtWidgets.QMainWindow()
    ui = Ui_Fuelometer()
    ui.setupUi(Fuelometer)
    Fuelometer.show()
    sys.exit(app.exec_())
