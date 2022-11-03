from select import select
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
class Submit(QDialog):
    def __init__(self):
        super(Submit,self).__init__()
        loadUi("home.ui",self)
        self.upip.clicked.connect(self.hupip)
        self.otrpays.clicked.connect(self.hotrpays)
        self.actrans.clicked.connect(self.hactrans)
        self.acb.clicked.connect(self.hacb)
        self.bot.clicked.connect(self.hbot)
    def hupip(self):
        volunteerPage=Submit()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)
app=QApplication(sys.argv)
mainwindow=Submit()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(680)
widget.setFixedWidth(720)
widget.show()

app.exec()
