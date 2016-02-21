from PyQt5 import QtCore, QtGui, QtWidgets


def addItem(self):
    addRow(self)
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