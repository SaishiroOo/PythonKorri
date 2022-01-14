import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QLabel,QHBoxLayout,QMessageBox)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        # self.setWindowTitle('BTS SNIR2')
        self.label1 = QLabel("Login  : ")
        self.label2 = QLabel("Passwod:")
        self.label3 = QLabel("Déconnecté")

        self.edit1 = QLineEdit("")
        self.edit1.setPlaceholderText("Enter Username Here")
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("Enter Password Here")
        self.edit2.setEchoMode((QLineEdit.Password))
        
        self.button = QPushButton("Se connecter")
        self.button2 = QPushButton("Se déconnecter")
        self.button2.hide()
        # Create layout and add widgets
        layoutVer = QVBoxLayout()
        layoutHor1 = QHBoxLayout()
        layoutHor2 = QHBoxLayout()
        layoutHor3 = QHBoxLayout()

        layoutHor1.addWidget(self.label1)
        layoutHor1.addWidget(self.edit1)

        layoutHor2.addWidget(self.label2)
        layoutHor2.addWidget(self.edit2)

        layoutHor3.addWidget(self.button)
        layoutHor3.addWidget(self.button2)



        # layoutVer.addWidget(self.edit2)
        layoutVer.addLayout(layoutHor1)
        layoutVer.addLayout(layoutHor2)
        layoutVer.addLayout(layoutHor3)
        # layoutVer.addWidget(self.button)
        layoutVer.addWidget(self.label3)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.seConnecter)
        self.button2.clicked.connect(self.seDeconnecter)
        self.messagebox = QMessageBox()
        self.messagebox.setText("Erreur de connexion")

    # Greets the user
    def seConnecter(self):
        if self.edit1.text() == "ilyas" and self.edit2.text() == "pass":
        # print(f"Hello {self.edit1.text()}")
            self.label3.setText("Connecté")
            # self.button.setText("Se déconnecter")
            self.edit1.setPlaceholderText("Enter Username Here")
            self.edit2.setPlaceholderText("Enter Password Here")
            # self.button.hide()
            self.label1.hide()
            self.label2.hide()
            self.edit1.hide()
            self.edit2.hide()
            self.button2.show()
            
            
        else:
            self.edit1.setText("")
            self.edit2.setText("")
            self.messagebox.show()

    def seDeconnecter(self):
        
        # print(f"Hello {self.edit1.text()}")
        self.label3.setText("Décoonnecté")
        self.edit1.setText("")
        self.edit2.setText("")
        # self.edit1.setPlaceholderText("Enter Username Here")
        # self.edit2.setPlaceholderText("Enter Password Here") 
        # self.button.setText("Se déconnecter")

        self.label1.show()
        self.label2.show()
        self.edit1.show()
        self.edit2.show()
        self.button.show()
        # self.button2.hide()
        

            
            
            

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
