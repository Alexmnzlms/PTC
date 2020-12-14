#include <iostream>
#include <string>
#include "ordenar_vector.h"
#include <fstream>
#include <random>
#include <ctime>
#include "time.h"
using namespace std;

vector<int> ordenar(const std::vector<int> &mi_vector) {
    vector<int> salida = mi_vector;
    int i, j, minimo;
    int n = mi_vector.size();
    for (i = 0; i < n-1; i++){
            minimo = i;
            for (j = i+1; j < n; j++){
                    if (salida[j] < salida[minimo]){
                        minimo = j;
                    }
            }
            int temp = salida[minimo];
            salida[minimo] = salida[i];
            salida[i] = temp;

    }

    return salida;

}

