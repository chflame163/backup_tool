# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editlist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 235)
        Form.setMinimumSize(QtCore.QSize(460, 235))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(460, 0))
        self.frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgba(240, 240, 240,233), stop:1 rgba(222, 222, 222,233));\n"
"border-radius:18px  \n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_frame = QtWidgets.QFrame(self.frame)
        self.top_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setLineWidth(0)
        self.top_frame.setObjectName("top_frame")
        self.top_frame_horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.top_frame_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame_horizontalLayout.setSpacing(57)
        self.top_frame_horizontalLayout.setObjectName("top_frame_horizontalLayout")
        self.path_frame = QtWidgets.QFrame(self.top_frame)
        self.path_frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.path_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.path_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.path_frame.setLineWidth(0)
        self.path_frame.setObjectName("path_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.path_frame)
        self.horizontalLayout_5.setContentsMargins(24, 16, -1, 2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_set_target = QtWidgets.QPushButton(self.path_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_set_target.sizePolicy().hasHeightForWidth())
        self.btn_set_target.setSizePolicy(sizePolicy)
        self.btn_set_target.setMinimumSize(QtCore.QSize(66, 28))
        self.btn_set_target.setMaximumSize(QtCore.QSize(80, 28))
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
        self.btn_set_target.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.btn_set_target.setFont(font)
        self.btn_set_target.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_set_target.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.btn_set_target.setObjectName("btn_set_target")
        self.horizontalLayout_5.addWidget(self.btn_set_target)
        self.lab_path_name = QtWidgets.QLabel(self.path_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_path_name.sizePolicy().hasHeightForWidth())
        self.lab_path_name.setSizePolicy(sizePolicy)
        self.lab_path_name.setMinimumSize(QtCore.QSize(0, 28))
        self.lab_path_name.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.lab_path_name.setFont(font)
        self.lab_path_name.setStyleSheet("QLabel {\n"
"    border: 0px solid rgb(244, 244, 244); \n"
"    border-radius: 12px; \n"
"    background-color: rgba(255, 255, 255,222); \n"
"    color: rgb(44, 44, 44); \n"
"\n"
"}\n"
"")
        self.lab_path_name.setText("")
        self.lab_path_name.setObjectName("lab_path_name")
        self.horizontalLayout_5.addWidget(self.lab_path_name)
        self.top_frame_horizontalLayout.addWidget(self.path_frame)
        self.close_frame = QtWidgets.QFrame(self.top_frame)
        self.close_frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.close_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.close_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_frame.setLineWidth(0)
        self.close_frame.setObjectName("close_frame")
        self.close_frame_verticalLayout = QtWidgets.QVBoxLayout(self.close_frame)
        self.close_frame_verticalLayout.setContentsMargins(26, 10, 10, 26)
        self.close_frame_verticalLayout.setObjectName("close_frame_verticalLayout")
        self.btn_close = QtWidgets.QPushButton(self.close_frame)
        self.btn_close.setMinimumSize(QtCore.QSize(14, 14))
        self.btn_close.setMaximumSize(QtCore.QSize(14, 14))
        self.btn_close.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(240, 108, 96);\n"
"border:0px solid rgba(113, 17, 15,50);\n"
"border-radius:7px;\n"
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
        self.close_frame_verticalLayout.addWidget(self.btn_close)
        self.top_frame_horizontalLayout.addWidget(self.close_frame)
        self.top_frame_horizontalLayout.setStretch(0, 19)
        self.top_frame_horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.top_frame)
        self.bottom_frame = QtWidgets.QFrame(self.frame)
        self.bottom_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.bottom_frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setLineWidth(0)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table_frame = QtWidgets.QFrame(self.bottom_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_frame.sizePolicy().hasHeightForWidth())
        self.table_frame.setSizePolicy(sizePolicy)
        self.table_frame.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(240, 240, 240), stop:1 rgb(222, 222, 222));\n"
"border-radius:20px  \n"
"}\n"
"")
        self.table_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setLineWidth(0)
        self.table_frame.setObjectName("table_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.table_frame)
        self.horizontalLayout_3.setContentsMargins(12, 0, 0, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView = QtWidgets.QTableView(self.table_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 65, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 250, 255, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 167, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 65, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 250, 255, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 167, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 75, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tableView.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.setStyleSheet("QTableWidget{\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:12px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(190, 205, 225);\n"
"}\n"
"QTableWidget::section{\n"
"border-radius:12px;\n"
"}\n"
"QTableWidget:item{\n"
"padding-top:12px;\n"
"    border-bottom:1px solid rgb(50, 50, 50);\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"    color: rgb(111, 199, 255);\n"
"}\n"
"")
        self.tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableView.setLineWidth(0)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setAutoScroll(True)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.tableView)
        self.horizontalLayout_2.addWidget(self.table_frame)
        self.btns_verticalLayout = QtWidgets.QVBoxLayout()
        self.btns_verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.btns_verticalLayout.setSpacing(88)
        self.btns_verticalLayout.setObjectName("btns_verticalLayout")
        self.btn_clear_file = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_clear_file.setMinimumSize(QtCore.QSize(88, 28))
        self.btn_clear_file.setMaximumSize(QtCore.QSize(16777215, 28))
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
        self.btn_clear_file.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.btn_clear_file.setFont(font)
        self.btn_clear_file.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.btn_clear_file.setObjectName("btn_clear_file")
        self.btns_verticalLayout.addWidget(self.btn_clear_file)
        self.btn_start_backup = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_start_backup.setMinimumSize(QtCore.QSize(88, 50))
        self.btn_start_backup.setMaximumSize(QtCore.QSize(16777215, 50))
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
        self.btn_start_backup.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.btn_start_backup.setFont(font)
        self.btn_start_backup.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(177,177, 177);\n"
"border:2px solid rgba(199, 199, 199,50);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(144, 144, 144)\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.btn_start_backup.setObjectName("btn_start_backup")
        self.btns_verticalLayout.addWidget(self.btn_start_backup)
        self.btns_verticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.btns_verticalLayout)
        self.right_side_frame = QtWidgets.QFrame(self.bottom_frame)
        self.right_side_frame.setMinimumSize(QtCore.QSize(12, 0))
        self.right_side_frame.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.right_side_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side_frame.setLineWidth(0)
        self.right_side_frame.setObjectName("right_side_frame")
        self.horizontalLayout_2.addWidget(self.right_side_frame)
        self.verticalLayout_2.addWidget(self.bottom_frame)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 12))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bottom_side_frame = QtWidgets.QFrame(self.frame_2)
        self.bottom_side_frame.setMinimumSize(QtCore.QSize(0, 12))
        self.bottom_side_frame.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.bottom_side_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_side_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_side_frame.setLineWidth(0)
        self.bottom_side_frame.setObjectName("bottom_side_frame")
        self.horizontalLayout_7.addWidget(self.bottom_side_frame)
        self.conner_frame = QtWidgets.QFrame(self.frame_2)
        self.conner_frame.setMinimumSize(QtCore.QSize(18, 12))
        self.conner_frame.setMaximumSize(QtCore.QSize(18, 12))
        self.conner_frame.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.conner_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conner_frame.setLineWidth(0)
        self.conner_frame.setObjectName("conner_frame")
        self.horizontalLayout_7.addWidget(self.conner_frame)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_set_target.setText(_translate("Form", "备份到"))
        self.btn_clear_file.setText(_translate("Form", "清空列表"))
        self.btn_start_backup.setText(_translate("Form", "开始备份"))
