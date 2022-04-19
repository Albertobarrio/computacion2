import argparse
import os
import sys

cli_parser = argparse.ArgumentParser(prog='Inversor',
                                     description='Invierte un archivo de texto',
                                     epilog='Trabajo Practico Obligatorio')

cli_parser.add_argument('-f',
                        '--file',
                        action='store',
                        required=True,
                        help='Archivo a invertir')

args = cli_parser.parse_args()


    
with open(args.file, 'r') as file_open:
    for line in file_open.readlines():
        r1,w1 = os.pipe()
        r2,w2 = os.pipe()

        if os.fork() == 0:
            os.close(w1)
            os.close(r2)
            os._exit(0)
        
        os.close(r1)
        os.close(w2)
        w1 = os.fdopen(w1,'w')
        w1.write(line)
    