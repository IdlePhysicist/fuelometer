# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_databaseViewer(object):
    def setupUi(self, databaseViewer):
        databaseViewer.setObjectName("databaseViewer")
        databaseViewer.resize(616, 346)
        self.centralwidget = QtWidgets.QWidget(databaseViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.showAllButton = QtWidgets.QRadioButton(self.centralwidget)
        self.showAllButton.setObjectName("showAllButton")
        self.gridLayout.addWidget(self.showAllButton, 1, 0, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 1, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 590, 286))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 591, 291))
        self.tableView.setObjectName("tableView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        databaseViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(databaseViewer)
        QtCore.QMetaObject.connectSlotsByName(databaseViewer)

    def retranslateUi(self, databaseViewer):
        _translate = QtCore.QCoreApplication.translate
        databaseViewer.setWindowTitle(_translate("databaseViewer", "Database "))
        self.showAllButton.setText(_translate("databaseViewer", "Show All"))
        self.deleteButton.setText(_translate("databaseViewer", "Delete Entry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    databaseViewer = QtWidgets.QMainWindow()
    ui = Ui_databaseViewer()
    ui.setupUi(databaseViewer)
    databaseViewer.show()
    sys.exit(app.exec_())

