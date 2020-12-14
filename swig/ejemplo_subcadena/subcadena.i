/* File: example.i */
%module subcadena
%include "std_string.i"

%{
#define SWIG_FILE_WITH_INIT
#include "subcadena.h"
#include <string>
using namespace std;
%}

using namespace std;

int buscarSubcadena(const string  & palabra, const string & subcadena);


