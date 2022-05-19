import argparse
import os
import sys


# Defino el parser

cli_parser = argparse.ArgumentParser(prog='Copia',
                                     description='Copia el contenido de un archivo y lo guarda en otro')

# Agrego los argumentos

cli_parser.add_argument('-i',
                        '--i',
                        action='store',
                        help='Archivo origen',
                        dest='source_file')
                        
cli_parser.add_argument('-o',
                        '--o',
                        action='store',
                        help='Almacena la salida del comando ejecutado',
                        dest='dest_file')

# Recupero los valores de los argumentos

args = cli_parser.parse_args()

source_file = args.source_file
des_file = args.dest_file

try:
    with open(source_file, 'r') as reader, open(des_file, 'w') as writer:
        lines = reader.readlines()
        writer.writelines(lines)
except FileNotFoundError:
    print(f"El archivo {source_file} no ha sido encotrado")
except IOError as e:
    print("Error")
