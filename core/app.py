from interface.ui_interface import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow

from PySide2.QtGui import QPixmap, QImage
from PySide2.QtCore import QTimer, Slot, QThread, Signal, Qt
import cv2
import numpy as np

import psutil
import time
from datetime import datetime

from colores.detector import DetectorColor


class Utiles(QThread):
    cpu = Signal(float)
    ram = Signal(float)
    date = Signal(str)
    time = Signal(str)

    def run(self):
        while True:
            self.cpu.emit(psutil.cpu_percent())
            self.ram.emit(psutil.virtual_memory().percent)
            self.date.emit(datetime.now().strftime("%d/%m/%Y"))
            self.time.emit(datetime.now().strftime("%H:%M:%S"))

            time.sleep(1)


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        # Interfaz
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Predeterminado
        self.ui.radioButton_trayectoria_off.setChecked(True)
        self.ui.radioButton_sinTexto.setChecked(True)
        self.ui.stackedWidget_selector.setCurrentIndex(0)
        self.ui.stackedWidget_right.setCurrentIndex(0)
        self.ui.stackedWidget_blur.setCurrentIndex(0)

        # Cabecera
        self.hilo = Utiles()
        self.hilo.cpu.connect(self.label_cpu)
        self.hilo.ram.connect(self.label_ram)
        self.hilo.date.connect(self.label_date)
        self.hilo.time.connect(self.label_time)
        self.hilo.start()

        # Combobox webcam
        self.cap = None
        self.img = None
        self.ui.comboBox_webcam.setCurrentIndex(0)
        self.ui.comboBox_webcam.currentIndexChanged.connect(self.webcam_selector)
        self.ui.comboBox_webcam.addItems(["Webcam1", "Webcam2"])

        # Mando webcam
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_frame(option=self.ui.comboBox_selector.currentIndex()))
        self.ui.pushButton_start_webcam.clicked.connect(lambda: self.timer.start(round(1000 / 30)))
        self.ui.pushButton_stop_webcam.clicked.connect(self.webcam_off)

        # Combobox selector
        self.ui.comboBox_selector.addItems(["Detector color HSV", "Detector de bordes"])
        self.ui.comboBox_selector.currentIndexChanged.connect(self.ui.stackedWidget_selector.setCurrentIndex)
        self.ui.comboBox_selector.currentIndexChanged.connect(self.ui.stackedWidget_right.setCurrentIndex)

        """
        Objeto HSV detector y widgets
        """
        self.detector = DetectorColor()

        # Sliders HSV
        self.ui.min_h.valueChanged.connect(self.write_h_min)
        self.ui.min_s.valueChanged.connect(self.write_s_min)
        self.ui.min_v.valueChanged.connect(self.write_v_min)
        self.ui.min_h.valueChanged.connect(self.ui.label_min_h.setNum)
        self.ui.min_s.valueChanged.connect(self.ui.label_min_s.setNum)
        self.ui.min_v.valueChanged.connect(self.ui.label_min_v.setNum)

        self.ui.max_h.valueChanged.connect(self.write_h_max)
        self.ui.max_s.valueChanged.connect(self.write_s_max)
        self.ui.max_v.valueChanged.connect(self.write_v_max)
        self.ui.max_h.valueChanged.connect(self.ui.label_max_h.setNum)
        self.ui.max_s.valueChanged.connect(self.ui.label_max_s.setNum)
        self.ui.max_v.valueChanged.connect(self.ui.label_max_v.setNum)

        # Dials area
        self.area_min = self.ui.dial_area_min.value()
        self.area_max = self.ui.dial_area_max.value()
        self.ui.dial_area_min.valueChanged.connect(self.ui.label_dial_area_min.setNum)
        self.ui.dial_area_max.valueChanged.connect(self.ui.label_dial_area_max.setNum)

        self.colorBajo = np.array([0, 0, 0], np.uint8)
        self.colorAlto = np.array([255, 255, 255], np.uint8)

        """
        Filtros opencv
        """
        # Umbrales
        lista = ["THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC",
                 "THRESH_TOZERO", "THRESH_TOZERO_INV", "THRESH_MASK",
                 "THRESH_OTSU", "THRESH_TRIANGLE"]
        self.ui.comboBox_umbral.addItems(lista)
        self.ui.stackedWidget_umbral.setCurrentIndex(0)
        self.ui.radioButton_umbral.setChecked(True)
        self.ui.radioButton_umbral.toggled.connect(self.thresh_frames_options)
        self.ui.comboBox_adaptive_umbral.addItems(["ADAPTIVE_THRESH_GAUSSIAN_C", "ADAPTIVE_THRESH_MEAN_C"])
        self.ui.comboBox_umbral_2.addItems(lista)
        self.ui.comboBox_blocksize_umbral.addItems(["3", "5", "7", "9", "11", "13", "15", "17", "19", "21", "23", "25"])
        self.ui.comboBox_blocksize_umbral.setCurrentText("9")
        self.ui.comboBox_c_umbral.addItems(["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"])
        self.ui.comboBox_c_umbral.setCurrentText("0")

        # Blur
        self.ui.comboBox_blur_types.addItems(["BLUR", "GAUSSIAN BLUR", "MEDIANBLUR", "BILATERAL"])
        self.ui.comboBox_blur_types.currentIndexChanged.connect(self.ui.stackedWidget_blur.setCurrentIndex)
        self.ui.slider_kernel_blur.valueChanged.connect(self.ui.label_blur.setNum)
        self.ui.slider_kernel_gaussian_blur.valueChanged.connect(self.ui.label_gaussian_blur.setNum)
        self.ui.slider_sigma_gaussian_blur.valueChanged.connect(self.ui.label_sigma_gaussian_blur.setNum)
        self.ui.slider_canny_umbral_alto.valueChanged.connect(self.ui.label_canny_umbral_alto.setNum)
        self.ui.slider_canny_umbral_bajo.valueChanged.connect(self.ui.label_canny_umbral_bajo.setNum)
        self.ui.slider_medianblur.valuechanged.connect(self.ui.label_medianblur.setNum)

    @Slot(float)
    def label_cpu(self, value):
        self.ui.label_cpu.setText(f"{value}%")

    @Slot(float)
    def label_ram(self, value):
        self.ui.label_ram.setText(f"{value}%")

    @Slot(str)
    def label_date(self, value):
        self.ui.label_date.setText(f"{value}")

    @Slot(str)
    def label_time(self, value):
        self.ui.label_time.setText(f"{value}")

    @Slot(int)
    def webcam_selector(self, value):
        self.cap = cv2.VideoCapture(value)

    def webcam_off(self):
        self.timer.stop()
        self.ui.label_img_principal.clear()

    def update_frame(self, option):

        ret, frame = self.cap.read()
        if ret:
            self.area_min = self.ui.dial_area_min.value()
            self.area_max = self.ui.dial_area_max.value()

            if option == 0:
                frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                maskAzul = cv2.inRange(frameHSV, self.colorBajo, self.colorAlto)
                self.detector.dibujar_hsv(mask=maskAzul,
                                          frame=frame,
                                          area_min=self.area_min,
                                          area_max=self.area_max,
                                          button_empty=self.ui.radioButton_sinTexto,
                                          button_area=self.ui.radioButton_textoArea,
                                          button_text=self.ui.radioButton_textoCentro,
                                          track=self.ui.radioButton_trayectoria_on)
                self.image_pixmap_rgb(frame=frame,
                                      method=cv2.COLOR_BGR2RGB)
            elif option == 1:

                img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                if self.ui.radioButton_umbral.isChecked():
                    self.detector.dibujar_umbral(frame=img_gray,
                                                 thresh=self.ui.slider_umbral_min.value(),
                                                 maxval=self.ui.slider_umbral_max.value(),
                                                 label=self.ui.label_img_umbral,
                                                 method=self.detector.thresh_types(
                                                     self.ui.comboBox_umbral.currentIndex()))
                elif self.ui.radioButton_adapative.isChecked():
                    self.detector.dibujar_umbral_adapative(frame=img_gray,
                                                           maxval=self.ui.slider_max_adaptive_umbral.value(),
                                                           label=self.ui.label_img_umbral,
                                                           blocksize=int(
                                                               self.ui.comboBox_blocksize_umbral.currentText()),
                                                           c=int(self.ui.comboBox_c_umbral.currentText()),
                                                           adaptive_method=self.detector.adaptive_thresh_types(
                                                               self.ui.comboBox_adaptive_umbral.currentIndex()),
                                                           method=self.detector.thresh_types(
                                                               self.ui.comboBox_umbral.currentIndex()))

                self.blur_types(img_gray=img_gray,
                                kernel=self.ui.slider_kernel_blur.value(),
                                sigma=self.ui.slider_sigma_gaussian_blur.value(),
                                diameter=0,
                                sigmacolor=0,
                                sigmaspace=0)

                if self.ui.radioButton_canny.isChecked():
                    kernel = self.ui.slider_kernel_blur.value()
                    self.detector.dibujar_canny(frame=img_gray,
                                                kernel=(kernel, kernel),
                                                umbral_bajo=self.ui.slider_canny_umbral_bajo.value(),
                                                umbral_alto=self.ui.slider_canny_umbral_alto.value(),
                                                label=self.ui.label_img_canny,
                                                imagen=frame,
                                                indice=self.ui.spinBox_pruebas_contour.value())

                if self.ui.radioButton_canny.isChecked():
                    frame = cv2.cvtColor(src=frame, code=cv2.COLOR_HSV2BGR)
                    self.image_pixmap_rgb(frame=frame)
                else:
                    self.image_pixmap_gray(frame=frame)
        else:
            print("No conecta la cámara")

    def image_pixmap_rgb(self, frame, method=cv2.COLOR_BGR2HSV):

        self.ui.label_img_principal.clear()
        rgb_image = cv2.cvtColor(frame, method)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.ui.label_img_principal.setPixmap(QPixmap.fromImage(qt_image))

    def image_pixmap_gray(self, frame, method=cv2.COLOR_BGR2GRAY):

        self.ui.label_img_principal.clear()
        gray_image = cv2.cvtColor(frame, method)
        h, w = gray_image.shape
        qt_image = QImage(gray_image.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        self.ui.label_img_principal.setPixmap(QPixmap.fromImage(qt_image))

    @Slot(int)
    def write_h_min(self, value):
        self.colorBajo[0] = value

    @Slot(int)
    def write_s_min(self, value):
        self.colorBajo[1] = value

    @Slot(int)
    def write_v_min(self, value):
        self.colorBajo[2] = value

    @Slot(int)
    def write_h_max(self, value):
        self.colorAlto[0] = value

    @Slot(int)
    def write_s_max(self, value):
        self.colorAlto[1] = value

    @Slot(int)
    def write_v_max(self, value):
        self.colorAlto[2] = value

    @Slot(int)
    def update_tresh_types(self, index):
        self.detector.thresh_types(position=index)

    def thresh_frames_options(self):

        if self.ui.radioButton_umbral.isChecked():
            self.ui.stackedWidget_umbral.setCurrentIndex(0)
        elif self.ui.radioButton_adapative.isChecked():
            self.ui.stackedWidget_umbral.setCurrentIndex(1)

    def blur_types(self, img_gray, kernel, sigma, diameter, sigmacolor, sigmaspace):

        selection = self.ui.comboBox_blur_types.currentText()

        if selection == "BLUR":
            self.detector.dibujar_blur(frame=img_gray,
                                       kernel=(kernel, kernel),
                                       label=self.ui.label_img_blur)
        elif selection == "GAUSSIAN BLUR":
            self.detector.dibujar_gaussian_blur(frame=img_gray,
                                                kernel=(kernel, kernel),
                                                sigma=sigma,
                                                label=self.ui.label_img_blur)
        elif selection == "MEDIANBLUR":
            self.detector.dibujar_median_blur(frame=img_gray,
                                              kernel=(kernel, kernel),
                                              label=self.ui.label_img_blur)
        elif selection == "BILATERAL":
            self.detector.dibujar_bilateral_blur(frame=img_gray,
                                                 diameter=diameter,
                                                 sigmacolor=sigmacolor,
                                                 sigmaspace=sigmaspace)



