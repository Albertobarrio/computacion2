import argparse
from email import message
import os

def hijo():
    pass

if __name__ == "__main__":

    # Declaracion del parser
    cli_parser = argparse.ArgumentParser(prog='Sumador',
                                         description='Suma todos los números enteros pares entre 0 y su número de PID',
                                         epilog='Trabajo Practico Obligatorio')

    # Argumentos

    cli_parser.add_argument('-n',
                            '--numero',
                            action='store',
                            type=int,
                            required=True,
                            help='Numero de procesos hijos',
                            dest='num')
    
    cli_parser.add_argument('-v',
                            '--verboso',
                            action='store_true',
                            help='Activar modo verboso')

    # Obtenemos los argumentos
    args = cli_parser.parse_args()
    
    try:
        if args.num > 0:
            for _ in range(args.num):
                pass            
        raise ValueError

    except ValueError:
        print('El numero debe ser mayor a 0') 

    