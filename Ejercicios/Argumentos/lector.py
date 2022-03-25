#!/usr/bin/python3

import argparse
import  os
import  sys

# Creamos el parser
# prog: sirve para indicar el nombre del programa, por default toma el nombre del script y va a
#       a ser indicado en el help text
# description: sirve para indicar el funcionamiento del base del programa y se muestra al princi
#              pio del programa
# epilog: testo que se muestra al final del help text
# usage: sirve para customizar el hel text ahi bien cheto
# prefix_chars: para modificar el char que usamos para pasar argumentos opcionales , por default
#              es - pero lo podemos cambiar

cli_parser = argparse.ArgumentParser(prog='Lector',
                                     usage='%(prog)s [options] path', 
                                     description='Copia y pega un archivo',
                                     epilog='Disfrfuta el programa esta re cheto',
                                     prefix_chars='/')

# Agregamos los argumentos
cli_parser.add_argument('Path',metavar='path',type=str,help='the path to list')

# Ejecutamos el metodo parse_args()

args = cli_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("No es un directorio")
    sys.exit()

print('\n'.join(os.listdir(input_path)))
