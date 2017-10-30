# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    # noinspection PyArgumentList
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("Mi Aplicación Numero Uno")

        self.central_widget = QtGui.QWidget(self)
        self.pushButton = QtGui.QPushButton(self.central_widget)
        # self.pushButton.setGeometry(QtCore.QRect(10, 10, 110, 32))

        self.pushButton.resize(100, 50)
        self.pushButton.move(10, 10)

        self.pushButton.setText("Hola Mundo")
        self.pushButton.clicked.connect(self.btn_click)
        self.setCentralWidget(self.central_widget)

    def btn_click(self, sender):
        QtGui.QMessageBox.about(self, self.tr("My Application"),
                                "Esta es una advertencia de seguridad")
