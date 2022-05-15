#! /usr/bin/env bash
# Build moves
pyinstaller -F -n moves_editor moves/src/app.py &
wineconsole pyinstaller -F -n moves_editor.exe moves/src/app.py &

# Build pokemon
# pyinstaller -F -n pokemon_editor pokemon/src/app.py &
# 
# wineconsole pyinstaller -F -n pokemon_editor.exe pokemon/src/app.py &

wait
echo "Done!"