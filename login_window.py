# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
import xmlrpc

from xmlrpc import client as rpc_client


class Login(QtGui.QDialog):
    font = QtGui.QFont()

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setObjectName("login_form")

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.font.setPointSize(20)
        self.textName = QtGui.QLineEdit(self)
        self.textName.move(100, 100)
        self.textName.resize(300, 40)
        self.textName.setPlaceholderText(self.tr("Nombre de Usuario"))
        self.textName.setFont(self.font)
        self.textName.setStyleSheet(
            "border-radius: 5px; background-color: rgb(100,100,100)")

        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handle_login)
        self.buttonLogin.move(30, 100)
        self.buttonLogin.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.textPass.move(10, 50)
        self.textPass.setPlaceholderText(self.tr("Contraseña"))

        self.textPass.setFont(self.font)

        self.textPass.setEchoMode(QtGui.QLineEdit.Password)

        self.setFixedSize(500, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        self.setStyleSheet("#login_form{background-color: rgba(100,100,100,128);}")

    def handle_login(self):
        username = self.textName.text()
        password = self.textPass.text()

        db = rpc_client.ServerProxy('https://odoo.jorgejuarez.net/xmlrpc/2/common')
        auth_id = db.authenticate("odoo", username, password, {})
        if auth_id is not False:
            self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password {0}'.format(auth_id))
