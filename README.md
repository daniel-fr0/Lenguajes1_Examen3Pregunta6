# Interprete de un subconjunto del lenguaje Prolog

Este interprete permite la definicion de predicados y la realizacion de consultas sobre los mismos.
El programa usa caracteristicas de python `3.10` por lo que se recomienda usar esta version o superior.

## Ejecucion

Ejecutar la instalacion de las dependencias con el siguiente comando:

Para ejecutar el interprete se debe ejecutar el archivo `main.py` con el interprete de python3.

```bash
	python3 main.py
```

## Pruebas

Para correr las pruebas debe ejecutar el siguiente comando en el directorio raiz del proyecto:

```bash
	python3 -m unittest discover -s tests -v
```

Tambien cuenta con un script que permite correr las pruebas:

```bash
	./run_tests.sh
```