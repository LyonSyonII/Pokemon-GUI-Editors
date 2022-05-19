import sys
from os import path
from typing import Any, Tuple
from pathlib import Path

import rtoml as toml
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from window import Ui_MainWindow


def under_to_space(text: str) -> str:
    return text.replace("_", " ")


class Window(Ui_MainWindow, QMainWindow):
    root_path: Path
    moves_path: Path
    moves_parse: dict[str, dict[str, dict[str, Any]]]
    moves: dict[str, dict[str, Any]]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_slots()

        # Get root path based on type of executable
        if getattr(sys, "frozen", False):
            self.root_path = Path(sys.executable).parent
        else:
            self.root_path = Path(path.dirname(path.abspath(__file__)))

        # If path does not exist, ask the user to select it
        (self.root_path, self.moves_path) = self.get_file_path("moves.toml.bytes")

        # Load moves.toml
        self.moves_parse = toml.load(self.moves_path)
        self.moves_parse.setdefault("Moves", {})
        self.moves = self.moves_parse["Moves"]

        # Add existing moves to the "Name" entry
        items = map(under_to_space, self.moves.keys())
        self.combo_name.addItems(list(items))
        # Add existing types to the "Type 1" and "Type 2" entries
        types_path = self.get_file_path("types.toml.bytes")[1]
        if types := toml.load(types_path).get("Types"):
            self.combo_type1.addItems(types.keys())
            self.combo_type2.addItems(types.keys())

    def connect_slots(self):
        self.combo_name.currentTextChanged.connect(self.name_changed)  # type: ignore
        self.combo_type1.currentTextChanged.connect(self.type1_changed)  # type: ignore
        self.combo_type2.currentTextChanged.connect(self.type2_changed)  # type: ignore
        self.combo_category.currentTextChanged.connect(self.category_changed)  # type: ignore
        self.spin_power.valueChanged.connect(self.power_changed)  # type: ignore
        self.spin_accuracy.valueChanged.connect(self.accuracy_changed)  # type: ignore
        self.spin_pp.valueChanged.connect(self.pp_changed)  # type: ignore
        self.button_save.clicked.connect(self.save_move)  # type: ignore
        self.button_cancel.clicked.connect(self.close)  # type: ignore

    def name_changed(self):
        text = self.combo_name.currentText()
        # If move is found in dictionary
        if move := self.moves.get(text.replace(" ", "_")):
            self.combo_type1.setCurrentText(move["type1"])
            self.combo_type2.setCurrentText(move["type2"])
            self.combo_category.setCurrentText(move["category"])
            self.spin_power.setValue(move["power"])
            self.spin_accuracy.setValue(move["accuracy"])
            self.spin_pp.setValue(move["pp"])
            self.combo_target.setCurrentText(move["target"])
            self.spin_priority.setValue(move["priority"])
            self.check_flag_a.setChecked(move["flags"] & 1)
            self.check_flag_b.setChecked(move["flags"] & 2)
            self.check_flag_c.setChecked(move["flags"] & 4)
            self.check_flag_d.setChecked(move["flags"] & 8)
            self.check_flag_e.setChecked(move["flags"] & 16)
            self.check_flag_f.setChecked(move["flags"] & 32)
            self.check_flag_g.setChecked(move["flags"] & 64)
            self.check_flag_h.setChecked(move["flags"] & 128)
            self.txtedit_description.setText(move["description"])

    def type1_changed(self):
        text = self.combo_type1.currentText()

    def type2_changed(self):
        text = self.combo_type2.currentText()

    def category_changed(self):
        text = self.combo_category.currentText()

    def power_changed(self):
        value = self.spin_power.value()

    def accuracy_changed(self):
        value = self.spin_accuracy.value()

    def pp_changed(self):
        value = self.spin_pp.value()

    def save_move(self):
        # Get move flags mask
        flags = (
            self.check_flag_a.isChecked()
            + self.check_flag_b.isChecked() * 2
            + self.check_flag_c.isChecked() * 4
            + self.check_flag_d.isChecked() * 8
            + self.check_flag_e.isChecked() * 16
            + self.check_flag_f.isChecked() * 32
            + self.check_flag_g.isChecked() * 64
            + self.check_flag_h.isChecked() * 128
        )
        # Update move definition (if it does not exist it will be created)
        self.moves.update(
            {
                self.combo_name.currentText().replace(" ", "_"): {
                    "name": self.combo_name.currentText(),
                    "type1": self.combo_type1.currentText(),
                    "type2": self.combo_type2.currentText(),
                    "category": self.combo_category.currentText(),
                    "power": self.spin_power.value(),
                    "accuracy": self.spin_accuracy.value(),
                    "pp": self.spin_pp.value(),
                    "target": self.combo_target.currentText(),
                    "priority": self.spin_priority.value(),
                    "flags": flags,
                    "description": self.txtedit_description.toPlainText(),
                }
            }
        )
        # Add new move to the "Name" entry
        self.combo_name.addItem(self.combo_name.currentText())
        # Save move to file
        with open(self.moves_path, "w", encoding="utf-8") as file:
            print(toml.dump(self.moves_parse, file))
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
