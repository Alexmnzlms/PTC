#!/bin/bash

rm tiempos_python.txt
rm tiempos_c++.txt
rm tiempos_python_swig.txt

for s in {0..20000}
do
    echo -n $s '' >> tiempos_c++.txt && ./buscar_c++ >> tiempos_c++.txt
    echo -n $s '' >> tiempos_python.txt && python3 buscar_python.py >> tiempos_python.txt
    echo -n $s '' >> tiempos_python_swig.txt && python3 buscar_python_swig.py >> tiempos_python_swig.txt

done
