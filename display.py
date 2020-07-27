# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be loss
import paho.mqtt.Client as mqtt
from urllib.parse import urlparse
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
from threading import Thread
import sys
import re
import os

icon = "shoutout.png"
NOTICE = "NOTICE"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 956)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelImg = QtWidgets.QLabel(self.centralwidget)
        self.labelImg.setGeometry(QtCore.QRect(10, 0, 1341, 231))
        self.labelImg.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.labelImg.setText("")
        self.labelImg.setPixmap(QtGui.QPixmap("shoutout.png"))
        self.labelImg.setObjectName("labelImg")
        self.label_2Notice = QtWidgets.QLabel(self.centralwidget)
        self.label_2Notice.setGeometry(QtCore.QRect(480, 60, 481, 111))
        self.label_2Notice.setStyleSheet("font: 72pt \"AR DELANEY\";")
        self.label_2Notice.setObjectName("label_2Notice")
        self.label_3Display = QtWidgets.QLabel(self.centralwidget)
        self.label_3Display.setGeometry(QtCore.QRect(10, 245, 1341, 651))
        self.label_3Display.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.label_3Display.setText("")
        self.label_3Display.setObjectName("label_3Display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1359, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.start(3000)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notice Board"))
        self.label_2Notice.setText(_translate("MainWindow", "NOTICE"))
        
    def _update(self):
        MainWindow = QtWidgets.QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notice Board"))
        self.label_2Notice.setText(_translate("MainWindow", "NOTICE"))
        
    def on_connect(client, userdata, flags, rc):
        print("rc: " + str(rc))    
        
    def on_message(client, obj, msg):
        print(str(msg.payload) )
        if(str(msg.payload) ):
           noticeReceived = str(msg.payload)
           result = re.search('%1(.*)%2', noticeReceived)
           
           global NOTICE
           NOTICE = result.group(1)
           
    def on_publish(client, obj, mid):
       print("mid:Successful " + str(mid))

    def on_subscribe(client, obj, mid, granted_qos):
       print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(client, obj, level, string):
       print(string)
       
       mqttc = mqtt.Client()
       mqttc.on_message = on_message
       mqttc.on_connect = on_connect
       mqttc.on_publish = on_publish
       mqttc.on_subscribe = on_subscribe
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
                threadA.join()
                threadB.join()

       
        
    