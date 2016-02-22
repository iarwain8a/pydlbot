# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydlbot.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    rows = 2
    cols = 2
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addtext = QtWidgets.QLineEdit(self.centralwidget)
        self.addtext.setObjectName("addtext")
        self.horizontalLayout.addWidget(self.addtext)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 100, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 70)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(self.cols)
        self.tableWidget.setRowCount(self.rows)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add.clicked.connect(self.addItem)
        if (self.addtext.text() != ""):
            self.puta()

    def puta(self):
        item = self.tableWidget.item(self.rows-2, 0)
        item.setText("puta")

    def addItem(self):
        self.addRow()
        text = self.addtext.text()
        item = self.tableWidget.item(self.rows-2, 0)
        item.setText(text)
        item = self.tableWidget.item(self.rows-2, 1)
        #item.setText(text)
    
    def addRow(self):
        self.rows = self.rows + 1
        self.tableWidget.setRowCount(self.rows)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(self.rows-2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(self.rows-2, 1, item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pydlbot"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Quit"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit"))
        self.pushButton_3.setText(_translate("MainWindow", "Download now"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "file name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Download every"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "flash"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "week"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

