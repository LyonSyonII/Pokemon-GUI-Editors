# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QSplitter,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 761)
        MainWindow.setMinimumSize(QSize(376, 697))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setMaximumSize(QSize(16777215, 370))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ATitle = QLabel(self.widget)
        self.ATitle.setObjectName("ATitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ATitle.sizePolicy().hasHeightForWidth())
        self.ATitle.setSizePolicy(sizePolicy)
        self.ATitle.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies(["Neo Euler"])
        font.setPointSize(25)
        self.ATitle.setFont(font)
        self.ATitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ATitle)

        self.fields = QWidget(self.widget)
        self.fields.setObjectName("fields")
        sizePolicy.setHeightForWidth(self.fields.sizePolicy().hasHeightForWidth())
        self.fields.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.fields)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_9 = QSplitter(self.fields)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_9.setMaximumSize(QSize(16777215, 73))
        self.splitter_9.setOrientation(Qt.Vertical)
        self.label_5 = QLabel(self.splitter_9)
        self.label_5.setObjectName("label_5")
        self.label_5.setMinimumSize(QSize(0, 22))
        self.label_5.setMaximumSize(QSize(16777215, 22))
        self.label_5.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.splitter_9.addWidget(self.label_5)
        self.combo_category = QComboBox(self.splitter_9)
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.setObjectName("combo_category")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.combo_category.sizePolicy().hasHeightForWidth()
        )
        self.combo_category.setSizePolicy(sizePolicy1)
        self.combo_category.setMinimumSize(QSize(0, 32))
        self.combo_category.setMaximumSize(QSize(16777215, 50))
        self.combo_category.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.splitter_9.addWidget(self.combo_category)

        self.gridLayout.addWidget(self.splitter_9, 1, 2, 1, 1)

        self.splitter_7 = QSplitter(self.fields)
        self.splitter_7.setObjectName("splitter_7")
        self.splitter_7.setMaximumSize(QSize(16777215, 73))
        self.splitter_7.setOrientation(Qt.Vertical)
        self.label_6 = QLabel(self.splitter_7)
        self.label_6.setObjectName("label_6")
        self.label_6.setMinimumSize(QSize(0, 22))
        self.label_6.setMaximumSize(QSize(16777215, 22))
        self.label_6.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.splitter_7.addWidget(self.label_6)
        self.spin_pp = QSpinBox(self.splitter_7)
        self.spin_pp.setObjectName("spin_pp")
        sizePolicy1.setHeightForWidth(self.spin_pp.sizePolicy().hasHeightForWidth())
        self.spin_pp.setSizePolicy(sizePolicy1)
        self.spin_pp.setMaximumSize(QSize(16777215, 50))
        self.spin_pp.setValue(10)
        self.splitter_7.addWidget(self.spin_pp)

        self.gridLayout.addWidget(self.splitter_7, 2, 3, 1, 1)

        self.splitter_3 = QSplitter(self.fields)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_3.setMaximumSize(QSize(16777215, 73))
        self.splitter_3.setOrientation(Qt.Vertical)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setMinimumSize(QSize(0, 22))
        self.label_3.setMaximumSize(QSize(16777215, 22))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.splitter_3.addWidget(self.label_3)
        self.combo_name = QComboBox(self.splitter_3)
        self.combo_name.setObjectName("combo_name")
        self.combo_name.setMinimumSize(QSize(150, 32))
        self.combo_name.setMaximumSize(QSize(16777215, 50))
        self.combo_name.setEditable(True)
        self.splitter_3.addWidget(self.combo_name)

        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 4)

        self.splitter = QSplitter(self.fields)
        self.splitter.setObjectName("splitter")
        self.splitter.setMaximumSize(QSize(16777215, 73))
        self.splitter.setOrientation(Qt.Vertical)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(0, 22))
        self.label_4.setMaximumSize(QSize(16777215, 22))
        self.label_4.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.splitter.addWidget(self.label_4)
        self.combo_type2 = QComboBox(self.splitter)
        self.combo_type2.setObjectName("combo_type2")
        sizePolicy1.setHeightForWidth(self.combo_type2.sizePolicy().hasHeightForWidth())
        self.combo_type2.setSizePolicy(sizePolicy1)
        self.combo_type2.setMinimumSize(QSize(0, 32))
        self.combo_type2.setMaximumSize(QSize(16777215, 50))
        self.combo_type2.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_type2.setDuplicatesEnabled(False)
        self.splitter.addWidget(self.combo_type2)

        self.gridLayout.addWidget(self.splitter, 1, 1, 1, 1)

        self.splitter_4 = QSplitter(self.fields)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_4.setMaximumSize(QSize(16777215, 73))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_9 = QLabel(self.splitter_4)
        self.label_9.setObjectName("label_9")
        self.label_9.setMinimumSize(QSize(0, 22))
        self.label_9.setMaximumSize(QSize(16777215, 22))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.splitter_4.addWidget(self.label_9)
        self.combo_target = QComboBox(self.splitter_4)
        self.combo_target.addItem("")
        self.combo_target.addItem("")
        self.combo_target.addItem("")
        self.combo_target.setObjectName("combo_target")
        self.combo_target.setMinimumSize(QSize(100, 32))
        self.combo_target.setMaximumSize(QSize(16777215, 50))
        self.combo_target.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.splitter_4.addWidget(self.combo_target)

        self.gridLayout.addWidget(self.splitter_4, 2, 0, 1, 1)

        self.splitter_5 = QSplitter(self.fields)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_5.setMaximumSize(QSize(16777215, 73))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_10 = QLabel(self.splitter_5)
        self.label_10.setObjectName("label_10")
        self.label_10.setMinimumSize(QSize(0, 22))
        self.label_10.setMaximumSize(QSize(16777215, 22))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.splitter_5.addWidget(self.label_10)
        self.spin_priority = QSpinBox(self.splitter_5)
        self.spin_priority.setObjectName("spin_priority")
        sizePolicy1.setHeightForWidth(
            self.spin_priority.sizePolicy().hasHeightForWidth()
        )
        self.spin_priority.setSizePolicy(sizePolicy1)
        self.spin_priority.setMaximumSize(QSize(16777215, 50))
        self.spin_priority.setMinimum(-6)
        self.spin_priority.setMaximum(6)
        self.spin_priority.setValue(0)
        self.splitter_5.addWidget(self.spin_priority)

        self.gridLayout.addWidget(self.splitter_5, 2, 1, 1, 1)

        self.splitter_2 = QSplitter(self.fields)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_2.setMaximumSize(QSize(16777215, 73))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(0, 22))
        self.label_2.setMaximumSize(QSize(16777215, 22))
        self.label_2.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.splitter_2.addWidget(self.label_2)
        self.combo_type1 = QComboBox(self.splitter_2)
        self.combo_type1.setObjectName("combo_type1")
        sizePolicy1.setHeightForWidth(self.combo_type1.sizePolicy().hasHeightForWidth())
        self.combo_type1.setSizePolicy(sizePolicy1)
        self.combo_type1.setMinimumSize(QSize(0, 32))
        self.combo_type1.setMaximumSize(QSize(16777215, 50))
        self.combo_type1.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.splitter_2.addWidget(self.combo_type1)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.splitter_6 = QSplitter(self.fields)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter_6.setMaximumSize(QSize(16777215, 73))
        self.splitter_6.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter_6)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(0, 22))
        self.label.setMaximumSize(QSize(16777215, 22))
        self.label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.splitter_6.addWidget(self.label)
        self.spin_power = QSpinBox(self.splitter_6)
        self.spin_power.setObjectName("spin_power")
        sizePolicy1.setHeightForWidth(self.spin_power.sizePolicy().hasHeightForWidth())
        self.spin_power.setSizePolicy(sizePolicy1)
        self.spin_power.setMaximumSize(QSize(16777215, 50))
        self.spin_power.setMinimum(0)
        self.spin_power.setMaximum(1000)
        self.spin_power.setSingleStep(10)
        self.spin_power.setValue(70)
        self.splitter_6.addWidget(self.spin_power)

        self.gridLayout.addWidget(self.splitter_6, 2, 2, 1, 1)

        self.splitter_8 = QSplitter(self.fields)
        self.splitter_8.setObjectName("splitter_8")
        self.splitter_8.setMaximumSize(QSize(16777215, 73))
        self.splitter_8.setOrientation(Qt.Vertical)
        self.label_7 = QLabel(self.splitter_8)
        self.label_7.setObjectName("label_7")
        self.label_7.setMinimumSize(QSize(0, 22))
        self.label_7.setMaximumSize(QSize(16777215, 22))
        self.label_7.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.splitter_8.addWidget(self.label_7)
        self.spin_accuracy = QSpinBox(self.splitter_8)
        self.spin_accuracy.setObjectName("spin_accuracy")
        sizePolicy1.setHeightForWidth(
            self.spin_accuracy.sizePolicy().hasHeightForWidth()
        )
        self.spin_accuracy.setSizePolicy(sizePolicy1)
        self.spin_accuracy.setMaximumSize(QSize(16777215, 50))
        self.spin_accuracy.setMaximum(100)
        self.spin_accuracy.setSingleStep(10)
        self.spin_accuracy.setValue(100)
        self.splitter_8.addWidget(self.spin_accuracy)

        self.gridLayout.addWidget(self.splitter_8, 1, 3, 1, 1)

        self.verticalLayout_2.addWidget(self.fields)

        self.verticalLayout_12.addWidget(self.widget)

        self.flagsdescr = QWidget(self.centralwidget)
        self.flagsdescr.setObjectName("flagsdescr")
        self.flagsdescr.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.flagsdescr)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_10 = QSplitter(self.flagsdescr)
        self.splitter_10.setObjectName("splitter_10")
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.splitter_10.setOpaqueResize(False)
        self.flagsBox = QGroupBox(self.splitter_10)
        self.flagsBox.setObjectName("flagsBox")
        self.flagsBox.setMaximumSize(QSize(300, 16777215))
        self.flagsBox.setLayoutDirection(Qt.RightToLeft)
        self.flagsBox.setStyleSheet(
            "QGroupBox::title {\n"
            "    subcontrol-origin: padding;\n"
            "    left: 30px;\n"
            "    subcontrol-position: top left; \n"
            "}"
        )
        self.flagsBox.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)
        self.verticalLayout = QVBoxLayout(self.flagsBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_flag_a = QCheckBox(self.flagsBox)
        self.check_flag_a.setObjectName("check_flag_a")
        self.check_flag_a.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_a.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_a)

        self.check_flag_b = QCheckBox(self.flagsBox)
        self.check_flag_b.setObjectName("check_flag_b")
        self.check_flag_b.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_b.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_b)

        self.check_flag_c = QCheckBox(self.flagsBox)
        self.check_flag_c.setObjectName("check_flag_c")
        self.check_flag_c.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_c.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_c)

        self.check_flag_d = QCheckBox(self.flagsBox)
        self.check_flag_d.setObjectName("check_flag_d")
        self.check_flag_d.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_d.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_d)

        self.check_flag_e = QCheckBox(self.flagsBox)
        self.check_flag_e.setObjectName("check_flag_e")
        self.check_flag_e.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_e.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_e)

        self.check_flag_f = QCheckBox(self.flagsBox)
        self.check_flag_f.setObjectName("check_flag_f")
        self.check_flag_f.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_f.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_f)

        self.check_flag_g = QCheckBox(self.flagsBox)
        self.check_flag_g.setObjectName("check_flag_g")
        self.check_flag_g.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_g.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_g)

        self.check_flag_h = QCheckBox(self.flagsBox)
        self.check_flag_h.setObjectName("check_flag_h")
        self.check_flag_h.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_h.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_h)

        self.check_flag_i = QCheckBox(self.flagsBox)
        self.check_flag_i.setObjectName("check_flag_i")
        self.check_flag_i.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_i.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_i)

        self.check_flag_j = QCheckBox(self.flagsBox)
        self.check_flag_j.setObjectName("check_flag_j")
        self.check_flag_j.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_j.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_j)

        self.check_flag_k = QCheckBox(self.flagsBox)
        self.check_flag_k.setObjectName("check_flag_k")
        self.check_flag_k.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_k.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_k)

        self.check_flag_l = QCheckBox(self.flagsBox)
        self.check_flag_l.setObjectName("check_flag_l")
        self.check_flag_l.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_l.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_l)

        self.check_flag_m = QCheckBox(self.flagsBox)
        self.check_flag_m.setObjectName("check_flag_m")
        self.check_flag_m.setLayoutDirection(Qt.RightToLeft)
        self.check_flag_m.setTristate(False)

        self.verticalLayout.addWidget(self.check_flag_m)

        self.splitter_10.addWidget(self.flagsBox)
        self.groupBox_2 = QGroupBox(self.splitter_10)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_2.setStyleSheet(
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center; \n"
            "}"
        )
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txtedit_description = QTextEdit(self.groupBox_2)
        self.txtedit_description.setObjectName("txtedit_description")
        sizePolicy.setHeightForWidth(
            self.txtedit_description.sizePolicy().hasHeightForWidth()
        )
        self.txtedit_description.setSizePolicy(sizePolicy)
        self.txtedit_description.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.txtedit_description)

        self.splitter_10.addWidget(self.groupBox_2)

        self.horizontalLayout_2.addWidget(self.splitter_10)

        self.verticalLayout_12.addWidget(self.flagsdescr)

        self.saveclose = QWidget(self.centralwidget)
        self.saveclose.setObjectName("saveclose")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.saveclose.sizePolicy().hasHeightForWidth())
        self.saveclose.setSizePolicy(sizePolicy2)
        self.saveclose.setMaximumSize(QSize(180, 32))
        self.horizontalLayout = QHBoxLayout(self.saveclose)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.button_cancel = QPushButton(self.saveclose)
        self.button_cancel.setObjectName("button_cancel")
        self.button_cancel.setMaximumSize(QSize(91, 32))

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_save = QPushButton(self.saveclose)
        self.button_save.setObjectName("button_save")
        self.button_save.setMaximumSize(QSize(91, 32))

        self.horizontalLayout.addWidget(self.button_save)

        self.verticalLayout_12.addWidget(self.saveclose, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.combo_type2, self.combo_category)
        QWidget.setTabOrder(self.combo_category, self.spin_accuracy)
        QWidget.setTabOrder(self.spin_accuracy, self.combo_target)
        QWidget.setTabOrder(self.combo_target, self.spin_priority)
        QWidget.setTabOrder(self.spin_priority, self.spin_power)
        QWidget.setTabOrder(self.spin_power, self.spin_pp)
        QWidget.setTabOrder(self.spin_pp, self.check_flag_a)
        QWidget.setTabOrder(self.check_flag_a, self.check_flag_b)
        QWidget.setTabOrder(self.check_flag_b, self.check_flag_c)
        QWidget.setTabOrder(self.check_flag_c, self.check_flag_d)
        QWidget.setTabOrder(self.check_flag_d, self.check_flag_e)
        QWidget.setTabOrder(self.check_flag_e, self.check_flag_f)
        QWidget.setTabOrder(self.check_flag_f, self.check_flag_g)
        QWidget.setTabOrder(self.check_flag_g, self.check_flag_h)
        QWidget.setTabOrder(self.check_flag_h, self.check_flag_i)
        QWidget.setTabOrder(self.check_flag_i, self.check_flag_j)
        QWidget.setTabOrder(self.check_flag_j, self.check_flag_k)
        QWidget.setTabOrder(self.check_flag_k, self.check_flag_l)
        QWidget.setTabOrder(self.check_flag_l, self.check_flag_m)
        QWidget.setTabOrder(self.check_flag_m, self.txtedit_description)
        QWidget.setTabOrder(self.txtedit_description, self.button_cancel)
        QWidget.setTabOrder(self.button_cancel, self.button_save)

        self.retranslateUi(MainWindow)

        self.combo_type2.setCurrentIndex(-1)
        self.combo_target.setCurrentIndex(2)
        self.combo_type1.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.ATitle.setText(
            QCoreApplication.translate("MainWindow", "Move Editor", None)
        )
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Category", None))
        self.combo_category.setItemText(
            0, QCoreApplication.translate("MainWindow", "Physical", None)
        )
        self.combo_category.setItemText(
            1, QCoreApplication.translate("MainWindow", "Special", None)
        )
        self.combo_category.setItemText(
            2, QCoreApplication.translate("MainWindow", "Status", None)
        )

        self.label_6.setText(QCoreApplication.translate("MainWindow", "PP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Name", None))
        self.combo_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name", None)
        )
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Type 2", None))
        # if QT_CONFIG(tooltip)
        self.combo_type2.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>First Type</p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.combo_type2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "None", None)
        )
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Target", None))
        self.combo_target.setItemText(
            0, QCoreApplication.translate("MainWindow", "Automatic", None)
        )
        self.combo_target.setItemText(
            1, QCoreApplication.translate("MainWindow", "UserOrAlly", None)
        )
        self.combo_target.setItemText(
            2, QCoreApplication.translate("MainWindow", "AnyFoe", None)
        )

        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Priority", None)
        )
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Type 1", None))
        # if QT_CONFIG(tooltip)
        self.combo_type1.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>First Type</p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.combo_type1.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "None", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "Power", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Accuracy", None))
        self.spin_accuracy.setSuffix(
            QCoreApplication.translate("MainWindow", "%", None)
        )
        self.flagsBox.setTitle(QCoreApplication.translate("MainWindow", "Flags", None))
        self.check_flag_a.setText(
            QCoreApplication.translate("MainWindow", "Contact", None)
        )
        self.check_flag_b.setText(
            QCoreApplication.translate("MainWindow", "Bypasses Protect", None)
        )
        self.check_flag_c.setText(
            QCoreApplication.translate("MainWindow", "Status Only", None)
        )
        self.check_flag_d.setText(
            QCoreApplication.translate("MainWindow", "Buff/Debuf", None)
        )
        self.check_flag_e.setText(
            QCoreApplication.translate("MainWindow", "Removes Frozen", None)
        )
        self.check_flag_f.setText(
            QCoreApplication.translate("MainWindow", "High Critical Rate", None)
        )
        self.check_flag_g.setText(
            QCoreApplication.translate("MainWindow", "Bite Move", None)
        )
        self.check_flag_h.setText(
            QCoreApplication.translate("MainWindow", "Punch Move", None)
        )
        self.check_flag_i.setText(
            QCoreApplication.translate("MainWindow", "Sound Move", None)
        )
        self.check_flag_j.setText(
            QCoreApplication.translate("MainWindow", "Powder Move", None)
        )
        self.check_flag_k.setText(
            QCoreApplication.translate("MainWindow", "Pulse Move", None)
        )
        self.check_flag_l.setText(
            QCoreApplication.translate("MainWindow", "Bullet Move", None)
        )
        self.check_flag_m.setText(
            QCoreApplication.translate("MainWindow", "Dance Move", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Description", None)
        )
        self.txtedit_description.setPlaceholderText("")
        self.button_cancel.setText(
            QCoreApplication.translate("MainWindow", "Close", None)
        )
        self.button_save.setText(QCoreApplication.translate("MainWindow", "Save", None))

    # retranslateUi
