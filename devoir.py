import sys
from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,QRadioButton,QGroupBox,
    QVBoxLayout, QDialog,QLabel,QHBoxLayout,QMessageBox, QWidget)

class Camera(QDialog):

    def __init__(self, parent=None):
        super(Camera, self).__init__(parent)
        # Create widgets
        self.setWindowTitle('Video_calculate')
        self.label1 = QLabel("Taille")
        self.label2 = QLabel("ips")
        self.label3 = QLabel("Hdd")
        self.label4 = QLabel("Jour")
        self.label5 = QLabel("Heures")
        self.label6 = QLabel("Minutes")
        self.label7 = QLabel("Secondes")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()
        self.edit7 = QLineEdit()

        
        self.button = QPushButton("Calculer")
        self.button2 = QPushButton("Exit")
        self.radio = QRadioButton("Durée")
        self.radio2 = QRadioButton("HDD")
        # Create layout and add widgets
        layoutVer1 = QVBoxLayout()
        layoutVer2 = QVBoxLayout()
        layoutVer3 = QVBoxLayout()
        layoutVer4 = QVBoxLayout()
        layoutVer5 = QVBoxLayout()
        layoutVer6 = QVBoxLayout()
        layoutHor1 = QHBoxLayout()
        layoutHor2 = QHBoxLayout()
        layoutHor3 = QHBoxLayout()
        layoutHor4 = QHBoxLayout()
        layoutHor5 = QHBoxLayout()

        layoutHor1.addWidget(self.label1)
        layoutHor1.addWidget(self.edit1)

        layoutHor2.addWidget(self.label2)
        layoutHor2.addWidget(self.edit2)

        layoutHor3.addWidget(self.label3)
        layoutHor3.addWidget(self.edit3)

        layoutHor4.addWidget(self.label3)
        layoutHor4.addWidget(self.label4)

        layoutHor5.addWidget(self.button3)

        # layoutVer.addWidget(self.edit2)
        layoutVer1.addLayout(layoutHor1)
        layoutVer2.addLayout(layoutHor2)
        layoutVer3.addLayout(layoutHor3)
        layoutVer4.addLayout(layoutHor4)
        layoutVer5.addLayout(layoutHor5)
        layoutVer6.addLayout(layoutHor5)
        # layoutVer.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.Calculer)
        self.button2.clicked.connect(self.Effacer)
        self.button3.clicked.connect(self.close)
        self.messagebox = QMessageBox()
        self.messagebox.setText("Erreur de synthaxe")
        validator= QRegularExpressionValidator(QRegularExpression("[0-9]+"))
        self.edit1.setValidator(validator)
        self.edit2.setValidator(validator)
