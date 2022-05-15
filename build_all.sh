#! /usr/bin/env bash
# Build moves
pyinstaller -F -n moves_editor moves/src/app.py
cp moves/dist/moves_editor moves_editor

wineconsole pyinstaller -F -n moves_editor.exe moves/src/app.py
cp moves/dist/moves_editor.exe moves_editor.exe

# Build pokemon
# pyinstaller -F -n pokemon_editor pokemon/src/app.py
# cp pokemon/dist/pokemon_editor pokemon_editor
# 
# wineconsole pyinstaller -F -n pokemon_editor.exe pokemon/src/app.py
# cp pokemon/dist/pokemon_editor.exe pokemon_editor.exe