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
    leido = ""
    for line in file_open.readlines():
        r1,w1 = os.pipe()
        r2,w2 = os.pipe()
        
        if os.fork():
            os.close(r1)
            os.close(w2)
            w1 = os.fdopen(w1,'w')
            w1.write(line)
            w1.flush()
            r2 = os.fdopen(r2)
            while True:
                leido = r2.read()
                print(leido)
            
        else:
            os.close(w1)
            os.close(r2)
            r1 = os.fdopen(r1)
            w2 = os.fdopen(w2,'w')
            leido = r1.read()
            w2.write(leido[::-1])
            os._exit(0)
    