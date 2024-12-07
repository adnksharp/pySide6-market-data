# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1042, 378)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.symbol = QLineEdit(Widget)
        self.symbol.setObjectName(u"symbol")
        sizePolicy.setHeightForWidth(self.symbol.sizePolicy().hasHeightForWidth())
        self.symbol.setSizePolicy(sizePolicy)
        self.symbol.setStyleSheet(u"background-color: #000; color: #5bf2fa;")
        self.symbol.setFrame(False)

        self.horizontalLayout.addWidget(self.symbol)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation))
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.name = QLabel(Widget)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.name)

        self.search = QPushButton(Widget)
        self.search.setObjectName(u"search")
        self.search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search.setMouseTracking(True)
        self.search.setTabletTracking(True)
        self.search.setStyleSheet(u"background-color: #000; color: #5bf2fa;")
        self.search.setFlat(True)

        self.horizontalLayout.addWidget(self.search)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.period = QComboBox(Widget)
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.setObjectName(u"period")

        self.horizontalLayout_2.addWidget(self.period)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.interval = QComboBox(Widget)
        self.interval.addItem("")
        self.interval.addItem("")
        self.interval.addItem("")
        self.interval.addItem("")
        self.interval.addItem("")
        self.interval.setObjectName(u"interval")

        self.horizontalLayout_2.addWidget(self.interval)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Widget)

        self.period.setCurrentIndex(7)
        self.interval.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Tickers", None))
        self.label.setText(QCoreApplication.translate("Widget", u"S\u00edmbolo:", None))
        self.symbol.setText("")
        self.pushButton.setText("")
        self.name.setText("")
        self.search.setText(QCoreApplication.translate("Widget", u"buscar", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Periodo:", None))
        self.period.setItemText(0, QCoreApplication.translate("Widget", u"1 d\u00eda", None))
        self.period.setItemText(1, QCoreApplication.translate("Widget", u"5 d\u00edas", None))
        self.period.setItemText(2, QCoreApplication.translate("Widget", u"1 mes", None))
        self.period.setItemText(3, QCoreApplication.translate("Widget", u"3 meses", None))
        self.period.setItemText(4, QCoreApplication.translate("Widget", u"6 meses", None))
        self.period.setItemText(5, QCoreApplication.translate("Widget", u"1 a\u00f1o", None))
        self.period.setItemText(6, QCoreApplication.translate("Widget", u"2 a\u00f1os", None))
        self.period.setItemText(7, QCoreApplication.translate("Widget", u"En lo que va del a\u00f1o", None))
        self.period.setItemText(8, QCoreApplication.translate("Widget", u"M\u00e1ximo", None))

        self.label_3.setText(QCoreApplication.translate("Widget", u" Intervalo:", None))
        self.interval.setItemText(0, QCoreApplication.translate("Widget", u"1d", None))
        self.interval.setItemText(1, QCoreApplication.translate("Widget", u"5d", None))
        self.interval.setItemText(2, QCoreApplication.translate("Widget", u"1wk", None))
        self.interval.setItemText(3, QCoreApplication.translate("Widget", u"1mo", None))
        self.interval.setItemText(4, QCoreApplication.translate("Widget", u"3mo", None))

        self.interval.setCurrentText(QCoreApplication.translate("Widget", u"1wk", None))
        self.label_4.setText("")
    # retranslateUi

