import argparse
import os
import time
cli_parser = argparse.ArgumentParser(prog='Inversor',
                                     description='Invierte un archivo de texto',
                                     epilog='Trabajo Practico Obligatorio')

cli_parser.add_argument('-f',
                        '--file',
                        action='store',
                        required=True,
                        help='Archivo a invertir')

args = cli_parser.parse_args()

pipe1_r,pipe1_w = os.pipe()
pipe2_r,pipe2_w = os.pipe()

with open(args.file, 'r') as file_open:
    os.close(pipe1_r)
    os.close(pipe2_w)
    for line in file_open:
        w1 = os.fdopen(pipe1_w,'w')
        w1.write(line)        
        if os.fork() == 0:
            os.close(pipe1_w)
            os.close(pipe2_r)
            b_leido = os.read(pipe1_w, 1024)
            print(b_leido)   


