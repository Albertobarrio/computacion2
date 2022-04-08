import argparse
import os
import time


cli_parser = argparse.ArgumentParser(prog='Escritor',
                                     description='Crea n procesos hijos que escriben una letra en un rachivo',
                                     epilog='Trabajo Practico Obligatorio')

cli_parser.add_argument('-n',
                        '--numero',
                        action='store',
                        type=int,
                        required=True,
                        help='Numero de procesos hijos')


cli_parser.add_argument('-r',
                        '--rep',
                        action='store',
                        type=int,
                        required=True,
                        help='Cantidad de veces que se debe escribir una letra')

cli_parser.add_argument('-f',
                        '--filepath',
                        action='store',
                        required=True,
                        help='Path del archivo')


cli_parser.add_argument('-v',
                        '--verboso',
                        action='store_true',
                        help='Activar modo verboso')
