import pydlbot_ui as Ui
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import threading

if __name__ == '__main__':
	p = threading.Thread(target=main)
        p.start()
        for i in range(3):
                t = threading.Thread(target=f,args=(i,))
                t.start()

def main():
	app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def f(id):
    print ("thread function",id)
    return
