from ctypes import cast
import sys
from os.path import dirname, abspath
from typing import Any, Sequence, Tuple, KeysView
from pathlib import Path

import tomli as toml
import tomli_w as toml_w
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
    QSpinBox,
    QComboBox,
    QWidget,
)
from PySide6 import QtGui
from window import Ui_MainWindow


def under_to_space(text: str) -> str:
    return text.replace("_", " ")


class SpinBox(QSpinBox, QWidget):
    def wheelEvent(self, event: QtGui.QWheelEvent):
        event.ignore()


class ComboBox(QComboBox, QWidget):
    def wheelEvent(self, event: QtGui.QWheelEvent):
        event.ignore()


class Window(QMainWindow, Ui_MainWindow):
    root_path: Path
    pkm_path: Path
    pkm_parse: dict[str, dict[str, dict[str, Any]]]
    pkm: dict[str, dict[str, Any]]
    pkm_items: Sequence[str]
    move_items: Sequence[str]
    item_items: Sequence[str]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_slots()

        # Get root path based on type of executable
        if getattr(sys, "frozen", False):
            self.root_path = Path(sys.executable).parent
        else:
            self.root_path = Path(dirname(abspath(__file__)))

        # If path does not exist, ask the user to select it
        (self.root_path, self.pkm_path) = self.get_file_path("pokemon.toml.bytes")

        # Load pokemon.toml
        self.pkm_parse = toml.load(self.pkm_path)
        self.pkm_parse.setdefault("Pokemon", {})
        self.pkm = self.pkm_parse["Pokemon"]

        # Add existing Pokemon to the "Name" entry
        self.pkm_items = list(map(under_to_space, self.pkm.keys()))
        self.combo_name.addItems([under_to_space(p) for p in self.pkm.keys()])

        # Save existing moves for later entries
        moves_path = self.get_file_path("moves.toml.bytes")[1]
        moves: KeysView[str] = toml.load(moves_path).get("Moves", {}).keys()
        self.move_items = [under_to_space(move) for move in moves]

        # Save existing items for later entries
        items_path = self.get_file_path("items.toml.bytes")[1]
        items: KeysView[str] = toml.load(items_path).get("Items", {}).keys()
        self.item_items = [under_to_space(item) for item in items]

        # Add existing abilities to the corresponding entries
        abilities_path = self.get_file_path("abilities.toml.bytes")[1]
        abilities = [
            under_to_space(a)
            for a in self.load_toml(abilities_path).get("Abilities", {}).keys()
        ]
        self.combo_ability1.addItems(abilities)
        self.combo_ability2.addItems(abilities)
        self.combo_ability3.addItems(abilities)

        # Add existing types to the "Type 1" and "Type 2" entries
        types_path = self.get_file_path("types.toml.bytes")[1]
        if types := toml.load(types_path).get("Types"):
            self.combo_type1.addItems(types.keys())
            self.combo_type2.addItems(types.keys())

    def connect_slots(self):
        self.combo_name.currentTextChanged.connect(self.name_changed)  # type: ignore
        self.button_save.clicked.connect(self.save_poke)  # type: ignore
        self.button_cancel.clicked.connect(self.close)  # type: ignore
        self.button_add_move.clicked.connect(self.add_move_item)  # type: ignore
        self.button_remove_move.clicked.connect(lambda: self.remove_tree_item(self.tree_moves))  # type: ignore
        self.button_add_evolution.clicked.connect(self.add_evolution_item)  # type: ignore
        self.button_remove_evolution.clicked.connect(lambda: self.remove_tree_item(self.tree_evolutions))  # type: ignore

    def name_changed(self):
        text = self.combo_name.currentText()
        # If move is found in dictionary
        if pkm := self.pkm.get(text.replace(" ", "_")):
            self.combo_type1.setCurrentText(pkm["type1"])
            self.combo_type2.setCurrentText(pkm["type2"])
            # Add stats
            self.spin_hp.setValue(pkm.get("hp", 0))
            self.spin_atk.setValue(pkm.get("atk", 0))
            self.spin_defense.setValue(pkm.get("def", 0))
            self.spin_sp_atk.setValue(pkm.get("sp_atk", 0))
            self.spin_sp_def.setValue(pkm.get("sp_def", 0))
            self.spin_spd.setValue(pkm.get("speed", 0))
            # Remove current moves
            for _ in range(self.tree_moves.topLevelItemCount()):
                self.tree_moves.takeTopLevelItem(0)
            # Add new moves
            for move in pkm["moves"]:
                self.add_move_item(move["lvl"], move["move"])

    def add_move_item(self, level: int = 1, move: str | None = None):
        # Get current item
        i = self.tree_moves.topLevelItemCount()
        # Create level spinbox with the needed properties
        spin_level = SpinBox()
        spin_level.setMaximum(100)
        spin_level.setMinimum(0)
        spin_level.setValue(level)
        spin_level.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        # Create move combobox with the needed properties
        combo_move = ComboBox()
        combo_move.setEditable(True)
        combo_move.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        combo_move.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        combo_move.setPlaceholderText("Select move")
        if move:
            combo_move.setCurrentText(move)
        combo_move.addItems(self.move_items)
        # Add both to the tree
        self.tree_moves.insertTopLevelItem(i, QTreeWidgetItem())
        self.tree_moves.setItemWidget(self.tree_moves.topLevelItem(i), 0, spin_level)
        self.tree_moves.setItemWidget(self.tree_moves.topLevelItem(i), 1, combo_move)

    def add_evolution_item(self, pkm: str | None = None, evo_method: str | None = None):
        # Get current item
        i = self.tree_evolutions.topLevelItemCount()
        # Create pokemon combobox with the needed properties
        combo_pkm = ComboBox()
        combo_pkm.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        combo_pkm.setEditable(True)
        combo_pkm.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        combo_pkm.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        combo_pkm.setPlaceholderText("Select Pokémon")
        combo_pkm.addItems(self.pkm_items)
        if pkm:
            combo_pkm.setCurrentText(pkm)

        # Create evolution method combobox with the needed properties
        combo_method = ComboBox()
        combo_method.setEditable(True)
        combo_method.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        combo_method.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        combo_method.setPlaceholderText("Select move")
        combo_method.addItems(["Level", "Item", "Custom"])
        if evo_method:
            combo_method.setCurrentText(evo_method)
        else:
            combo_method.setCurrentIndex(0)
        combo_method.currentTextChanged.connect(self.update_evolution_tree)  # type: ignore

        # Add both to the tree
        tree_item = QTreeWidgetItem()
        self.tree_evolutions.insertTopLevelItem(i, tree_item)
        self.tree_evolutions.setItemWidget(tree_item, 0, combo_pkm)
        self.tree_evolutions.setItemWidget(tree_item, 1, combo_method)
        widget_value = self.get_evo_method_widget(combo_method.currentIndex())
        if widget_value:
            self.tree_evolutions.setItemWidget(tree_item, 2, widget_value)

    def get_evo_method_widget(
        self, method: int, value: int | str | None = None
    ) -> QWidget | None:
        widget_value: QWidget | None = None
        match method:
            # Level
            case 0:
                widget_value = SpinBox()
                widget_value.setMinimum(0)
                widget_value.setMaximum(100)
                widget_value.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
                if value is not None:
                    widget_value.setValue(int(value))
                else:
                    widget_value.setValue(1)
            # Item
            case 1:
                widget_value = ComboBox()
                widget_value.setEditable(True)
                widget_value.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
                widget_value.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
                widget_value.addItems(self.item_items)
                if value is not None:
                    widget_value.setCurrentText(str(value))
                else:
                    widget_value.setCurrentText("None")
        return widget_value

    def update_evolution_tree(self):
        current_item = self.tree_evolutions.currentItem()
        # Get current evolution method index (0 => level, 1 => item, 2 => custom)
        method: int = self.tree_evolutions.itemWidget(current_item, 1).currentIndex()  # type: ignore
        # Get corresponding widget based on the method
        widget: QWidget | None = self.get_evo_method_widget(method)
        # If function returns widget, add it to the tree
        if widget:
            self.tree_evolutions.setItemWidget(current_item, 2, widget)
        else:
            self.tree_evolutions.removeItemWidget(current_item, 2)

    def remove_tree_item(self, tree: QTreeWidget):
        i = tree.currentIndex().row()
        if i == -1:
            tree.takeTopLevelItem(tree.topLevelItemCount() - 1)
        else:
            tree.takeTopLevelItem(tree.currentIndex().row())

    def save_poke(self):
        # Update move definition (if it does not exist it will be created)
        # tree_moves_items: list[] = self.tree_moves.findItems("*", Qt.MatchWildcard)  # type: ignore

        tree_evolutions_items: list[QTreeWidgetItem] = [
            self.tree_evolutions.topLevelItem(i)
            for i in range(self.tree_evolutions.topLevelItemCount())
        ]

        self.pkm.update(
            {
                self.combo_name.currentText().replace(" ", "_"): {
                    "name": self.combo_name.currentText(),
                    "type1": self.combo_type1.currentText(),
                    "type2": self.combo_type2.currentText(),
                    "moves": [
                        {
                            "lvl": spin_level.value(),
                            "move": combo_move.currentText(),
                        }
                        for spin_level, combo_move in zip(
                            self.tree_moves.findChildren(SpinBox),
                            self.tree_moves.findChildren(ComboBox),
                        )
                    ],
                    "evolutions": [
                        {
                            "pkm": self.tree_evolutions.itemWidget(item, 0).currentText(),  # type: ignore
                            "method": self.tree_evolutions.itemWidget(item, 1).currentText(),  # type: ignore
                            "value": self.tree_evolutions.itemWidget(item, 2).value(),
                        }
                        for item in tree_evolutions_items
                    ],
                }
            }
        )
        print(self.pkm)
        # Save move to file
        print(toml.dumps(self.pkm_parse, pretty=False))
        # with open(self.pkm_path, "w", encoding="utf-8") as file:

        # print(toml.dump(self.pkm_parse, file, pretty=True))
        #    file.close()

    def get_file_path(self, file_name: str) -> Tuple[Path, Path]:
        path = self.root_path / file_name
        if not path.exists():
            # Ask the user to select the moves.toml file
            selected: str = QFileDialog.getOpenFileName(
                self, caption=f"Select {file_name}", filter=file_name
            )[0]
            # If returned path is null, stop the program
            if not selected:
                self.close()
                sys.exit()
            path = Path(selected)
        return (path.parent, path)

    def load_toml(self, path: Path) -> dict[str, Any]:
        with open(path, "rb") as file:
            return toml.load(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()

    sys.exit(app.exec())
