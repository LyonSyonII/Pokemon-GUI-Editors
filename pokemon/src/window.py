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
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QTabWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 641)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.z_Title = QLabel(self.centralwidget)
        self.z_Title.setObjectName("z_Title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_Title.sizePolicy().hasHeightForWidth())
        self.z_Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Neo Euler"])
        font.setPointSize(25)
        self.z_Title.setFont(font)
        self.z_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.z_Title)

        self.z_label_3 = QLabel(self.centralwidget)
        self.z_label_3.setObjectName("z_label_3")
        self.z_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.z_label_3)

        self.combo_name = QComboBox(self.centralwidget)
        self.combo_name.setObjectName("combo_name")
        self.combo_name.setMinimumSize(QSize(150, 32))
        self.combo_name.setMaximumSize(QSize(16777215, 32))
        self.combo_name.setEditable(True)

        self.verticalLayout_2.addWidget(self.combo_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stats = QWidget(self.centralwidget)
        self.stats.setObjectName("stats")
        self.stats.setMinimumSize(QSize(305, 251))
        font1 = QFont()
        font1.setBold(False)
        self.stats.setFont(font1)
        self.gridLayout = QGridLayout(self.stats)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QWidget(self.stats)
        self.widget.setObjectName("widget")
        self.widget.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_13 = QVBoxLayout(self.widget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.z_label_12 = QLabel(self.widget)
        self.z_label_12.setObjectName("z_label_12")
        self.z_label_12.setMaximumSize(QSize(16777215, 22))
        self.z_label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.z_label_12)

        self.spin_spd = QSpinBox(self.widget)
        self.spin_spd.setObjectName("spin_spd")
        self.spin_spd.setAlignment(Qt.AlignCenter)
        self.spin_spd.setMinimum(1)
        self.spin_spd.setMaximum(255)
        self.spin_spd.setSingleStep(5)
        self.spin_spd.setValue(100)

        self.verticalLayout_13.addWidget(self.spin_spd)

        self.gridLayout.addWidget(self.widget, 3, 2, 1, 1)

        self.widget1 = QWidget(self.stats)
        self.widget1.setObjectName("widget1")
        self.widget1.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.z_label_2 = QLabel(self.widget1)
        self.z_label_2.setObjectName("z_label_2")
        self.z_label_2.setMinimumSize(QSize(0, 22))
        self.z_label_2.setMaximumSize(QSize(16777215, 22))
        self.z_label_2.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.z_label_2)

        self.combo_type1 = QComboBox(self.widget1)
        self.combo_type1.setObjectName("combo_type1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_type1.sizePolicy().hasHeightForWidth())
        self.combo_type1.setSizePolicy(sizePolicy1)
        self.combo_type1.setMinimumSize(QSize(0, 32))
        self.combo_type1.setEditable(True)
        self.combo_type1.setInsertPolicy(QComboBox.NoInsert)
        self.combo_type1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_3.addWidget(self.combo_type1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.z_label_4 = QLabel(self.widget1)
        self.z_label_4.setObjectName("z_label_4")
        self.z_label_4.setMinimumSize(QSize(0, 22))
        self.z_label_4.setMaximumSize(QSize(16777215, 22))
        self.z_label_4.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.z_label_4)

        self.combo_type2 = QComboBox(self.widget1)
        self.combo_type2.setObjectName("combo_type2")
        sizePolicy1.setHeightForWidth(self.combo_type2.sizePolicy().hasHeightForWidth())
        self.combo_type2.setSizePolicy(sizePolicy1)
        self.combo_type2.setMinimumSize(QSize(0, 32))
        self.combo_type2.setEditable(True)
        self.combo_type2.setInsertPolicy(QComboBox.NoInsert)
        self.combo_type2.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_type2.setDuplicatesEnabled(False)

        self.verticalLayout_4.addWidget(self.combo_type2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.gridLayout.addWidget(self.widget1, 0, 0, 1, 3)

        self.widget2 = QWidget(self.stats)
        self.widget2.setObjectName("widget2")
        self.widget2.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_5 = QVBoxLayout(self.widget2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.z_label = QLabel(self.widget2)
        self.z_label.setObjectName("z_label")
        self.z_label.setMinimumSize(QSize(0, 22))
        self.z_label.setMaximumSize(QSize(16777215, 22))
        self.z_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.z_label)

        self.combo_ability1 = QComboBox(self.widget2)
        self.combo_ability1.setObjectName("combo_ability1")
        sizePolicy1.setHeightForWidth(
            self.combo_ability1.sizePolicy().hasHeightForWidth()
        )
        self.combo_ability1.setSizePolicy(sizePolicy1)
        self.combo_ability1.setMinimumSize(QSize(0, 32))
        self.combo_ability1.setEditable(True)
        self.combo_ability1.setInsertPolicy(QComboBox.NoInsert)
        self.combo_ability1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_5.addWidget(self.combo_ability1)

        self.gridLayout.addWidget(self.widget2, 1, 0, 1, 1)

        self.widget3 = QWidget(self.stats)
        self.widget3.setObjectName("widget3")
        self.widget3.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_6 = QVBoxLayout(self.widget3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.z_label_5 = QLabel(self.widget3)
        self.z_label_5.setObjectName("z_label_5")
        self.z_label_5.setMinimumSize(QSize(0, 22))
        self.z_label_5.setMaximumSize(QSize(16777215, 22))
        self.z_label_5.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_6.addWidget(self.z_label_5)

        self.combo_ability2 = QComboBox(self.widget3)
        self.combo_ability2.setObjectName("combo_ability2")
        sizePolicy1.setHeightForWidth(
            self.combo_ability2.sizePolicy().hasHeightForWidth()
        )
        self.combo_ability2.setSizePolicy(sizePolicy1)
        self.combo_ability2.setMinimumSize(QSize(0, 32))
        self.combo_ability2.setEditable(True)
        self.combo_ability2.setInsertPolicy(QComboBox.NoInsert)
        self.combo_ability2.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.combo_ability2.setDuplicatesEnabled(False)

        self.verticalLayout_6.addWidget(self.combo_ability2)

        self.gridLayout.addWidget(self.widget3, 1, 1, 1, 1)

        self.widget4 = QWidget(self.stats)
        self.widget4.setObjectName("widget4")
        self.widget4.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_7 = QVBoxLayout(self.widget4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.z_label_6 = QLabel(self.widget4)
        self.z_label_6.setObjectName("z_label_6")
        self.z_label_6.setMinimumSize(QSize(0, 22))
        self.z_label_6.setMaximumSize(QSize(16777215, 22))
        self.z_label_6.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_7.addWidget(self.z_label_6)

        self.combo_ability3 = QComboBox(self.widget4)
        self.combo_ability3.setObjectName("combo_ability3")
        sizePolicy1.setHeightForWidth(
            self.combo_ability3.sizePolicy().hasHeightForWidth()
        )
        self.combo_ability3.setSizePolicy(sizePolicy1)
        self.combo_ability3.setMinimumSize(QSize(0, 32))
        self.combo_ability3.setEditable(True)
        self.combo_ability3.setInsertPolicy(QComboBox.NoInsert)
        self.combo_ability3.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_7.addWidget(self.combo_ability3)

        self.gridLayout.addWidget(self.widget4, 1, 2, 1, 1)

        self.widget5 = QWidget(self.stats)
        self.widget5.setObjectName("widget5")
        self.widget5.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_8 = QVBoxLayout(self.widget5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.z_label_7 = QLabel(self.widget5)
        self.z_label_7.setObjectName("z_label_7")
        self.z_label_7.setMaximumSize(QSize(16777215, 22))
        self.z_label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.z_label_7)

        self.spin_hp = QSpinBox(self.widget5)
        self.spin_hp.setObjectName("spin_hp")
        self.spin_hp.setAlignment(Qt.AlignCenter)
        self.spin_hp.setMinimum(1)
        self.spin_hp.setMaximum(255)
        self.spin_hp.setSingleStep(5)
        self.spin_hp.setValue(100)

        self.verticalLayout_8.addWidget(self.spin_hp)

        self.gridLayout.addWidget(self.widget5, 2, 0, 1, 1)

        self.widget6 = QWidget(self.stats)
        self.widget6.setObjectName("widget6")
        self.widget6.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_9 = QVBoxLayout(self.widget6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.z_label_9 = QLabel(self.widget6)
        self.z_label_9.setObjectName("z_label_9")
        self.z_label_9.setMaximumSize(QSize(16777215, 22))
        self.z_label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.z_label_9)

        self.spin_defense = QSpinBox(self.widget6)
        self.spin_defense.setObjectName("spin_defense")
        self.spin_defense.setAlignment(Qt.AlignCenter)
        self.spin_defense.setMinimum(1)
        self.spin_defense.setMaximum(255)
        self.spin_defense.setSingleStep(5)
        self.spin_defense.setValue(100)

        self.verticalLayout_9.addWidget(self.spin_defense)

        self.gridLayout.addWidget(self.widget6, 2, 1, 1, 1)

        self.widget7 = QWidget(self.stats)
        self.widget7.setObjectName("widget7")
        self.widget7.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_10 = QVBoxLayout(self.widget7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.z_label_11 = QLabel(self.widget7)
        self.z_label_11.setObjectName("z_label_11")
        self.z_label_11.setMaximumSize(QSize(16777215, 22))
        self.z_label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.z_label_11)

        self.spin_sp_def = QSpinBox(self.widget7)
        self.spin_sp_def.setObjectName("spin_sp_def")
        self.spin_sp_def.setAlignment(Qt.AlignCenter)
        self.spin_sp_def.setMinimum(1)
        self.spin_sp_def.setMaximum(255)
        self.spin_sp_def.setSingleStep(5)
        self.spin_sp_def.setValue(100)

        self.verticalLayout_10.addWidget(self.spin_sp_def)

        self.gridLayout.addWidget(self.widget7, 2, 2, 1, 1)

        self.widget8 = QWidget(self.stats)
        self.widget8.setObjectName("widget8")
        self.widget8.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_11 = QVBoxLayout(self.widget8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.z_label_8 = QLabel(self.widget8)
        self.z_label_8.setObjectName("z_label_8")
        self.z_label_8.setMaximumSize(QSize(16777215, 22))
        self.z_label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.z_label_8)

        self.spin_atk = QSpinBox(self.widget8)
        self.spin_atk.setObjectName("spin_atk")
        self.spin_atk.setAlignment(Qt.AlignCenter)
        self.spin_atk.setMinimum(1)
        self.spin_atk.setMaximum(255)
        self.spin_atk.setSingleStep(5)
        self.spin_atk.setValue(100)

        self.verticalLayout_11.addWidget(self.spin_atk)

        self.gridLayout.addWidget(self.widget8, 3, 0, 1, 1)

        self.widget9 = QWidget(self.stats)
        self.widget9.setObjectName("widget9")
        self.widget9.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_12 = QVBoxLayout(self.widget9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.z_label_10 = QLabel(self.widget9)
        self.z_label_10.setObjectName("z_label_10")
        self.z_label_10.setMaximumSize(QSize(16777215, 22))
        self.z_label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.z_label_10)

        self.spin_sp_atk = QSpinBox(self.widget9)
        self.spin_sp_atk.setObjectName("spin_sp_atk")
        self.spin_sp_atk.setAlignment(Qt.AlignCenter)
        self.spin_sp_atk.setMinimum(1)
        self.spin_sp_atk.setMaximum(255)
        self.spin_sp_atk.setSingleStep(5)
        self.spin_sp_atk.setValue(100)

        self.verticalLayout_12.addWidget(self.spin_sp_atk)

        self.gridLayout.addWidget(self.widget9, 3, 1, 1, 1)

        self.horizontalLayout.addWidget(self.stats)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_moves = QWidget()
        self.tab_moves.setObjectName("tab_moves")
        self.verticalLayout = QVBoxLayout(self.tab_moves)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree_moves = QTreeWidget(self.tab_moves)
        self.tree_moves.setObjectName("tree_moves")
        self.tree_moves.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tree_moves.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tree_moves.setProperty("showDropIndicator", False)
        self.tree_moves.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tree_moves.setRootIsDecorated(False)
        self.tree_moves.setUniformRowHeights(True)
        self.tree_moves.setItemsExpandable(False)
        self.tree_moves.setSortingEnabled(True)
        self.tree_moves.setExpandsOnDoubleClick(False)

        self.verticalLayout.addWidget(self.tree_moves)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_add_move = QPushButton(self.tab_moves)
        self.button_add_move.setObjectName("button_add_move")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.button_add_move.setFont(font2)
        self.button_add_move.setStyleSheet("QPushButton {color: #0dff00;}")
        self.button_add_move.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.button_add_move)

        self.button_remove_move = QPushButton(self.tab_moves)
        self.button_remove_move.setObjectName("button_remove_move")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        self.button_remove_move.setFont(font3)
        self.button_remove_move.setStyleSheet(
            "QPushButton {\n" "	color: rgb(255, 0, 4);\n" "	text-align: center\n" "}"
        )
        self.button_remove_move.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.button_remove_move)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_moves, "")
        self.tab_evolutions = QWidget()
        self.tab_evolutions.setObjectName("tab_evolutions")
        self.tabWidget.addTab(self.tab_evolutions, "")
        self.tab_misc = QWidget()
        self.tab_misc.setObjectName("tab_misc")
        self.tabWidget.addTab(self.tab_misc, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_cancel = QPushButton(self.centralwidget)
        self.button_cancel.setObjectName("button_cancel")
        self.button_cancel.setMaximumSize(QSize(91, 32))
        self.button_cancel.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.button_cancel)

        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.button_save.setMaximumSize(QSize(91, 32))

        self.horizontalLayout_3.addWidget(self.button_save)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.combo_name, self.combo_type1)
        QWidget.setTabOrder(self.combo_type1, self.combo_type2)
        QWidget.setTabOrder(self.combo_type2, self.combo_ability1)
        QWidget.setTabOrder(self.combo_ability1, self.combo_ability2)
        QWidget.setTabOrder(self.combo_ability2, self.combo_ability3)
        QWidget.setTabOrder(self.combo_ability3, self.spin_hp)
        QWidget.setTabOrder(self.spin_hp, self.spin_defense)
        QWidget.setTabOrder(self.spin_defense, self.spin_sp_def)
        QWidget.setTabOrder(self.spin_sp_def, self.spin_atk)
        QWidget.setTabOrder(self.spin_atk, self.spin_sp_atk)
        QWidget.setTabOrder(self.spin_sp_atk, self.spin_spd)
        QWidget.setTabOrder(self.spin_spd, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tree_moves)
        QWidget.setTabOrder(self.tree_moves, self.button_add_move)
        QWidget.setTabOrder(self.button_add_move, self.button_remove_move)
        QWidget.setTabOrder(self.button_remove_move, self.button_cancel)
        QWidget.setTabOrder(self.button_cancel, self.button_save)

        self.retranslateUi(MainWindow)

        self.combo_type1.setCurrentIndex(-1)
        self.combo_type2.setCurrentIndex(-1)
        self.combo_ability1.setCurrentIndex(-1)
        self.combo_ability2.setCurrentIndex(-1)
        self.combo_ability3.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.z_Title.setText(
            QCoreApplication.translate("MainWindow", "Pok\u00e9mon Editor", None)
        )
        self.z_label_3.setText(QCoreApplication.translate("MainWindow", "Name", None))
        self.combo_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name", None)
        )
        self.z_label_12.setText(QCoreApplication.translate("MainWindow", "Spd", None))
        self.z_label_2.setText(QCoreApplication.translate("MainWindow", "Type 1", None))
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
        self.z_label_4.setText(QCoreApplication.translate("MainWindow", "Type 2", None))
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
        self.z_label.setText(
            QCoreApplication.translate("MainWindow", "Ability 1", None)
        )
        # if QT_CONFIG(tooltip)
        self.combo_ability1.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>First Type</p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.combo_ability1.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "None", None)
        )
        self.z_label_5.setText(
            QCoreApplication.translate("MainWindow", "Ability 2", None)
        )
        # if QT_CONFIG(tooltip)
        self.combo_ability2.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>First Type</p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.combo_ability2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "None", None)
        )
        self.z_label_6.setText(QCoreApplication.translate("MainWindow", "Hidden", None))
        # if QT_CONFIG(tooltip)
        self.combo_ability3.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p>First Type</p></body></html>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.combo_ability3.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "None", None)
        )
        self.z_label_7.setText(QCoreApplication.translate("MainWindow", "Hp", None))
        self.z_label_9.setText(QCoreApplication.translate("MainWindow", "Def", None))
        self.z_label_11.setText(
            QCoreApplication.translate("MainWindow", "Sp. Def", None)
        )
        self.z_label_8.setText(QCoreApplication.translate("MainWindow", "Atk", None))
        self.z_label_10.setText(
            QCoreApplication.translate("MainWindow", "Sp. Atk", None)
        )
        ___qtreewidgetitem = self.tree_moves.headerItem()
        ___qtreewidgetitem.setText(
            1, QCoreApplication.translate("MainWindow", "Move", None)
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "Level", None)
        )
        self.button_add_move.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.button_remove_move.setText(
            QCoreApplication.translate("MainWindow", "-", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_moves),
            QCoreApplication.translate("MainWindow", "Moves", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_evolutions),
            QCoreApplication.translate("MainWindow", "Evolutions", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_misc),
            QCoreApplication.translate("MainWindow", "Misc", None),
        )
        self.button_cancel.setText(
            QCoreApplication.translate("MainWindow", "Close", None)
        )
        self.button_save.setText(QCoreApplication.translate("MainWindow", "Save", None))

    # retranslateUi
