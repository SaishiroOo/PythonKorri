from sys import float_repr_style
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (QLineEdit, QMainWindow, QPushButton, QApplication,QRadioButton,QGroupBox,
    QVBoxLayout,QLabel,QHBoxLayout, QWidget)

class Camera(QMainWindow):

    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.add_layouts_to_layouts()
        self.setup_connections()
        self.create_main_window()

    def create_main_window(self):   

        self.setWindowTitle('Video_calculate')
        self.size()

        self.setWindowIcon(QtGui.QIcon(r'C:\Users\snir\Documents\CodagePythonBTSSNIR2/Camera_p.ico'))

        self.widget = QWidget()
        self.widget.setLayout(self.layout_main)
        self.setCentralWidget(self.widget)

    def create_layouts(self):

        self.layoutVer1 = QVBoxLayout()
        self.layoutVer2 = QVBoxLayout()
        self.layoutVer3 = QVBoxLayout()
        self.layoutVer4 = QVBoxLayout()

        self.layoutHor1 = QHBoxLayout()
        self.layoutHor2 = QHBoxLayout()
        self.layoutHor3 = QHBoxLayout()
        self.layoutHor4 = QHBoxLayout()
        self.layoutHor5 = QHBoxLayout()
        self.layoutHor6 = QHBoxLayout()

        self.layout_main = QVBoxLayout()

    def add_widgets_to_layouts(self):

        self.layoutHor1.addWidget(self.radio)
        self.layoutHor1.addWidget(self.radio2)

        self.layoutHor2.addWidget(self.label1)
        self.layoutHor2.addWidget(self.edit1)

        self.layoutHor3.addWidget(self.label2)
        self.layoutHor3.addWidget(self.edit2)

        self.layoutHor4.addWidget(self.label3)
        self.layoutHor4.addWidget(self.edit3)

        self.layoutHor5.addWidget(self.label8)

        self.layoutHor6.addWidget(self.button)
        self.layoutHor6.addWidget(self.button2)

        self.layoutVer1.addWidget(self.label4)
        self.layoutVer1.addWidget(self.edit4)

        self.layoutVer2.addWidget(self.label5)
        self.layoutVer2.addWidget(self.edit5)

        self.layoutVer3.addWidget(self.label6)
        self.layoutVer3.addWidget(self.edit6)

        self.layoutVer4.addWidget(self.label7)
        self.layoutVer4.addWidget(self.edit7)

    def add_layouts_to_layouts(self):

        self.layout_main.addLayout(self.layoutHor1)
        self.layout_main.addLayout(self.layoutHor2)
        self.layout_main.addLayout(self.layoutHor3) 
        self.layout_main.addLayout(self.layoutHor4) 

        self.layoutHor5.addLayout(self.layoutVer1) 
        self.layoutHor5.addLayout(self.layoutVer2)
        self.layoutHor5.addLayout(self.layoutVer3)
        self.layoutHor5.addLayout(self.layoutVer4)   
        
        self.layout_main.addLayout(self.layoutHor5)
        self.layout_main.addLayout(self.layoutHor6)


    def create_widgets(self):

        self.label1 = QLabel("Taille")
        self.label2 = QLabel("ips")
        self.label3 = QLabel("Hdd")
        self.label4 = QLabel("Jour")
        self.label5 = QLabel("Heures")
        self.label6 = QLabel("Minutes")
        self.label7 = QLabel("Secondes")
        self.label8 = QLabel("Durée")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()
        self.edit7 = QLineEdit()

        self.edit4.setDisabled(True)
        self.edit5.setDisabled(True)
        self.edit6.setDisabled(True)
        self.edit7.setDisabled(True)

        self.button = QPushButton("Calculer")
        self.button2 = QPushButton("Exit")
        self.radio = QRadioButton("Durée")
        self.radio.setChecked(True)
        self.radio.toggled.connect(self.choix)
        self.radio2 = QRadioButton("HDD")

    def setup_connections(self):

        self.button.clicked.connect(self.Calculer)
        self.button2.clicked.connect(self.close)
        self.radio.clicked.connect(self.choix)
        self.radio2.clicked.connect(self.choix2)
        validator= QRegularExpressionValidator(QRegularExpression("[0-9-.]+"))
        self.edit1.setValidator(validator)
        self.edit2.setValidator(validator)
        self.edit3.setValidator(validator)
        self.edit4.setValidator(validator)
        self.edit5.setValidator(validator)
        self.edit6.setValidator(validator)
        self.edit7.setValidator(validator)


    def Calculer(self):

        if(self.radio.toggled):

            taille_i= int(self.edit1.text())
            ips= int(self.edit2.text())
            taille_s= float(self.edit3.text())

            duree = ((taille_s*(1024*1024))/(taille_i*ips))

            jour = duree / 86400%100
            heure= duree / 3600%24
            minute= duree / 60%60
            sec= duree % 60

        if(self.radio2.toggled):

            jour= int(self.edit4.text())
            heure= int(self.edit5.text())
            minute= int(self.edit6.text())
            sec= int(self.edit7.text())

            jour = jour*86400
            heure = heure*3600
            minute = minute*60
            duree=jour+heure+minute+sec

            taille_s=(taille_i*ips*duree)/(1024*1024)
            self.edit3.setText(taille_s)

    def choix(self):

        self.edit3.setDisabled(False)

        self.edit4.setDisabled(True)
        self.edit5.setDisabled(True)
        self.edit6.setDisabled(True)
        self.edit7.setDisabled(True)

    def choix2(self):

        self.edit3.setDisabled(True)

        self.edit4.setDisabled(False)
        self.edit5.setDisabled(False)
        self.edit6.setDisabled(False)
        self.edit7.setDisabled(False)

appli = QApplication([])
mon_window = Camera()
mon_window.show()
appli.exec()