import pydlbot_ui as Ui
import UiLogic as uilog
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    while True:
    	app = QtWidgets.QApplication(sys.argv)
    	MainWindow = QtWidgets.QMainWindow()
    	ui = Ui.Ui_MainWindow()
    	ui.setupUi(MainWindow)
    	MainWindow.show()
    	ui.add.clicked.connect(uilog.addItem(ui))