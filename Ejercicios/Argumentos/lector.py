#!/usr/bin/python3

import argparse
import  os
import  sys

from click import argument

# Creamos el parser

cli_parser = argparse.ArgumentParser(description='Copia y pega un archivo')

# Agregamos los argumentos
cli_parser.add_argument('Path',metavar='path',type=str,help='the path to list')

# Ejecutamos el metodo parse_args()

args = cli_parser.parse_args()