# -*- coding: utf-8 -*-

"""
a QtGui.QInputDialog dialog. 
"""

import sys,getinfo
from PyQt4 import QtGui
from PyQt4 import QtCore
import _mssql
import uuid
import decimal

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.li = QtGui.QLineEdit(self)
        self.li.setGeometry(20,10,200,20)

        self.btn = QtGui.QPushButton(u'搜索描述 GO！', self)
        self.btn.move(230, 10)
        #self.btn.clicked.connect(self.showdes)
        self.btn2 = QtGui.QPushButton(u'搜索价格 GO！', self)
        self.btn2.move(330, 10)
        #self.btn2.clicked.connect(self.showpri)

        self.liba = QtGui.QLabel(self)
        self.liba.setGeometry(20,40,430,20)
        #self.connect(self.li, QtCore.SIGNAL('textChanged(QString)'),self.tech)
        self.bk = QtGui.QTextEdit(self)
        self.bk.setGeometry(20,70,430,180)

        self.bkl = QtGui.QLabel(self)
        self.bkl.setGeometry(470,40,430,20)

        self.bkt = QtGui.QTextEdit(self)
        self.bkt.setGeometry(470,70,430,180)

        self.liba2 = QtGui.QLabel(self)
        self.liba2.setGeometry(20,250,430,20)

        self.le = QtGui.QTextEdit(self)
        self.le.setGeometry(20,270,430,300)

        self.libd = QtGui.QLabel(self)
        self.libd.setGeometry(470,250,430,20)

        self.lebd = QtGui.QTextEdit(self)
        self.lebd.setGeometry(470,270,430,300)

        self.resize(920, 580)
        self.setWindowTitle(u'酒价格查询软件 By Tian')
        self.center()
        self.show()

    def center(self):  #主窗口居中显示函数

        screen=QtGui.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

print __name__
if __name__ == '__main__':
    main()