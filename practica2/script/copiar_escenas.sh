#!/bin/sh

for i in $(seq 1 6); do
	if [ $i -lt 4 ]; then
		cp ../escenas/escenaenPie.ttt "../positivo${i}/"
	else
		cp ../escenas/escenasentado.ttt "../positivo${i}/"
	fi
done

for i in $(seq 1 6); do
	if [ $i -lt 4 ]; then
		cp ../escenas/escenacilindroMenor.ttt "../negativo${i}/"
		cp ../escenas/escenacilindroMenorPared.ttt "../negativo${i}/"
	else
		cp ../escenas/escenacilindroMayor.ttt "../negativo${i}/"
		cp ../escenas/escenacilindroMayorPared.ttt "../negativo${i}/"
	fi
done

cp ../escenas/escenaTest.ttt ../predecir/
