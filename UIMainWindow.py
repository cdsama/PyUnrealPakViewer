# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\cdsama-git\PyUnrealPakViewer\UIMainWindow.ui',
# licensing of 'e:\cdsama-git\PyUnrealPakViewer\UIMainWindow.ui' applies.
#
# Created: Wed Jan 23 18:55:48 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 588)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.label = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontal_layout.addWidget(self.label)
        self.combo_box = QtWidgets.QComboBox(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.combo_box.setFont(font)
        self.combo_box.setObjectName("combo_box")
        self.horizontal_layout.addWidget(self.combo_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem)
        self.btn_test = QtWidgets.QPushButton(self.central_widget)
        self.btn_test.setObjectName("btn_test")
        self.horizontal_layout.addWidget(self.btn_test)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.file_list_view = QtWidgets.QListWidget(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_list_view.sizePolicy().hasHeightForWidth())
        self.file_list_view.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.file_list_view.setFont(font)
        self.file_list_view.setObjectName("file_list_view")
        self.verticalLayout_2.addWidget(self.file_list_view)
        self.pak_content_tree_view = QtWidgets.QTreeWidget(self.central_widget)
        self.pak_content_tree_view.setColumnCount(4)
        self.pak_content_tree_view.setObjectName("pak_content_tree_view")
        self.pak_content_tree_view.headerItem().setText(0, "1")
        self.pak_content_tree_view.headerItem().setText(1, "2")
        self.pak_content_tree_view.headerItem().setText(2, "3")
        self.pak_content_tree_view.headerItem().setText(3, "4")
        self.pak_content_tree_view.header().setCascadingSectionResizes(True)
        self.verticalLayout_2.addWidget(self.pak_content_tree_view)
        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "引擎位置：", None, -1))
        self.btn_test.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))

