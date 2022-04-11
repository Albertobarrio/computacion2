import argparse
import os
import time

def escribir(file_open):
    file_open.write('H')
    file_open.flush()
    time.sleep(2)    


cli_parser = argparse.ArgumentParser(prog='Escritor',
                                     description='Crea n procesos hijos que escriben una letra en un archivo',
                                     epilog='Trabajo Practico Obligatorio')

cli_parser.add_argument('-n',
                        '--numero',
                        action='store',
                        type=int,
                        required=True,
                        choices=range(1,28),
                        help='Numero de procesos hijos')

# cli_parser.add_argument('-r',
#                         '--rep',
#                         action='store',
#                         type=int,
#                         required=True,
#                         help='Cantidad de veces que se debe escribir una letra')

cli_parser.add_argument('-f',
                        '--filepath',
                        action='store',
                        required=True,
                        help='Path del archivo')

cli_parser.add_argument('-v',
                        '--verboso',
                        action='store_true',
                        help='Activar modo verboso')

args = cli_parser.parse_args()


file_open = open(args.filepath, 'a+')

for _ in range(args.numero):
    print(f'{_} veces')
    if os.fork() == 0:
        print('Soy el hijo')
        escribir(file_open)
        os._exit(0)
os.wait()

file_open.close()





