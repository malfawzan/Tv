import sys

import setuptools.windows_support
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from remotcontrol import *
from PyQt5.uic import loadUi


class Controller(QMainWindow, Ui_remotcontrol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.ui = Ui_remotcontrol
        self.setupUi(self)



        self.Button_Power.clicked.connect(lambda: self.power())
        self.Button_mute.clicked.connect(lambda: self.mute())
        self.Button_Netflix.clicked.connect(lambda: self.netflix())
        self.Button_sing.clicked.connect(lambda: self.sing())
        self.Button_hulu.clicked.connect(lambda: self.hulu())
        self.Button_Vudu.clicked.connect(lambda: self.vudu())
        self.Button_Right.clicked.connect(lambda: self.right())
        self.Button_Left.clicked.connect(lambda: self.left())
        self.Button_Down.clicked.connect(lambda: self.down())
        self.Button_Up.clicked.connect(lambda: self.up())
        self.Button_Home.clicked.connect(lambda: self.home())


    def netflix(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("netflix.img.jpg"))
    def hulu(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("hulu.img.jpg"))

    def sing(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("sing.img.jpg"))

    def vudu(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("Vudu3.png"))

    def home(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("home.img.jpg"))

    def right(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("cnn.img.png"))

    def left(self):
        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("fox.png"))

    def power(self):

        self.imglabel.setScaledContents(True)
        self.imglabel.setPixmap(QtGui.QPixmap("power.jpg"))

    def down(self):
        self.label.setScaledContents(True)
        self.label.setPixmap(QtGui.QPixmap("volumedown.png"))

    def up(self):
        self.label.setScaledContents(True)
        self.label.setPixmap(QtGui.QPixmap("volumeup.png"))

    def mute(self):
        self.label.setScaledContents(True)
        self.label.setPixmap(QtGui.QPixmap("volumemute.png"))


