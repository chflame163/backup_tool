# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_msgbox.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 180)
        Form.setMinimumSize(QSize(400, 180))
        Form.setMaximumSize(QSize(400, 180))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        Form.setFont(font)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 381, 161))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgba(240, 240, 240,233), stop:1 rgba(222, 222, 222,233));\n"
"border-radius:18px  \n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lab_title = QLabel(self.frame)
        self.lab_title.setObjectName(u"lab_title")
        self.lab_title.setGeometry(QRect(20, 7, 341, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(16)
        self.lab_title.setFont(font1)
        self.lab_title.setStyleSheet(u"color: rgb(49, 54, 54)")
        self.lab_title.setAlignment(Qt.AlignCenter)
        self.lab_message = QLabel(self.frame)
        self.lab_message.setObjectName(u"lab_message")
        self.lab_message.setGeometry(QRect(20, 30, 341, 81))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(10)
        self.lab_message.setFont(font2)
        self.lab_message.setStyleSheet(u"color: rgb(33, 38, 38)")
        self.lab_message.setAlignment(Qt.AlignCenter)
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(359, 9, 14, 14))
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
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 110, 241, 41))
        self.btn_horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.btn_horizontalLayout.setSpacing(36)
        self.btn_horizontalLayout.setObjectName(u"btn_horizontalLayout")
        self.btn_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_ok = QPushButton(self.layoutWidget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(0, 36))
        self.btn_ok.setMaximumSize(QSize(88, 16777215))
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
        self.btn_ok.setFont(font2)
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

        self.btn_horizontalLayout.addWidget(self.btn_ok)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Warning!", None))
        self.lab_title.setText(QCoreApplication.translate("Form", u"\u8b66\u544a\uff01", None))
        self.lab_message.setText(QCoreApplication.translate("Form", u"\u6d88\u606f\n"
"", None))
        self.btn_close.setText("")
        self.btn_ok.setText(QCoreApplication.translate("Form", u"Yes", None))
    # retranslateUi

