import argparse
from posixpath import split
import subprocess as sp
import time
import sys
import os


# Defino el parser

cli_parser = argparse.ArgumentParser(prog='Ejecutor',
                                     description='Ejecuta un comando y guardas las salidas en archivos')

# Agrego los argumentos

cli_parser.add_argument('-c', 
                        '--c',
                        action='store',
                        metavar='command',
                        help='Comando a ejecutar', 
                        dest='command', 
                        type=str, 
                        required=True)
cli_parser.add_argument('-o', 
                        '--o', 
                        action='store',
                        metavar='output_file',
                        help='Almacena la salida del comando ejecutado', 
                        dest='output_file')
cli_parser.add_argument('-l',
                        '--l', 
                        action='store', 
                        metavar='log_file',
                        help='Almacena un mesaje o la salida de error', 
                        dest='log_file')

# Ejecutamos el metodo parse_args()

args = cli_parser.parse_args()
#print(vars(args))

#sp.Popen([args.command], shell=True)
#process = sp.Popen((args.command).split())
