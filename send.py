# -*- coding: utf-8 -*-

#form implementation generated from reading ui file 'send.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import paho.mqtt.client as mqtt
from threading import Thread
import os
import urlparse
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1365, 763)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelImg = QtWidgets.QLabel(self.centralwidget)
        self.labelImg.setGeometry(QtCore.QRect(10, 0, 1341, 241))
        self.labelImg.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.labelImg.setText("")
        self.labelImg.setPixmap(QtGui.QPixmap("shoutout.png"))
        self.labelImg.setObjectName("labelImg")
        self.labelNotice = QtWidgets.QLabel(self.centralwidget)
        self.labelNotice.setGeometry(QtCore.QRect(470, 60, 451, 111))
        self.labelNotice.setStyleSheet("font: 72pt \"AR DELANEY\";")
        self.labelNotice.setObjectName("labelNotice")
        self.textEditTypeMsg = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditTypeMsg.setGeometry(QtCore.QRect(13, 246, 1331, 471))
        self.textEditTypeMsg.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.textEditTypeMsg.setObjectName("textEditTypeMsg")
        self.pushButtonSend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend.setGeometry(QtCore.QRect(620, 660, 151, 51))
        self.pushButtonSend.setStyleSheet("font: 87 22pt \"Arial Black\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButtonSend.setObjectName("pushButtonSend")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1365, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E Notice Board"))
        self.labelNotice.setText(_translate("MainWindow", "NOTICE"))
        self.pushButtonSend.setText(_translate("MainWindow", "SEND"))
        self.pushButtonSend.clicked.connect(self.send)
        
    def publish(self):
        NOTICE = self.textEdit.toPlainText()
        noticeText = "%1"+NOTICE+"%2"
        mqttc.send(topic, noticeText)
        
    def on_connect(client, userdata, flags, rc):
        print("rc:Connected " + str(rc))
    
    def on_publish(client, obj, mid):
        print("mid:Notice Successfuly Send " + str(mid))
        
        mqttc = mqtt.Client()
        mqttc.on_connect = on_connect
        mqttc.on_publish = on_publish
        
        
        topic = 'notice'

        mqttc.username_pw_set("your_username", "your_password")
        mqttc.connect("your_hostname", "your_port")

        mqttc.subscribe(topic, 0)
        
def sqImport(tId):
    if tId == 0:
        while 1:
            rc = 0
            while rc == 0:
                rc = mqttc.loop()
                print("rc: " + str(rc))
    
    if tId == 1:
        while 1:
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
                
threadA = Thread(target = sqImport, args=[0])
threadB = Thread(target = sqImport, args=[1])
threadA.start()
threadB.start()
# Do work indepedent of loopA and loopB 
threadA.join()
threadB.join()
