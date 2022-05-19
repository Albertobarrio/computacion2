import argparse
import mmap
import os
import sys

cli_parser = argparse.ArgumentParser(prog='Mapeador',
                                     description='Le por stdin y los escribe en un archivo',
                                     epilog='Trabajo Practico Obligatorio')

cli_parser.add_argument('-f',
                        '--file',
                        action='store',
                        required=True,
                        help='Archivo nuevo')

args = cli_parser.parse_args()

# Creamos la memoria compartida para que tanto el padre como el hijo puedan acceder
mm = mmap.mmap(-1, 512)

pid_hijo_1 = os.fork()
# Hijo 1
if pid_hijo_1 == 0:
    for line in sys.stdin:
        print("dato leido: "+line)

os.wait()

