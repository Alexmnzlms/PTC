#include <iostream>
#include "time.h"
using namespace std;


int buscarSubcadena(const string & palabra, const string & subcadena){
    int pos = -1;
	 int coincidencias = 0;
	 int iterador_palabra = 0;
    int iterador_sub = 0;


    bool encontrado = false;

    while(iterador_palabra < palabra.size() && (encontrado == false)){

        if (palabra[iterador_palabra] == subcadena[iterador_sub]){
            coincidencias = coincidencias + 1;
            iterador_sub = iterador_sub + 1;
        }
        else{
            if (coincidencias != 0);
                iterador_palabra = iterador_palabra - coincidencias;

            coincidencias = 0;
            iterador_sub = 0;
        }
        if (coincidencias == subcadena.size()){
            encontrado = true;
            pos = iterador_palabra - coincidencias + 1;
        }

        iterador_palabra = iterador_palabra + 1;

    }

   return pos;
}

int main(){

    clock_t begin,end;

    begin = clock();
    buscarSubcadena("me llamo pepito","ito");
    end = clock();

    cout << static_cast<double>((end-begin))/CLOCKS_PER_SEC << endl;



}