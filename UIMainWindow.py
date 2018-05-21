# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIMainWindow.ui'
#
# Created: Mon May 21 15:21:52 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1525348439
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 587)
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
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_list_view = QtWidgets.QListWidget(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_list_view.sizePolicy().hasHeightForWidth())
        self.file_list_view.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.file_list_view.setFont(font)
        self.file_list_view.setObjectName("file_list_view")
        self.horizontalLayout.addWidget(self.file_list_view)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.pak_content_tree_view = QtWidgets.QListWidget(self.central_widget)
        self.pak_content_tree_view.setObjectName("pak_content_tree_view")
        self.horizontalLayout.addWidget(self.pak_content_tree_view)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 23))
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

