#!/usr/bin/python3

import argparse
from ensurepip import version
import os
import sys

# En este ejemplo vemos lo basico de arparse

# Creamos el parser
#
# prog: sirve para indicar el nombre del programa, por default toma el nombre del script y va a
#       a ser indicado en el help text
# description: sirve para indicar el funcionamiento del base del programa y se muestra al princi
#              pio del programa
# allow_abbrev: permite o no usar abreviaciones argumentos opcionales
# epilog: testo que se muestra al final del help text
# usage: sirve para customizar el hel text ahi bien cheto
# prefix_chars: para modificar el char que usamos para pasar argumentos opcionales , por default
#              es - pero lo podemos cambiar
# add_help: para habilitar o no la ayuda automaticas

cli_parser = argparse.ArgumentParser(prog='Lector',
                                     usage='%(prog)s [options] path',
                                     description='Copia y pega un archivo',
                                     epilog='Disfrfuta el programa esta re cheto')


# Dos tipos de argumentos:
#   Posicionales son los que los comando necesitan para operar, son posicionales porque su
#   posicion define su funcionamiento
#
#   Opcionales no son obligatorios pero cuando se ponen modifican el comportamiento
# La diferencia es radical es que los opcionales empiezan con - o -- y los posicionales no 

#  Tipos de actions:
#  -store: stores the input value to the Namespace object. (This is the default action.)
#  -store_const: stores a constant value when the corresponding optional arguments are specified.
#  -store_true: stores the Boolean value True when the corresponding optional argument is specified and stores a False elsewhere.
#  -store_false: stores the Boolean value False when the corresponding optional argument is specified and stores True elsewhere.
#  -append: stores a list, appending a value to the list each time the option is provided.
#  -append_const: stores a list appending a constant value to the list each time the option is provided.
#  -count: stores an int that is equal to the times the option has been provided.
#  -help: shows a help text and exits.
#  -version: shows the version of the program and exits.

# Agregamos los argumentos
cli_parser.add_argument('Path', metavar='path', type=str, help='the path to list')

cli_parser.add_argument('-l','--long', action='store_true', help='enable the log listing format')

# Ejecutamos el metodo parse_args()

args = cli_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("No es un directorio")
    sys.exit()

for line in os.listdir(input_path):
    if args.long:  # Simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d  %s' % (size, line)
    print(line)
#print('\n'.join(os.listdir(input_path)))
