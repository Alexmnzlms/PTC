#!/bin/sh

swig -c++ -python ordenar_vector.i
g++ -O2 -fPIC -c ordenar_vector.cpp
g++ -O2 -fPIC -c ordenar_vector_wrap.cxx -I/usr/include/python3.9
g++ -shared ordenar_vector.o ordenar_vector_wrap.o -o _ordenar_vector.so


