import sys
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QLabel,QHBoxLayout,QMessageBox, QWidget)

class Calculatrice(QDialog):

    def __init__(self, parent=None):
        super(Calculatrice, self).__init__(parent)
        # Create widgets
        # self.setWindowTitle('BTS SNIR2')
        self.label1 = QLabel("1er nombre  :")
        self.label2 = QLabel("2eme nombre :")
        self.label3 = QLabel("La sommes des deux nombre :")
        self.label4 = QLabel("...")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        
        self.button = QPushButton("Calculer")
        self.button2 = QPushButton("Effacer")
        self.button3 = QPushButton("Quitter")
        # Create layout and add widgets
        layoutVer = QVBoxLayout()
        layoutHor1 = QHBoxLayout()
        layoutHor2 = QHBoxLayout()
        layoutHor3 = QHBoxLayout()
        layoutHor4 = QHBoxLayout()
        layoutHor5 = QHBoxLayout()

        layoutHor1.addWidget(self.label1)
        layoutHor1.addWidget(self.edit1)

        layoutHor2.addWidget(self.label2)
        layoutHor2.addWidget(self.edit2)

        layoutHor3.addWidget(self.button)
        layoutHor3.addWidget(self.button2)

        layoutHor4.addWidget(self.label3)
        layoutHor4.addWidget(self.label4)

        layoutHor5.addWidget(self.button3)

        # layoutVer.addWidget(self.edit2)
        layoutVer.addLayout(layoutHor1)
        layoutVer.addLayout(layoutHor2)
        layoutVer.addLayout(layoutHor3)
        layoutVer.addLayout(layoutHor4)
        layoutVer.addLayout(layoutHor5)
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

    # Greets the user
    def Calculer(self):

        nb1= int(self.edit1.text())
        nb2= int(self.edit2.text())
        somme = str(nb1+nb2)
        self.label4.setText(somme)    

    def Effacer(self):

        self.edit1.setText("")
        self.edit2.setText("")
        self.label4.setText("...")      

    

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Calculatrice()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
