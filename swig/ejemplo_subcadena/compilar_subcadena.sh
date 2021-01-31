#!/bin/sh

swig -c++ -python subcadena.i
g++ -O2 -fPIC -c subcadena.cpp
g++ -O2 -fPIC -c subcadena_wrap.cxx -I/usr/include/python3.9
g++ -shared subcadena.o subcadena_wrap.o -o _subcadena.so



