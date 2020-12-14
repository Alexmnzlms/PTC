/* File: example.i */
%module ordenar_vector
%include "std_vector.i"

namespace std{
   %template(vectori) vector<int>;
}

%{
#define SWIG_FILE_WITH_INIT
#include "ordenar_vector.h"
#include <vector>
using namespace std;
%}

%include "ordenar_vector.h"


