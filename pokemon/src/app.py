import sys
from os.path import dirname, abspath
from typing import Any, Sequence, Tuple, KeysView
from pathlib import Path

import toml
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QTreeWidgetItem,
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
    move_items: Sequence[str]

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
        # Load moves.toml
        self.pkm_parse = toml.load(self.pkm_path)
        self.pkm_parse.setdefault("Pokemon", {})
        self.pkm = self.pkm_parse["Pokemon"]

        # Add existing Pokemon to the "Name" entry
        self.combo_name.addItems([under_to_space(p) for p in self.pkm.keys()])

        # Save existing moves for later entries
        moves_path = self.get_file_path("moves.toml.bytes")[1]
        moves: KeysView[str] = toml.load(moves_path).get("Moves", {}).keys()
        self.move_items = [under_to_space(move) for move in moves]

        # Add existing abilities to the corresponding entries
        abilities_path = self.get_file_path("abilities.toml.bytes")[1]
        abilities = [
            under_to_space(a)
            for a in toml.load(abilities_path).get("Abilities", {}).keys()
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
        self.button_remove_move.clicked.connect(self.remove_move_item)  # type: ignore

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
        level_box = SpinBox()
        level_box.setMaximum(100)
        level_box.setMinimum(0)
        level_box.setValue(level)
        level_box.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        # Create move combobox with the needed properties
        move_box = ComboBox()
        move_box.setEditable(True)
        move_box.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        move_box.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        move_box.setPlaceholderText("Select move")
        if move:
            move_box.setCurrentText(move)
        move_box.addItems(self.move_items)
        # Add both to the tree
        self.tree_moves.insertTopLevelItem(i, QTreeWidgetItem())
        self.tree_moves.setItemWidget(self.tree_moves.topLevelItem(i), 0, level_box)
        self.tree_moves.setItemWidget(self.tree_moves.topLevelItem(i), 1, move_box)

    def remove_move_item(self):
        i = self.tree_moves.currentIndex().row()
        if i == -1:
            self.tree_moves.takeTopLevelItem(self.tree_moves.topLevelItemCount() - 1)
        else:
            self.tree_moves.takeTopLevelItem(self.tree_moves.currentIndex().row())

    def save_poke(self):
        # Update move definition (if it does not exist it will be created)
        self.pkm.update(
            {
                self.combo_name.currentText().replace(" ", "_"): {
                    "name": self.combo_name.currentText(),
                    "type1": self.combo_type1.currentText(),
                    "type2": self.combo_type2.currentText(),
                }
            }
        )
        # Save move to file
        with open(self.pkm_path, "w", encoding="utf-8") as file:
            print(toml.dump(self.pkm_parse, file))
            file.close()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()

    sys.exit(app.exec())
