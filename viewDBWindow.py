# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_viewDB(object):
    def setupUi(self, viewDB):
        viewDB.setObjectName("viewDB")
        viewDB.resize(576, 278)
        self.gridLayout = QtWidgets.QGridLayout(viewDB)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(viewDB)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 550, 218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 551, 221))
        self.tableView.setObjectName("tableView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(viewDB)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.deleteEntryButton = QtWidgets.QPushButton(viewDB)
        self.deleteEntryButton.setObjectName("deleteEntryButton")
        self.gridLayout.addWidget(self.deleteEntryButton, 1, 1, 1, 1)

        self.retranslateUi(viewDB)
        QtCore.QMetaObject.connectSlotsByName(viewDB)

    def retranslateUi(self, viewDB):
        _translate = QtCore.QCoreApplication.translate
        viewDB.setWindowTitle(_translate("viewDB", "View Database"))
        self.checkBox.setText(_translate("viewDB", "Show All"))
        self.deleteEntryButton.setText(_translate("viewDB", "Delete Entry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewDB = QtWidgets.QDialog()
    ui = Ui_viewDB()
    ui.setupUi(viewDB)
    viewDB.show()
    sys.exit(app.exec_())
