# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydlbot.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    cont = 0
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
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_3.addWidget(self.listWidget)
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
        self.addtext.returnPressed.connect(self.listWidget.reset)
        self.pushButton_5.pressed.connect(self.listWidget.clearSelection)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.puta)
        #self.addtext.returnPressed.connect()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def puta(self):
        self.cont = self.cont + 1
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(self.cont)
        text = self.addtext.text()
        item.setText(text)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pydlbot"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Quit"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit"))
        self.pushButton_3.setText(_translate("MainWindow", "Download now"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "flash"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

