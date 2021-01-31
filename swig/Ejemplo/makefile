all:
	swig -python example.i
	gcc -c -fpic example.c example_wrap.c -I/usr/include/python3.9
	gcc -shared example.o example_wrap.o -o _example.so
	python
