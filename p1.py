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
        upi=Upi()
        widget.addWidget(upi)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def hotrpays(self):
        otrs=Otrs()
        widget.addWidget(otrs)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def hbot(self):
        bot=Bot()
        widget.addWidget(bot)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def hacb(self):
        acb=acb()
        widget.addWidget(acb)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def hactrans(self):
        actrsns=Actrans()
        widget.addWidget(actrsns)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class Actrsns(QDialog):
    def __init__(self):
        super(Actrsns,self).__init__()
        loadUi("",self)
class Acb(QDialog):
    def __init__(self):
        super(Acb,self).__init__()
        loadUi("home.ui",self)
class Bot(QDialog):
    def __init__(self):
        super(Bot,self).__init__()
        loadUi("home.ui",self)
class Otrs(QDialog):
    def __init__(self):
        super(Otrs,self).__init__()
        loadUi("home.ui",self)
class Upi(QDialog):
    def __init__(self):
        super(Upi,self).__init__()
        loadUi("upip5.ui",self)
class Intro(QDialog):
    def __init__(self):
        super(Intro,self).__init__()
        loadUi("logo.ui",self)
        self.logo.clicked.connect(self.hpushButton)

    def hpushButton(self):
        hsubmit=Submit()
        widget.addWidget(hsubmit)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        

app=QApplication(sys.argv)
mainwindow=Intro()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(800)
widget.setFixedWidth(775)
widget.show()

app.exec()
