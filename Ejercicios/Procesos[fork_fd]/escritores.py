import argparse
import os
import time

from click import open_file

cli_parser = argparse.ArgumentParser(prog='Escritor',
                                     description='Crea n procesos hijos que escriben una letra en un archivo',
                                     epilog='Trabajo Practico Obligatorio')

cli_parser.add_argument('-n',
                        '--numero',
                        action='store',
                        type=int,
                        required=True,
                        choices=range(1, 27),
                        help='Numero de procesos hijos , desde el 1 al 26')

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

args = cli_parser.parse_args()

with open(args.filepath, 'w+') as file_open:
    for _ in range(args.numero):
        if os.fork() == 0:
            letra = chr(65 + _)
            for _ in range(args.rep):
                if args.verboso:
                    print(f'Proceso {os.getpid()} escribiendo letra {letra}')
                file_open.write(letra)
                file_open.flush()
                time.sleep(1)
            os._exit(0)
    # Un for para que el padre esepere a cada hijo
    for _ in range(args.numero): 
        os.wait() 

# El padre lee el arhivo nuevo y lo muestra por pantalla
with open(args.filepath, 'r') as new_file:
    for line in new_file:
        print(line)
        


# Lo mismo pero sin el with
# file_open = open(args.filepath, 'w+')
# for _ in range(args.numero):
#     if os.fork() == 0:
#         letra = chr(65 + _)
#         for _ in range(args.rep):
#             if args.verboso:
#                 print(f'Proceso {os.getpid()} escribiendo letra {letra}')
#             file_open.write(letra)
#             file_open.flush()
#             time.sleep(1)
#         os._exit(0)
# Cerramos el archivo
#file_open.close()
