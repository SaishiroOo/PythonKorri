#!/usr/bin/env python

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import cv2

class MainApp(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.video_size = QSize(320, 240)
        self.setup_ui()
        self.setup_camera1()
        self.setup_camera2()
        self.setup_camera3()

    def setup_ui(self):
        """Initialize widgets.
        """
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)
        self.image2_label = QLabel()
        self.image2_label.setFixedSize(self.video_size)
       
        self.image3_label = QLabel()
        self.image3_label.setFixedSize(self.video_size)
     
        self.button = QPushButton("Quit")
        self.button1 = QPushButton("Camera 1")
        self.button2 = QPushButton("Camera 2")
        self.button3 = QPushButton("Camera 3")
        self.button4 = QPushButton("Tous les Cameras")
        self.button.clicked.connect(self.close)
        self.button1.clicked.connect(self.camera1)
        self.button2.clicked.connect(self.camera2)
        self.button3.clicked.connect(self.camera3)
        self.button4.clicked.connect(self.allCam)


        self.Hlayout = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()
        self.Hlayout3 = QHBoxLayout()
        self.main_layout = QVBoxLayout()
        self.Hlayout.addWidget(self.image_label)
        self.Hlayout.addWidget(self.image2_label)
        self.Hlayout2.addWidget(self.image3_label)
        self.Hlayout3.addWidget(self.button1)
        self.Hlayout3.addWidget(self.button2)
        self.Hlayout3.addWidget(self.button3)
        self.Hlayout3.addWidget(self.button4)
        self.main_layout.addLayout(self.Hlayout)
        self.main_layout.addLayout(self.Hlayout2)
        self.main_layout.addLayout(self.Hlayout3)
        self.main_layout.addWidget(self.button)

        self.setLayout(self.main_layout)

    def setup_camera1(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture("http://admin:admin@192.168.5.143/video.cgi")
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)
    
    def setup_camera2(self):
        """Initialize camera.
        """
        self.capture2 = cv2.VideoCapture("http://admin:admin@192.168.5.165/video.cgi")
        self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)
    
    def setup_camera3(self):
        """Initialize camera.
        """
        self.capture3 = cv2.VideoCapture("http://admin:admin@192.168.5.153/video.cgi")
        self.capture3.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture3.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(image))


        _, frame2 = self.capture2.read()
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        image2 = QImage(frame2, frame2.shape[1], frame2.shape[0], 
                       frame2.strides[0], QImage.Format_RGB888)
        self.image2_label.setPixmap(QPixmap.fromImage(image2))


        _, frame3 = self.capture3.read()
        frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
        image3 = QImage(frame3, frame3.shape[1], frame3.shape[0], 
                       frame3.strides[0], QImage.Format_RGB888)
        self.image3_label.setPixmap(QPixmap.fromImage(image3))

    def camera1(self):

        self.image_label.show()
        self.image2_label.hide()
        self.image3_label.hide()
    
    def camera2(self):
        
        self.image_label.hide()
        self.image2_label.show()
        self.image3_label.hide()
    
    def camera3(self):

        self.image_label.hide()
        self.image2_label.hide()
        self.image3_label.show()
    
    def allCam(self):

        self.image_label.show()
        self.image2_label.show()
        self.image3_label.show()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())