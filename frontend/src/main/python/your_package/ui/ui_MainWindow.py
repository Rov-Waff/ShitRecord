# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_account = QPushButton(Form)
        self.btn_account.setObjectName(u"btn_account")

        self.horizontalLayout.addWidget(self.btn_account)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(33)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_total = QLabel(Form)
        self.lb_total.setObjectName(u"lb_total")

        self.horizontalLayout_2.addWidget(self.lb_total)

        self.lb_today = QLabel(Form)
        self.lb_today.setObjectName(u"lb_today")

        self.horizontalLayout_2.addWidget(self.lb_today)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btn_rec = QPushButton(Form)
        self.btn_rec.setObjectName(u"btn_rec")

        self.verticalLayout.addWidget(self.btn_rec)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5982\u5395\u8bb0\u5f55\u5668", None))
        self.btn_account.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5982\u5395\u8bb0\u5f55\u5668", None))
        self.lb_total.setText(QCoreApplication.translate("Form", u"\u7d2f\u8bb0\u5982\u5395\uff1a", None))
        self.lb_today.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5982\u5395\uff1a", None))
        self.btn_rec.setText(QCoreApplication.translate("Form", u"\u8bb0\u5f55\u5982\u5395", None))
    # retranslateUi

