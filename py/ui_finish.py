# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_finish.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 180)
        Form.setMinimumSize(QSize(450, 180))
        Form.setMaximumSize(QSize(450, 180))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u"BackupTool.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 431, 161))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgba(240, 240, 240,233), stop:1 rgba(222, 222, 222,233));\n"
"border-radius:18px  \n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_ok = QPushButton(self.frame)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(163, 106, 111, 40))
        palette = QPalette()
        brush = QBrush(QColor(177, 177, 177, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush2 = QBrush(QColor(31, 31, 31, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_ok.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(10)
        self.btn_ok.setFont(font1)
        self.btn_ok.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.lab_title = QLabel(self.frame)
        self.lab_title.setObjectName(u"lab_title")
        self.lab_title.setGeometry(QRect(26, 13, 371, 36))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(16)
        self.lab_title.setFont(font2)
        self.lab_title.setStyleSheet(u"color: rgb(49, 54, 54)")
        self.lab_title.setAlignment(Qt.AlignCenter)
        self.lab_prompt = QLabel(self.frame)
        self.lab_prompt.setObjectName(u"lab_prompt")
        self.lab_prompt.setGeometry(QRect(13, 44, 401, 61))
        self.lab_prompt.setFont(font1)
        self.lab_prompt.setStyleSheet(u"color: rgb(33, 38, 38)")
        self.lab_prompt.setAlignment(Qt.AlignCenter)
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(406, 11, 14, 14))
        self.btn_close.setMinimumSize(QSize(14, 14))
        self.btn_close.setMaximumSize(QSize(14, 14))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:0px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Backup Finished", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.lab_title.setText(QCoreApplication.translate("Form", u"\u5907\u4efd\u5b8c\u6210", None))
        self.lab_prompt.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5df2\u6210\u529f\u5907\u4efd\u5230\n"
"", None))
        self.btn_close.setText("")
    # retranslateUi

