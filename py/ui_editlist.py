# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_editlist.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(535, 280)
        Form.setMinimumSize(QSize(460, 235))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(460, 0))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgba(240, 240, 240,233), stop:1 rgba(222, 222, 222,233));\n"
"border-radius:18px  \n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 50))
        self.top_frame.setMaximumSize(QSize(16777215, 50))
        self.top_frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.top_frame.setLineWidth(0)
        self.top_frame_horizontalLayout = QHBoxLayout(self.top_frame)
        self.top_frame_horizontalLayout.setSpacing(63)
        self.top_frame_horizontalLayout.setObjectName(u"top_frame_horizontalLayout")
        self.top_frame_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.path_frame = QFrame(self.top_frame)
        self.path_frame.setObjectName(u"path_frame")
        self.path_frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.path_frame.setFrameShape(QFrame.NoFrame)
        self.path_frame.setFrameShadow(QFrame.Raised)
        self.path_frame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.path_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(24, 16, -1, 2)
        self.btn_set_target = QPushButton(self.path_frame)
        self.btn_set_target.setObjectName(u"btn_set_target")
        sizePolicy.setHeightForWidth(self.btn_set_target.sizePolicy().hasHeightForWidth())
        self.btn_set_target.setSizePolicy(sizePolicy)
        self.btn_set_target.setMinimumSize(QSize(66, 28))
        self.btn_set_target.setMaximumSize(QSize(90, 28))
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
        self.btn_set_target.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(10)
        self.btn_set_target.setFont(font)
        self.btn_set_target.setLayoutDirection(Qt.RightToLeft)
        self.btn_set_target.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_set_target)

        self.lab_path_name = QLabel(self.path_frame)
        self.lab_path_name.setObjectName(u"lab_path_name")
        sizePolicy.setHeightForWidth(self.lab_path_name.sizePolicy().hasHeightForWidth())
        self.lab_path_name.setSizePolicy(sizePolicy)
        self.lab_path_name.setMinimumSize(QSize(0, 28))
        self.lab_path_name.setMaximumSize(QSize(16777215, 28))
        self.lab_path_name.setFont(font)
        self.lab_path_name.setStyleSheet(u"QLabel {\n"
"	border: 0px solid rgb(244, 244, 244); \n"
"	border-radius: 12px; \n"
"	background-color: rgba(255, 255, 255,222); \n"
"	color: rgb(44, 44, 44); \n"
"\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.lab_path_name)


        self.top_frame_horizontalLayout.addWidget(self.path_frame)

        self.close_frame = QFrame(self.top_frame)
        self.close_frame.setObjectName(u"close_frame")
        self.close_frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.close_frame.setFrameShape(QFrame.NoFrame)
        self.close_frame.setFrameShadow(QFrame.Raised)
        self.close_frame.setLineWidth(0)
        self.close_frame_verticalLayout = QVBoxLayout(self.close_frame)
        self.close_frame_verticalLayout.setObjectName(u"close_frame_verticalLayout")
        self.close_frame_verticalLayout.setContentsMargins(26, 10, 10, 26)
        self.btn_close = QPushButton(self.close_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(14, 14))
        self.btn_close.setMaximumSize(QSize(14, 14))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:0px solid rgba(113, 17, 15,50);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.close_frame_verticalLayout.addWidget(self.btn_close)


        self.top_frame_horizontalLayout.addWidget(self.close_frame)

        self.top_frame_horizontalLayout.setStretch(0, 19)
        self.top_frame_horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 0))
        self.bottom_frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.bottom_frame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.table_frame = QFrame(self.bottom_frame)
        self.table_frame.setObjectName(u"table_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_frame.sizePolicy().hasHeightForWidth())
        self.table_frame.setSizePolicy(sizePolicy1)
        self.table_frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.table_frame.setFrameShape(QFrame.NoFrame)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.table_frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.table_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 0, 0, 12)
        self.tableView = QTableView(self.table_frame)
        self.tableView.setObjectName(u"tableView")
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 0))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush4 = QBrush(QColor(66, 65, 66, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        brush5 = QBrush(QColor(249, 250, 255, 217))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush6 = QBrush(QColor(65, 167, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        brush8 = QBrush(QColor(0, 0, 0, 28))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush10 = QBrush(QColor(28, 75, 105, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.tableView.setPalette(palette1)
        self.tableView.setFont(font)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:12px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(190, 205, 225);\n"
"}\n"
"QTableWidget::section{\n"
"border-radius:12px;\n"
"}\n"
"QTableWidget:item{\n"
"padding-top:12px;\n"
"	border-bottom:1px solid rgb(50, 50, 50);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"	color: rgb(111, 199, 255);\n"
"}\n"
"")
        self.tableView.setFrameShape(QFrame.NoFrame)
        self.tableView.setLineWidth(0)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setAutoScroll(True)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.tableView)


        self.horizontalLayout_2.addWidget(self.table_frame)

        self.btns_verticalLayout = QVBoxLayout()
        self.btns_verticalLayout.setSpacing(88)
        self.btns_verticalLayout.setObjectName(u"btns_verticalLayout")
        self.btns_verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.btn_clear_file = QPushButton(self.bottom_frame)
        self.btn_clear_file.setObjectName(u"btn_clear_file")
        self.btn_clear_file.setMinimumSize(QSize(88, 28))
        self.btn_clear_file.setMaximumSize(QSize(16777215, 28))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_clear_file.setPalette(palette2)
        self.btn_clear_file.setFont(font)
        self.btn_clear_file.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"")

        self.btns_verticalLayout.addWidget(self.btn_clear_file)

        self.btn_start_backup = QPushButton(self.bottom_frame)
        self.btn_start_backup.setObjectName(u"btn_start_backup")
        self.btn_start_backup.setMinimumSize(QSize(88, 50))
        self.btn_start_backup.setMaximumSize(QSize(16777215, 50))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_start_backup.setPalette(palette3)
        self.btn_start_backup.setFont(font)
        self.btn_start_backup.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"")

        self.btns_verticalLayout.addWidget(self.btn_start_backup)

        self.btns_verticalLayout.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.btns_verticalLayout)

        self.right_side_frame = QFrame(self.bottom_frame)
        self.right_side_frame.setObjectName(u"right_side_frame")
        self.right_side_frame.setMinimumSize(QSize(12, 0))
        self.right_side_frame.setCursor(QCursor(Qt.SizeHorCursor))
        self.right_side_frame.setFrameShape(QFrame.NoFrame)
        self.right_side_frame.setFrameShadow(QFrame.Raised)
        self.right_side_frame.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.right_side_frame)


        self.verticalLayout_2.addWidget(self.bottom_frame)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 12))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bottom_side_frame = QFrame(self.frame_2)
        self.bottom_side_frame.setObjectName(u"bottom_side_frame")
        self.bottom_side_frame.setMinimumSize(QSize(0, 12))
        self.bottom_side_frame.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom_side_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_side_frame.setFrameShadow(QFrame.Raised)
        self.bottom_side_frame.setLineWidth(0)

        self.horizontalLayout_7.addWidget(self.bottom_side_frame)

        self.conner_frame = QFrame(self.frame_2)
        self.conner_frame.setObjectName(u"conner_frame")
        self.conner_frame.setMinimumSize(QSize(18, 12))
        self.conner_frame.setMaximumSize(QSize(18, 12))
        self.conner_frame.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.conner_frame.setFrameShape(QFrame.NoFrame)
        self.conner_frame.setFrameShadow(QFrame.Raised)
        self.conner_frame.setLineWidth(0)

        self.horizontalLayout_7.addWidget(self.conner_frame)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_set_target.setText(QCoreApplication.translate("Form", u"\u5907\u4efd\u5230", None))
        self.lab_path_name.setText("")
        self.btn_close.setText("")
        self.btn_clear_file.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u5217\u8868", None))
        self.btn_start_backup.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5907\u4efd", None))
    # retranslateUi

