set yrange [0:*]
set xrange [0:100]
set key left top box
set ylabel "Tiempo"
set xlabel "Ejecución"

plot "tiempos_c++.txt" with lines title "C++", \
"tiempos_python.txt" with lines title "Python", \
"tiempos_python_swig.txt" with lines title "Python-Swig"




