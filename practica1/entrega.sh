#!/bin/sh

make
cp memoria.pdf poblacion/memoria.pdf
cd poblacion
python main.py
rm resultados/*
rm -rf __pycache__
ls -laR
cd ..
zip Practica1_AlejandroManzanaresLemus.zip -r poblacion
