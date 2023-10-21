import cv2
import numpy as np
from PySide2.QtGui import QPixmap, QImage, Qt


class DetectorColor:

    def __init__(self):

        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.azulBajo = np.array([100, 100, 20], np.uint8)
        self.azulAlto = np.array([255, 255, 255], np.uint8)  # 125,255,255

        self.path_points = []

    def dibujar_hsv(self, mask, frame, area_min, area_max, button_empty, button_text, button_area, track):
        contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

        for c in contornos:
            area = cv2.contourArea(c)

            M = cv2.moments(c)
            if M["m00"] == 0:
                M["m00"] = 1
            eje_x = int(M["m10"] / M["m00"])
            eje_y = int(M['m01'] / M['m00'])

            if area_min <= area <= area_max:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

                if button_area.isChecked():
                    cv2.putText(img=frame,
                                text=str(area),
                                org=(eje_x + 10, eje_y - 10),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.5,
                                color=(255, 0, 0),
                                thickness=1,
                                lineType=cv2.LINE_AA)
                elif button_text.isChecked():
                    cv2.putText(img=frame,
                                text=f"{eje_x}-{eje_y}",
                                org=(eje_x + 10, eje_y - 10),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.5,
                                color=(255, 0, 0),
                                thickness=1,
                                lineType=cv2.LINE_AA)

                if track.isChecked():
                    self.path_points.append((eje_x, eje_y))
                    for i in range(1, len(self.path_points)):
                        cv2.line(img=frame,
                                 pt1=self.path_points[i - 1],
                                 pt2=self.path_points[i],
                                 color=(0, 255, 255),
                                 thickness=1,
                                 lineType=cv2.LINE_AA)
                else:
                    self.path_points.clear()

    @staticmethod
    def dibujar_umbral(frame, thresh, maxval, label, method=cv2.THRESH_BINARY):

        _, img_umbral = cv2.threshold(src=frame,
                                      thresh=thresh,
                                      maxval=maxval,
                                      type=method)

        h, w = img_umbral.shape
        qt_image = QImage(img_umbral.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

    @staticmethod
    def dibujar_umbral_adapative(frame, maxval, label, blocksize, c,
                                 adaptive_method=cv2.ADAPTIVE_THRESH_MEAN_C, method=cv2.THRESH_BINARY):

        img_umbral = cv2.adaptiveThreshold(src=frame,
                                           maxValue=maxval,
                                           adaptiveMethod=adaptive_method,
                                           thresholdType=method,
                                           blockSize=blocksize,
                                           C=c)
        h, w = img_umbral.shape
        qt_image = QImage(img_umbral.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

    @staticmethod
    def thresh_types(position=0):

        lista = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV,
                 cv2.THRESH_MASK, cv2.THRESH_OTSU, cv2.THRESH_TRIANGLE]

        return lista[position]

    @staticmethod
    def adaptive_thresh_types(position=0):

        lista = [cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.ADAPTIVE_THRESH_MEAN_C]

        return lista[position]

    @staticmethod
    def dibujar_blur(frame, kernel, label=None):

        img_blur = cv2.blur(src=frame,
                            ksize=(kernel, kernel))

        h, w = img_blur.shape
        qt_image = QImage(img_blur.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

    @staticmethod
    def dibujar_gaussian_blur(frame, kernel, sigma=0, label=None):

        if kernel % 2 == 0:
            kernel += 1

        img_blur = cv2.GaussianBlur(src=frame,
                                    ksize=(kernel, kernel),
                                    sigmaX=sigma)

        h, w = img_blur.shape
        qt_image = QImage(img_blur.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho más precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

    @staticmethod
    def dibujar_median_blur(frame, kernel, label=None):

        if kernel % 2 == 0:
            kernel += 1

        img_blur = cv2.medianBlur(src=frame,
                                  ksize=kernel)

        h, w = img_blur.shape
        qt_image = QImage(img_blur.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

    @staticmethod
    def dibujar_bilateral_blur(frame, diameter, sigmacolor, sigmaspace, label=None):

        img_blur = cv2.bilateralFilter(src=frame,
                                       d=diameter,
                                       sigmaColor=sigmacolor,
                                       sigmaSpace=sigmaspace)

        h, w = img_blur.shape
        qt_image = QImage(img_blur.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

    @staticmethod
    def dibujar_canny(frame, kernel, umbral_bajo, umbral_alto, label, imagen, indice):

        img_blur = cv2.blur(src=frame,
                            ksize=(kernel, kernel))

        canny = cv2.Canny(image=img_blur,
                          threshold1=umbral_bajo,
                          threshold2=umbral_alto)

        h, w = canny.shape
        qt_image = QImage(canny.data, w, h, w,
                          QImage.Format_Grayscale8)  # Ojo con la 16 que es mucho mas precisa y escala hasta 650000 Grayscale16
        label.setPixmap(QPixmap.fromImage(qt_image).scaled(300, 200, Qt.KeepAspectRatio))

        contornos, jerarquia = cv2.findContours(image=canny,
                                                mode=cv2.RETR_EXTERNAL,
                                                method=cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(image=imagen,
                         contours=contornos,
                         contourIdx=indice,
                         color=(0, 0, 126),
                         thickness=2)
