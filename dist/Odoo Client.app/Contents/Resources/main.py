# -*- coding:utf-8 -*-
import sys, os

from PyQt4 import QtGui, QtCore
from main_window import MainWindow
from login_window import Login


def main():
    app = QtGui.QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load('i18n/tr_de', os.path.dirname(__file__))
    app.installTranslator(translator)

    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        ex = MainWindow()
        ex.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
