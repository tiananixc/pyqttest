# -*- coding: utf-8 -*- 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import time

class Test(QDialog):
    def __init__(self,parent=None):
        super(Test,self).__init__(parent)
        self.listFile=QListWidget()
        self.btnStart=QPushButton('Start')
        layout=QGridLayout(self)
        layout.addWidget(self.listFile,0,0,1,2)
        layout.addWidget(self.btnStart,1,1)
        self.connect(self.btnStart,SIGNAL('clicked()'),self.slotAdd)
    def slotAdd(self):
        self.listFile.addItem('321+')
        QApplication.processEvents()
        time.sleep(1)
def main():

    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()