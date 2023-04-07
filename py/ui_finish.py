# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_finish.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 180)
        Form.setMinimumSize(QtCore.QSize(450, 180))
        Form.setMaximumSize(QtCore.QSize(450, 180))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BackupTool.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 161))
        self.frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgba(240, 240, 240,233), stop:1 rgba(222, 222, 222,233));\n"
"border-radius:18px  \n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_ok = QtWidgets.QPushButton(self.frame)
        self.btn_ok.setGeometry(QtCore.QRect(163, 106, 111, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_ok.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.btn_ok.setObjectName("btn_ok")
        self.lab_title = QtWidgets.QLabel(self.frame)
        self.lab_title.setGeometry(QtCore.QRect(126, 13, 181, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.lab_title.setFont(font)
        self.lab_title.setStyleSheet("color: rgb(49, 54, 54)")
        self.lab_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_title.setObjectName("lab_title")
        self.lab_prompt = QtWidgets.QLabel(self.frame)
        self.lab_prompt.setGeometry(QtCore.QRect(20, 54, 394, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.lab_prompt.setFont(font)
        self.lab_prompt.setStyleSheet("color: rgb(33, 38, 38)")
        self.lab_prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_prompt.setObjectName("lab_prompt")
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setGeometry(QtCore.QRect(406, 11, 14, 14))
        self.btn_close.setMinimumSize(QtCore.QSize(14, 14))
        self.btn_close.setMaximumSize(QtCore.QSize(14, 14))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(240, 108, 96);\n"
"border:0px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(232, 59, 35);\n"
"}\n"
"")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Backup Finished"))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.lab_title.setText(_translate("Form", "备份完成"))
        self.lab_prompt.setText(_translate("Form", "文件已成功备份到\n"
""))