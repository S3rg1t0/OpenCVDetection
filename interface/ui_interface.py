# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceFMWpvj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 741)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 60))
        self.groupBox.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.groupBox)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.comboBox_webcam = QComboBox(self.frame_9)
        self.comboBox_webcam.setObjectName(u"comboBox_webcam")
        self.comboBox_webcam.setMinimumSize(QSize(150, 0))
        self.comboBox_webcam.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_webcam)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_13 = QFrame(self.groupBox)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 20, 0)
        self.pushButton_start_webcam = QPushButton(self.frame_13)
        self.pushButton_start_webcam.setObjectName(u"pushButton_start_webcam")
        self.pushButton_start_webcam.setMinimumSize(QSize(0, 0))
        self.pushButton_start_webcam.setMaximumSize(QSize(50, 50))
        self.pushButton_start_webcam.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u":/iconos/btn_encender.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_start_webcam.setIcon(icon)
        self.pushButton_start_webcam.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_start_webcam)

        self.pushButton_stop_webcam = QPushButton(self.frame_13)
        self.pushButton_stop_webcam.setObjectName(u"pushButton_stop_webcam")
        self.pushButton_stop_webcam.setMaximumSize(QSize(50, 50))
        self.pushButton_stop_webcam.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/btn_apagar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_stop_webcam.setIcon(icon1)
        self.pushButton_stop_webcam.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_stop_webcam)


        self.horizontalLayout_4.addWidget(self.frame_13, 0, Qt.AlignLeft)

        self.frame_14 = QFrame(self.groupBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_cpu = QLabel(self.frame_14)
        self.label_cpu.setObjectName(u"label_cpu")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_cpu.setFont(font)

        self.gridLayout_5.addWidget(self.label_cpu, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_ram = QLabel(self.frame_14)
        self.label_ram.setObjectName(u"label_ram")
        self.label_ram.setFont(font)

        self.gridLayout_5.addWidget(self.label_ram, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_12.addLayout(self.gridLayout_5)


        self.horizontalLayout_4.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.groupBox)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_date = QLabel(self.frame_15)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font)

        self.verticalLayout_13.addWidget(self.label_date, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_time = QLabel(self.frame_15)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font)

        self.verticalLayout_13.addWidget(self.label_time, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.frame_15)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_9 = QGroupBox(self.frame_10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(0, 60))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.comboBox_selector = QComboBox(self.groupBox_9)
        self.comboBox_selector.setObjectName(u"comboBox_selector")

        self.verticalLayout_11.addWidget(self.comboBox_selector)


        self.verticalLayout_9.addWidget(self.groupBox_9)

        self.stackedWidget_selector = QStackedWidget(self.frame_10)
        self.stackedWidget_selector.setObjectName(u"stackedWidget_selector")
        self.stackedWidget_selector.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_selector.setFrameShadow(QFrame.Raised)
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayout_10 = QVBoxLayout(self.Page1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_detect_color = QFrame(self.Page1)
        self.frame_detect_color.setObjectName(u"frame_detect_color")
        self.frame_detect_color.setFrameShape(QFrame.StyledPanel)
        self.frame_detect_color.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_detect_color)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 20, 0, 30)
        self.groupBox_91 = QGroupBox(self.frame_detect_color)
        self.groupBox_91.setObjectName(u"groupBox_91")
        self.groupBox_91.setCursor(QCursor(Qt.SizeHorCursor))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_91)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.groupBox_91)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.groupBox_91)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 120))
        self.frame_12.setMaximumSize(QSize(16777215, 120))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.min_s = QSlider(self.frame_12)
        self.min_s.setObjectName(u"min_s")
        self.min_s.setMaximumSize(QSize(75, 16777215))
        self.min_s.setMaximum(255)
        self.min_s.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.min_s, 1, 0, 1, 1)

        self.min_h = QSlider(self.frame_12)
        self.min_h.setObjectName(u"min_h")
        self.min_h.setMaximumSize(QSize(75, 16777215))
        self.min_h.setStyleSheet(u"")
        self.min_h.setMaximum(255)
        self.min_h.setTracking(True)
        self.min_h.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.min_h, 0, 0, 1, 1)

        self.min_v = QSlider(self.frame_12)
        self.min_v.setObjectName(u"min_v")
        self.min_v.setMaximumSize(QSize(75, 16777215))
        self.min_v.setMaximum(255)
        self.min_v.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.min_v, 2, 0, 1, 1)

        self.label_min_h = QLabel(self.frame_12)
        self.label_min_h.setObjectName(u"label_min_h")

        self.gridLayout.addWidget(self.label_min_h, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_min_s = QLabel(self.frame_12)
        self.label_min_s.setObjectName(u"label_min_s")

        self.gridLayout.addWidget(self.label_min_s, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_min_v = QLabel(self.frame_12)
        self.label_min_v.setObjectName(u"label_min_v")

        self.gridLayout.addWidget(self.label_min_v, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.max_s = QSlider(self.frame_12)
        self.max_s.setObjectName(u"max_s")
        self.max_s.setMaximumSize(QSize(75, 16777215))
        self.max_s.setMaximum(255)
        self.max_s.setValue(255)
        self.max_s.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.max_s, 1, 0, 1, 1)

        self.max_h = QSlider(self.frame_12)
        self.max_h.setObjectName(u"max_h")
        self.max_h.setMaximumSize(QSize(75, 16777215))
        self.max_h.setMaximum(255)
        self.max_h.setValue(255)
        self.max_h.setTracking(True)
        self.max_h.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.max_h, 0, 0, 1, 1)

        self.max_v = QSlider(self.frame_12)
        self.max_v.setObjectName(u"max_v")
        self.max_v.setMaximumSize(QSize(75, 16777215))
        self.max_v.setMaximum(255)
        self.max_v.setValue(255)
        self.max_v.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.max_v, 2, 0, 1, 1)

        self.label_max_h = QLabel(self.frame_12)
        self.label_max_h.setObjectName(u"label_max_h")

        self.gridLayout_2.addWidget(self.label_max_h, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_max_s = QLabel(self.frame_12)
        self.label_max_s.setObjectName(u"label_max_s")

        self.gridLayout_2.addWidget(self.label_max_s, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_max_v = QLabel(self.frame_12)
        self.label_max_v.setObjectName(u"label_max_v")

        self.gridLayout_2.addWidget(self.label_max_v, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.verticalLayout_8.addWidget(self.groupBox_91)

        self.groupBox_10 = QGroupBox(self.frame_detect_color)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(0, 170))
        self.groupBox_10.setMaximumSize(QSize(16777215, 170))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dial_area_min = QDial(self.groupBox_10)
        self.dial_area_min.setObjectName(u"dial_area_min")
        self.dial_area_min.setMinimumSize(QSize(0, 90))
        self.dial_area_min.setMaximumSize(QSize(90, 90))
        self.dial_area_min.setStyleSheet(u"background-color: rgb(194, 255, 201);")
        self.dial_area_min.setMaximum(5000)
        self.dial_area_min.setSingleStep(10)
        self.dial_area_min.setValue(2500)
        self.dial_area_min.setNotchTarget(0.700000000000000)

        self.gridLayout_4.addWidget(self.dial_area_min, 1, 0, 1, 1)

        self.dial_area_max = QDial(self.groupBox_10)
        self.dial_area_max.setObjectName(u"dial_area_max")
        self.dial_area_max.setMinimumSize(QSize(0, 90))
        self.dial_area_max.setMaximumSize(QSize(90, 90))
        self.dial_area_max.setStyleSheet(u"background-color: rgb(255, 189, 156);")
        self.dial_area_max.setMaximum(10000)
        self.dial_area_max.setSingleStep(10)
        self.dial_area_max.setValue(5000)
        self.dial_area_max.setSliderPosition(5000)

        self.gridLayout_4.addWidget(self.dial_area_max, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_dial_area_min = QLabel(self.groupBox_10)
        self.label_dial_area_min.setObjectName(u"label_dial_area_min")

        self.gridLayout_4.addWidget(self.label_dial_area_min, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_dial_area_max = QLabel(self.groupBox_10)
        self.label_dial_area_max.setObjectName(u"label_dial_area_max")

        self.gridLayout_4.addWidget(self.label_dial_area_max, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_6.addLayout(self.gridLayout_4)


        self.verticalLayout_8.addWidget(self.groupBox_10)

        self.groupBox_3 = QGroupBox(self.frame_detect_color)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.radioButton_trayectoria_on = QRadioButton(self.groupBox_3)
        self.radioButton_trayectoria_on.setObjectName(u"radioButton_trayectoria_on")

        self.verticalLayout_17.addWidget(self.radioButton_trayectoria_on)

        self.radioButton_trayectoria_off = QRadioButton(self.groupBox_3)
        self.radioButton_trayectoria_off.setObjectName(u"radioButton_trayectoria_off")

        self.verticalLayout_17.addWidget(self.radioButton_trayectoria_off)


        self.verticalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_10.addWidget(self.frame_detect_color)

        self.stackedWidget_selector.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.verticalLayout_18 = QVBoxLayout(self.Page2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.Page2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_18)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.groupBox_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 5, 0, 5)
        self.radioButton_umbral = QRadioButton(self.frame_19)
        self.radioButton_umbral.setObjectName(u"radioButton_umbral")

        self.horizontalLayout_7.addWidget(self.radioButton_umbral)

        self.radioButton_adapative = QRadioButton(self.frame_19)
        self.radioButton_adapative.setObjectName(u"radioButton_adapative")

        self.horizontalLayout_7.addWidget(self.radioButton_adapative)


        self.verticalLayout_24.addWidget(self.frame_19)

        self.stackedWidget_umbral = QStackedWidget(self.groupBox_4)
        self.stackedWidget_umbral.setObjectName(u"stackedWidget_umbral")
        self.stackedWidget_umbral.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_umbral.setFrameShadow(QFrame.Raised)
        self.frame_umbral_normal = QWidget()
        self.frame_umbral_normal.setObjectName(u"frame_umbral_normal")
        self.gridLayout_6 = QGridLayout(self.frame_umbral_normal)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.slider_umbral_max = QSlider(self.frame_umbral_normal)
        self.slider_umbral_max.setObjectName(u"slider_umbral_max")
        self.slider_umbral_max.setMinimumSize(QSize(150, 0))
        self.slider_umbral_max.setMaximumSize(QSize(150, 16777215))
        self.slider_umbral_max.setMaximum(255)
        self.slider_umbral_max.setSliderPosition(255)
        self.slider_umbral_max.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.slider_umbral_max, 1, 0, 1, 1)

        self.slider_umbral_min = QSlider(self.frame_umbral_normal)
        self.slider_umbral_min.setObjectName(u"slider_umbral_min")
        self.slider_umbral_min.setMinimumSize(QSize(150, 0))
        self.slider_umbral_min.setMaximumSize(QSize(150, 16777215))
        self.slider_umbral_min.setMaximum(255)
        self.slider_umbral_min.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.slider_umbral_min, 0, 0, 1, 1)

        self.comboBox_umbral = QComboBox(self.frame_umbral_normal)
        self.comboBox_umbral.setObjectName(u"comboBox_umbral")
        self.comboBox_umbral.setMinimumSize(QSize(150, 0))
        self.comboBox_umbral.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.comboBox_umbral, 2, 0, 1, 1)

        self.stackedWidget_umbral.addWidget(self.frame_umbral_normal)
        self.page_umbral_adaptive = QWidget()
        self.page_umbral_adaptive.setObjectName(u"page_umbral_adaptive")
        self.verticalLayout_25 = QVBoxLayout(self.page_umbral_adaptive)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.page_umbral_adaptive)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.slider_max_adaptive_umbral = QSlider(self.frame_20)
        self.slider_max_adaptive_umbral.setObjectName(u"slider_max_adaptive_umbral")
        self.slider_max_adaptive_umbral.setOrientation(Qt.Horizontal)

        self.verticalLayout_26.addWidget(self.slider_max_adaptive_umbral)


        self.verticalLayout_25.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.page_umbral_adaptive)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_21)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.comboBox_umbral_2 = QComboBox(self.frame_21)
        self.comboBox_umbral_2.setObjectName(u"comboBox_umbral_2")

        self.gridLayout_7.addWidget(self.comboBox_umbral_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_21)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_21)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.comboBox_adaptive_umbral = QComboBox(self.frame_21)
        self.comboBox_adaptive_umbral.setObjectName(u"comboBox_adaptive_umbral")

        self.gridLayout_7.addWidget(self.comboBox_adaptive_umbral, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame_21)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 3, 0, 1, 1)

        self.comboBox_blocksize_umbral = QComboBox(self.frame_21)
        self.comboBox_blocksize_umbral.setObjectName(u"comboBox_blocksize_umbral")

        self.gridLayout_7.addWidget(self.comboBox_blocksize_umbral, 2, 1, 1, 1)

        self.comboBox_c_umbral = QComboBox(self.frame_21)
        self.comboBox_c_umbral.setObjectName(u"comboBox_c_umbral")

        self.gridLayout_7.addWidget(self.comboBox_c_umbral, 3, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_21)

        self.stackedWidget_umbral.addWidget(self.page_umbral_adaptive)

        self.verticalLayout_24.addWidget(self.stackedWidget_umbral, 0, Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_18)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.groupBox_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_22)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.comboBox_blur_types = QComboBox(self.frame_23)
        self.comboBox_blur_types.setObjectName(u"comboBox_blur_types")

        self.horizontalLayout_8.addWidget(self.comboBox_blur_types)


        self.verticalLayout_28.addWidget(self.frame_23, 0, Qt.AlignTop)

        self.stackedWidget_blur = QStackedWidget(self.frame_22)
        self.stackedWidget_blur.setObjectName(u"stackedWidget_blur")
        self.stackedWidget_blur.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_blur.setFrameShadow(QFrame.Raised)
        self.Page1_blur = QWidget()
        self.Page1_blur.setObjectName(u"Page1_blur")
        self.horizontalLayout_9 = QHBoxLayout(self.Page1_blur)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.Page1_blur)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_24)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.slider_kernel_blur = QSlider(self.frame_24)
        self.slider_kernel_blur.setObjectName(u"slider_kernel_blur")
        self.slider_kernel_blur.setMinimum(1)
        self.slider_kernel_blur.setMaximum(10)
        self.slider_kernel_blur.setOrientation(Qt.Horizontal)

        self.verticalLayout_29.addWidget(self.slider_kernel_blur)


        self.horizontalLayout_9.addWidget(self.frame_24)

        self.frame_28 = QFrame(self.Page1_blur)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_28)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_blur = QLabel(self.frame_28)
        self.label_blur.setObjectName(u"label_blur")
        self.label_blur.setMinimumSize(QSize(50, 0))

        self.verticalLayout_34.addWidget(self.label_blur)


        self.horizontalLayout_9.addWidget(self.frame_28)

        self.stackedWidget_blur.addWidget(self.Page1_blur)
        self.Page2_blur = QWidget()
        self.Page2_blur.setObjectName(u"Page2_blur")
        self.horizontalLayout_10 = QHBoxLayout(self.Page2_blur)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.Page2_blur)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_29)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(50)
        self.gridLayout_8.setVerticalSpacing(10)
        self.slider_sigma_gaussian_blur = QSlider(self.frame_29)
        self.slider_sigma_gaussian_blur.setObjectName(u"slider_sigma_gaussian_blur")
        self.slider_sigma_gaussian_blur.setMinimum(0)
        self.slider_sigma_gaussian_blur.setMaximum(100)
        self.slider_sigma_gaussian_blur.setValue(0)
        self.slider_sigma_gaussian_blur.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.slider_sigma_gaussian_blur, 1, 0, 1, 1)

        self.slider_kernel_gaussian_blur = QSlider(self.frame_29)
        self.slider_kernel_gaussian_blur.setObjectName(u"slider_kernel_gaussian_blur")
        self.slider_kernel_gaussian_blur.setMinimum(1)
        self.slider_kernel_gaussian_blur.setMaximum(10)
        self.slider_kernel_gaussian_blur.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.slider_kernel_gaussian_blur, 0, 0, 1, 1)

        self.label_gaussian_blur = QLabel(self.frame_29)
        self.label_gaussian_blur.setObjectName(u"label_gaussian_blur")
        self.label_gaussian_blur.setMinimumSize(QSize(50, 0))

        self.gridLayout_8.addWidget(self.label_gaussian_blur, 0, 1, 1, 1)

        self.label_sigma_gaussian_blur = QLabel(self.frame_29)
        self.label_sigma_gaussian_blur.setObjectName(u"label_sigma_gaussian_blur")
        self.label_sigma_gaussian_blur.setMinimumSize(QSize(50, 0))

        self.gridLayout_8.addWidget(self.label_sigma_gaussian_blur, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_8)


        self.horizontalLayout_10.addWidget(self.frame_29)

        self.stackedWidget_blur.addWidget(self.Page2_blur)
        self.Page3_blur = QWidget()
        self.Page3_blur.setObjectName(u"Page3_blur")
        self.verticalLayout_37 = QVBoxLayout(self.Page3_blur)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.Page3_blur)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_30)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(50)
        self.gridLayout_10.setVerticalSpacing(20)
        self.slider_kernel_medianblur = QSlider(self.frame_30)
        self.slider_kernel_medianblur.setObjectName(u"slider_kernel_medianblur")
        self.slider_kernel_medianblur.setMinimum(1)
        self.slider_kernel_medianblur.setMaximum(15)
        self.slider_kernel_medianblur.setSingleStep(2)
        self.slider_kernel_medianblur.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.slider_kernel_medianblur, 0, 0, 1, 1)

        self.label_medianblur = QLabel(self.frame_30)
        self.label_medianblur.setObjectName(u"label_medianblur")
        self.label_medianblur.setMinimumSize(QSize(50, 0))

        self.gridLayout_10.addWidget(self.label_medianblur, 0, 1, 1, 1)


        self.verticalLayout_38.addLayout(self.gridLayout_10)


        self.verticalLayout_37.addWidget(self.frame_30)

        self.stackedWidget_blur.addWidget(self.Page3_blur)

        self.verticalLayout_28.addWidget(self.stackedWidget_blur)


        self.verticalLayout_27.addWidget(self.frame_22)


        self.verticalLayout_19.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_18)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.groupBox_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_25)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, -1, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.radioButton_canny = QRadioButton(self.frame_26)
        self.radioButton_canny.setObjectName(u"radioButton_canny")

        self.horizontalLayout_11.addWidget(self.radioButton_canny)

        self.radioButton_2 = QRadioButton(self.frame_26)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_11.addWidget(self.radioButton_2)


        self.verticalLayout_32.addWidget(self.frame_26)

        self.stackedWidget_canny = QStackedWidget(self.frame_25)
        self.stackedWidget_canny.setObjectName(u"stackedWidget_canny")
        self.stackedWidget_canny.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_canny.setFrameShadow(QFrame.Raised)
        self.Page1_canny = QWidget()
        self.Page1_canny.setObjectName(u"Page1_canny")
        self.verticalLayout_35 = QVBoxLayout(self.Page1_canny)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.Page1_canny)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_27)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(50)
        self.gridLayout_9.setVerticalSpacing(10)
        self.slider_canny_umbral_alto = QSlider(self.frame_27)
        self.slider_canny_umbral_alto.setObjectName(u"slider_canny_umbral_alto")
        self.slider_canny_umbral_alto.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.slider_canny_umbral_alto, 0, 0, 1, 1)

        self.slider_canny_umbral_bajo = QSlider(self.frame_27)
        self.slider_canny_umbral_bajo.setObjectName(u"slider_canny_umbral_bajo")
        self.slider_canny_umbral_bajo.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.slider_canny_umbral_bajo, 1, 0, 1, 1)

        self.label_canny_umbral_alto = QLabel(self.frame_27)
        self.label_canny_umbral_alto.setObjectName(u"label_canny_umbral_alto")
        self.label_canny_umbral_alto.setMinimumSize(QSize(50, 0))

        self.gridLayout_9.addWidget(self.label_canny_umbral_alto, 0, 1, 1, 1)

        self.label_canny_umbral_bajo = QLabel(self.frame_27)
        self.label_canny_umbral_bajo.setObjectName(u"label_canny_umbral_bajo")
        self.label_canny_umbral_bajo.setMinimumSize(QSize(50, 0))

        self.gridLayout_9.addWidget(self.label_canny_umbral_bajo, 1, 1, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_9)


        self.verticalLayout_35.addWidget(self.frame_27)

        self.stackedWidget_canny.addWidget(self.Page1_canny)

        self.verticalLayout_32.addWidget(self.stackedWidget_canny)


        self.verticalLayout_31.addWidget(self.frame_25)


        self.verticalLayout_19.addWidget(self.groupBox_6)


        self.verticalLayout_18.addWidget(self.frame_18)

        self.stackedWidget_selector.addWidget(self.Page2)

        self.verticalLayout_9.addWidget(self.stackedWidget_selector)


        self.verticalLayout_7.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_img_principal = QLabel(self.frame_7)
        self.label_img_principal.setObjectName(u"label_img_principal")
        self.label_img_principal.setMinimumSize(QSize(500, 500))

        self.verticalLayout_23.addWidget(self.label_img_principal)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.spinBox_pruebas_contour = QSpinBox(self.frame_6)
        self.spinBox_pruebas_contour.setObjectName(u"spinBox_pruebas_contour")
        self.spinBox_pruebas_contour.setGeometry(QRect(10, 20, 51, 25))
        self.spinBox_pruebas_contour.setMinimumSize(QSize(0, 25))
        self.spinBox_pruebas_contour.setMaximumSize(QSize(150, 16777215))
        self.spinBox_pruebas_contour.setMinimum(-1)
        self.spinBox_pruebas_contour.setMaximum(10000)

        self.verticalLayout_2.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_4)

        self.stackedWidget_right = QStackedWidget(self.frame_2)
        self.stackedWidget_right.setObjectName(u"stackedWidget_right")
        self.stackedWidget_right.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget_right.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_right.setFrameShadow(QFrame.Raised)
        self.Page1_2 = QWidget()
        self.Page1_2.setObjectName(u"Page1_2")
        self.verticalLayout_14 = QVBoxLayout(self.Page1_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Page1_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.radioButton_sinTexto = QRadioButton(self.groupBox_2)
        self.radioButton_sinTexto.setObjectName(u"radioButton_sinTexto")

        self.verticalLayout_16.addWidget(self.radioButton_sinTexto)

        self.radioButton_textoArea = QRadioButton(self.groupBox_2)
        self.radioButton_textoArea.setObjectName(u"radioButton_textoArea")

        self.verticalLayout_16.addWidget(self.radioButton_textoArea)

        self.radioButton_textoCentro = QRadioButton(self.groupBox_2)
        self.radioButton_textoCentro.setObjectName(u"radioButton_textoCentro")

        self.verticalLayout_16.addWidget(self.radioButton_textoCentro)


        self.verticalLayout_15.addWidget(self.groupBox_2)


        self.verticalLayout_14.addWidget(self.frame)

        self.frame_16 = QFrame(self.Page1_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.Page1_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_17)

        self.stackedWidget_right.addWidget(self.Page1_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_20 = QVBoxLayout(self.page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_5)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.frame_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, 0, 0)
        self.label_img_umbral = QLabel(self.groupBox_7)
        self.label_img_umbral.setObjectName(u"label_img_umbral")

        self.verticalLayout_22.addWidget(self.label_img_umbral)


        self.verticalLayout_21.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.frame_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_img_blur = QLabel(self.groupBox_8)
        self.label_img_blur.setObjectName(u"label_img_blur")

        self.verticalLayout_30.addWidget(self.label_img_blur)


        self.verticalLayout_21.addWidget(self.groupBox_8)

        self.groupBox_11 = QGroupBox(self.frame_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_33 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_img_canny = QLabel(self.groupBox_11)
        self.label_img_canny.setObjectName(u"label_img_canny")

        self.verticalLayout_33.addWidget(self.label_img_canny)


        self.verticalLayout_21.addWidget(self.groupBox_11)


        self.verticalLayout_20.addWidget(self.frame_5)

        self.stackedWidget_right.addWidget(self.page)

        self.horizontalLayout.addWidget(self.stackedWidget_right)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_selector.setCurrentIndex(1)
        self.stackedWidget_umbral.setCurrentIndex(1)
        self.stackedWidget_blur.setCurrentIndex(2)
        self.stackedWidget_right.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Webcam:", None))
        self.pushButton_start_webcam.setText("")
        self.pushButton_stop_webcam.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_cpu.setText("")
        self.label_ram.setText("")
        self.label_date.setText("")
        self.label_time.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"SELECTOR", None))
        self.groupBox_91.setTitle(QCoreApplication.translate("MainWindow", u"HSV", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HSV Min.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HSV Max", None))
        self.label_min_h.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_min_s.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_min_v.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_max_h.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.label_max_s.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.label_max_v.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"AREA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Area min.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Area max.", None))
        self.label_dial_area_min.setText(QCoreApplication.translate("MainWindow", u"2500", None))
        self.label_dial_area_max.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"TRAYECTORIA", None))
        self.radioButton_trayectoria_on.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.radioButton_trayectoria_off.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"UMBRAL", None))
        self.radioButton_umbral.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.radioButton_adapative.setText(QCoreApplication.translate("MainWindow", u"Adpative", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Adaptive", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blocksize", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Umbral", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_blur.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_gaussian_blur.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_sigma_gaussian_blur.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_medianblur.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.radioButton_canny.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_canny_umbral_alto.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_canny_umbral_bajo.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_img_principal.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"TEXTO", None))
        self.radioButton_sinTexto.setText(QCoreApplication.translate("MainWindow", u"Sin texto", None))
        self.radioButton_textoArea.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.radioButton_textoCentro.setText(QCoreApplication.translate("MainWindow", u"Centro", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_img_umbral.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_img_blur.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_img_canny.setText("")
    # retranslateUi

