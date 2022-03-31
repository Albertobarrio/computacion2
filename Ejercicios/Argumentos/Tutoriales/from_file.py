#!/usr/bin/python3

import argparse

# En este ejemplo usamos mas argumentos que son obligatorios y v que
# es opcional.Tabien se van a leer los argumentos desde un archivos 

# Creamos el parser
# fromfile_prefic_chars indicamos el prefijo para identificar o poner antes de un archivo
cli_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

# Agregamos los argumentos
# En este caso de la a la e son argumentos obligatorios y no necesariamente tienen que ver
# con la letra podes poner numeros o leer desde un text, en cambio v es opcional pero si o
# si es con -v

cli_parser.add_argument('a',
                        help='a primer argumento')
cli_parser.add_argument('b',
                        help='b segundo argumento')
cli_parser.add_argument('c',
                        help='c tercer argumento')
cli_parser.add_argument('d',
                        help='d cuarto argumento')
cli_parser.add_argument('e',
                        help='e quinto argumento')
cli_parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='argumento opcional')

# Ejecutamos el metodo parse_args()

args = cli_parser.parse_args()

