#!/bin/bash
cd game
rm *.html
pyxel package ./ main.py
pyxel app2html game.pyxapp
sed -i -e 's/enabled/disabled/' ./game.html
