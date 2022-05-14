import sys
import os
import re
from typing import Any
from pathlib import Path

import toml
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from window import Ui_MainWindow


def camel_to_spaces(text: str) -> str:
    return re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)

class Window(QMainWindow, Ui_MainWindow):
    root_path: Path
    moves_path: Path
    moves: dict[str, dict[str, Any]]
    moves_parse: dict[str, dict[str, dict[str, Any]]]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_slots()

        # Get root path based on type of executable 
        if getattr(sys, "frozen", False):
            self.root_path = Path(sys.executable).parent
        else:
            self.root_path = Path(os.path.dirname(os.path.abspath(__file__)))

        # If path does not exist, ask the user to select it
        self.root_path = self.get_file_dir("moves.toml")

        # Load moves.toml
        self.moves_path = self.root_path / "moves.toml.bytes"
        self.moves_parse = toml.load(self.moves_path)
        self.moves = self.moves_parse["Moves"]

        # Add existing moves to the "Name" entry
        self.name.addItems(map(camel_to_spaces, self.moves.keys()))
        # Add existing types to the "Type 1" and "Type 2" entries
        types_path = self.get_file_dir("types.toml") / "types.toml.bytes"
        types: None | dict[str, Any] = toml.load(types_path).get("Types")
        if types:
            self.type1.addItems(types.keys())
            self.type2.addItems(types.keys())

    def connect_slots(self):
        self.name.currentTextChanged.connect(self.name_changed)
        self.type1.currentTextChanged.connect(self.type1_changed)
        self.type2.currentTextChanged.connect(self.type2_changed)
        self.category.currentTextChanged.connect(self.category_changed)
        self.power.valueChanged.connect(self.power_changed)
        self.accuracy.valueChanged.connect(self.accuracy_changed)
        self.pp.valueChanged.connect(self.pp_changed)
        self.save.clicked.connect(self.save_move)
        self.cancel.clicked.connect(self.close)

    def name_changed(self):
        text = self.name.currentText().title()
        move = self.moves.get(text.replace(" ", ""))
        if move:
            text = camel_to_spaces(text)
            self.type1.setCurrentText(move["type1"])
            self.type2.setCurrentText(move["type2"])
            self.category.setCurrentText(move["category"])
            self.power.setValue(move["power"])
            self.accuracy.setValue(move["accuracy"])
            self.pp.setValue(move["pp"])
            self.target.setCurrentText(move["target"])
            self.priority.setValue(move["priority"])
            self.flag_a.setChecked(move["flags"] & 1)
            self.flag_b.setChecked(move["flags"] & 2)
            self.flag_c.setChecked(move["flags"] & 4)
            self.flag_d.setChecked(move["flags"] & 8)
            self.flag_e.setChecked(move["flags"] & 16)
            self.flag_f.setChecked(move["flags"] & 32)
            self.flag_g.setChecked(move["flags"] & 64)
            self.flag_h.setChecked(move["flags"] & 128)
            self.description.setText(move["description"])
        self.name.setCurrentText(text)

    def type1_changed(self):
        text = self.type1.currentText()

    def type2_changed(self):
        text = self.type2.currentText()

    def category_changed(self):
        text = self.category.currentText()

    def power_changed(self):
        value = self.power.value()

    def accuracy_changed(self):
        value = self.accuracy.value()

    def pp_changed(self):
        value = self.pp.value()

    def save_move(self):
        # Get move flags mask
        flags = (
            self.flag_a.isChecked() * 1
            + self.flag_b.isChecked() * 2
            + self.flag_c.isChecked() * 4
            + self.flag_d.isChecked() * 8
            + self.flag_e.isChecked() * 16
            + self.flag_f.isChecked() * 32
            + self.flag_g.isChecked() * 64
            + self.flag_h.isChecked() * 128
        )

        # Update move definition (if it does not exist it will be created)
        self.moves.update(
            {
                self.name.currentText().replace(" ", ""): {
                    "name": self.name.currentText(),
                    "type1": self.type1.currentText(),
                    "type2": self.type2.currentText(),
                    "category": self.category.currentText(),
                    "power": self.power.value(),
                    "accuracy": self.accuracy.value(),
                    "pp": self.pp.value(),
                    "target": self.target.currentText(),
                    "priority": self.priority.value(),
                    "flags": flags,
                    "description": self.description.toPlainText(),
                }
            }
        )
        # Save move to file
        with open(self.moves_path, "w", encoding="utf-8") as file:
            dump = toml.dumps(self.moves_parse)
            file.write(dump)
            file.close()
            print(dump)
    
    def get_file_dir(self, file_name: str) -> Path:
        path = self.root_path/f"{file_name}.bytes"
        while not path.exists():
            # Ask the user to select the moves.toml file
            path_s = QFileDialog.getOpenFileName(
                caption=f"Select {file_name}", filter=f"{file_name}.bytes"
            )[0]
            # If returned path is null, stop the program
            if not path_s:
                self.close()
                sys.exit()
            path = Path(path_s)
        return path.parent


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()

    sys.exit(app.exec())
