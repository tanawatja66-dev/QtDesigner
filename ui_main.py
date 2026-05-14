# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_id = QLabel(self.groupBox)
        self.label_id.setObjectName(u"label_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_id)

        self.lineEdit_id = QLineEdit(self.groupBox)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_id)

        self.label_name = QLabel(self.groupBox)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.lineEdit_name = QLineEdit(self.groupBox)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_name)

        self.label_lastname = QLabel(self.groupBox)
        self.label_lastname.setObjectName(u"label_lastname")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_lastname)

        self.lineEdit_lastname = QLineEdit(self.groupBox)
        self.lineEdit_lastname.setObjectName(u"lineEdit_lastname")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_lastname)

        self.label_gender = QLabel(self.groupBox)
        self.label_gender.setObjectName(u"label_gender")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_gender)

        self.widget_gender = QWidget(self.groupBox)
        self.widget_gender.setObjectName(u"widget_gender")
        self.horizontalLayout_gender = QHBoxLayout(self.widget_gender)
        self.horizontalLayout_gender.setObjectName(u"horizontalLayout_gender")
        self.horizontalLayout_gender.setContentsMargins(0, -1, -1, -1)
        self.radioButton_male = QRadioButton(self.widget_gender)
        self.radioButton_male.setObjectName(u"radioButton_male")
        self.radioButton_male.setChecked(True)

        self.horizontalLayout_gender.addWidget(self.radioButton_male)

        self.radioButton_female = QRadioButton(self.widget_gender)
        self.radioButton_female.setObjectName(u"radioButton_female")

        self.horizontalLayout_gender.addWidget(self.radioButton_female)


        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.widget_gender)

        self.label_major = QLabel(self.groupBox)
        self.label_major.setObjectName(u"label_major")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_major)

        self.comboBox_major = QComboBox(self.groupBox)
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.addItem("")
        self.comboBox_major.setObjectName(u"comboBox_major")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox_major)


        self.verticalLayout_main.addWidget(self.groupBox)

        self.widget_buttons = QWidget(self.centralwidget)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.horizontalLayout_buttons = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.pushButton_clear = QPushButton(self.widget_buttons)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_buttons.addWidget(self.pushButton_clear)

        self.pushButton_delete = QPushButton(self.widget_buttons)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout_buttons.addWidget(self.pushButton_delete)

        self.pushButton_edit = QPushButton(self.widget_buttons)
        self.pushButton_edit.setObjectName(u"pushButton_edit")

        self.horizontalLayout_buttons.addWidget(self.pushButton_edit)

        self.pushButton_save = QPushButton(self.widget_buttons)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout_buttons.addWidget(self.pushButton_save)


        self.verticalLayout_main.addWidget(self.widget_buttons)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e2b\u0e31\u0e2a\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e2b\u0e31\u0e2a\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e23\u0e2d\u0e01\u0e0a\u0e37\u0e48\u0e2d\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.label_lastname.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.lineEdit_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e23\u0e2d\u0e01\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.label_gender.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1e\u0e28", None))
        self.radioButton_male.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e32\u0e22", None))
        self.radioButton_female.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e0d\u0e34\u0e07", None))
        self.label_major.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e32\u0e02\u0e32\u0e27\u0e34\u0e0a\u0e32", None))
        self.comboBox_major.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0e27\u0e34\u0e17\u0e22\u0e32\u0e01\u0e32\u0e23\u0e04\u0e2d\u0e21\u0e1e\u0e34\u0e27\u0e40\u0e15\u0e2d\u0e23\u0e4c", None))
        self.comboBox_major.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e2a\u0e32\u0e23\u0e2a\u0e19\u0e40\u0e17\u0e28", None))
        self.comboBox_major.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0e27\u0e34\u0e28\u0e27\u0e01\u0e23\u0e23\u0e21\u0e0b\u0e2d\u0e1f\u0e15\u0e4c\u0e41\u0e27\u0e23\u0e4c", None))

        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e49\u0e32\u0e07", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e1a", None))
        self.pushButton_edit.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e01\u0e49\u0e44\u0e02", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
