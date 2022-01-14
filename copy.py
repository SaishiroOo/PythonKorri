import sys
import sqlite3
from typing import Text
import webbrowser
from PySide6.QtWidgets import (QDateEdit, QComboBox, QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QLabel, QHBoxLayout, QMessageBox, QWidget)

conn = sqlite3.connect("important.db")
c = conn.cursor()
c.execute(
"""
CREATE TABLE IF NOT EXISTS personne
(
    username text,
    prenom text,
    nom text,
    login text,
    password text,
    birthday text,
    gender text
            
)
""")

conn.commit()
conn.close()

class Connexion(QDialog):

    def __init__(self, parent=None):
        super(Connexion, self).__init__(parent)
        # Create widgets

        self.setWindowTitle('Connexion')
        self.label1 = QLabel("Welcome")
        self.label2 = QLabel("Log In or Create a new account")
              
        self.button = QPushButton("Log In")
        self.button2 = QPushButton("Create a new account")
        self.button3 = QPushButton("Exit")
        
        self.PageLogin = Login(self)
        self.PageCreate = SignUp(self)
        
        # Create layout and add widgets

        layoutVer = QVBoxLayout()

        layoutVer.addWidget(self.label1)
        layoutVer.addWidget(self.label2)
        layoutVer.addWidget(self.button)
        layoutVer.addWidget(self.button2)
        layoutVer.addWidget(self.button3)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.Login)
        self.button2.clicked.connect(self.Create)
        self.button3.clicked.connect(self.close)

    # Greets the user
    def Login(self):

        self.PageLogin.exec() 

    def Create(self):

        self.PageCreate.exec()    

class Login(QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        # Create widgets

        self.setWindowTitle('Login')
        self.label1 = QLabel("Log In")
        self.label2 = QLabel("Log In to your existing account")
        self.label3 = QLabel("Username")
        self.label4 = QLabel("Password")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()

        self.edit2.setEchoMode((QLineEdit.Password))
        
        self.button = QPushButton("Log In")

        # Create layout and add widgets

        layoutVer = QVBoxLayout()

        layoutVer.addWidget(self.label1)
        layoutVer.addWidget(self.label2)
        layoutVer.addWidget(self.label3)
        layoutVer.addWidget(self.edit1)
        layoutVer.addWidget(self.label4)
        layoutVer.addWidget(self.edit2)
        layoutVer.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.Login)

    # Greets the user
    def Login(self):

        pass

class SignUp(QDialog):

    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent)
        # Create widgets

        self.setWindowTitle('Sign up')
        self.label1 = QLabel("Sign up")
        self.label2 = QLabel("Create new account now")
        self.label3 = QLabel("Username")
        self.label4 = QLabel("Password")
        self.label5 = QLabel("Confirm Password")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()   

        self.edit2.setEchoMode((QLineEdit.Password))
        self.edit3.setEchoMode((QLineEdit.Password))
        
        self.button = QPushButton("Sign up")

        self.Submit = Submit(self)

        # Create layout and add widgets

        layoutVer = QVBoxLayout()

        layoutVer.addWidget(self.label1)
        layoutVer.addWidget(self.label2)
        layoutVer.addWidget(self.label3)
        layoutVer.addWidget(self.edit1)
        layoutVer.addWidget(self.label4)
        layoutVer.addWidget(self.edit2)
        layoutVer.addWidget(self.label5)
        layoutVer.addWidget(self.edit3)
        layoutVer.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.Sign)

    # Greets the user
    def Sign(self):

        if(self.edit1.text()=="" or self.edit2.text()=="" or self.edit3.text()==""):
            self.edit1.setText("")
            self.edit2.setText("") 
            self.edit3.setText("")
        else:
            if(self.edit2.text() == self.edit3.text):
                conn = sqlite3.connect("important.db")
                c = conn.cursor()

                c.execute("""INSERT INTO personne (username,password)  VALUES(?, ?)""", (self.edit1.text(), self.edit2.text()))
                self.Submit.exec()

                conn.commit()
                conn.close()

class Submit(QDialog):

    def __init__(self, parent=None):
        super(Submit, self).__init__(parent)
        # Create widgets

        self.setWindowTitle('Submit')
        self.label1 = QLabel("Fill profile")
        self.label2 = QLabel("Set up your profile by completing these fields")
        self.label3 = QLabel("UserName")
        self.label4 = QLabel("LastName")
        self.label5 = QLabel("FirstName")
        self.label6 = QLabel("BirthDay")
        self.label7 = QLabel("Gender")

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QDateEdit()
        self.edit5 = QComboBox()
        
        self.button = QPushButton("Submit")

        self.edit5.addItem("F")
        self.edit5.addItem("M")
        self.edit5.addItem("N/A")

        # Create layout and add widgets

        layoutVer1 = QVBoxLayout()
        layoutVer2 = QVBoxLayout()
        layoutVer3 = QVBoxLayout()
        layoutHor = QHBoxLayout()

        layoutVer1.addWidget(self.label3)
        layoutVer1.addWidget(self.edit1)
        layoutVer1.addWidget(self.label4)
        layoutVer1.addWidget(self.edit2)
        layoutVer1.addWidget(self.label5)
        layoutVer1.addWidget(self.edit3)

        layoutVer2.addWidget(self.label6)
        layoutVer2.addWidget(self.edit4)
        layoutVer2.addWidget(self.label7)
        layoutVer2.addWidget(self.edit5)

        layoutVer3.addWidget(self.label1)
        layoutVer3.addWidget(self.label2)

        layoutHor.addLayout(layoutVer1)
        layoutHor.addLayout(layoutVer2)
        layoutVer3.addLayout(layoutHor)
        layoutVer3.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layoutVer3)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.Submit)

    # Greets the user
    def Submit(self):

        conn = sqlite3.connect("important.db")
        c = conn.cursor()

        c.execute("""UPDATE personne SET nom = ?, prenom = ? WHERE username = ? """, (self.edit2.text(), self.edit3.text(),self.edit1.text()))

        conn.commit()
        conn.close()

class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Create widgets

        self.setWindowTitle('Secret Window')
        self.label1 = QLabel("Welcome")
        self.label2 = QLabel("Ultra High Secret window")

        self.button = QPushButton("Open website")
        self.button2 = QPushButton("Exit")

        self.Page1 = Connexion(self)

        # Create layout and add widgets

        layoutVer = QVBoxLayout()

        layoutVer.addWidget(self.label1)
        layoutVer.addWidget(self.label2)
        layoutVer.addWidget(self.button)
        layoutVer.addWidget(self.button2)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.Open)
        self.button2.clicked.connect(self.Exit)

    # Greets the user
    def Open(self):

        webbrowser.open("https://snirpy.github.io/site/")

    def Exit(self):

        self.Page1.exec()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Connexion()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
