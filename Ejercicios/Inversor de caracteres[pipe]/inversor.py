import argparse
import os
import sys
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

# Se debe crear solo dos pipes porque si lo creamos en el for se crea un pipe por hijo
r1,w1 = os.pipe()
r2,w2 = os.pipe()

with open(args.file, 'r') as archivo:
    
    if os.fork():
        os.close(r1)
        os.close(w2)
        
        w1 = os.fdopen(w1,'w')
        
        for line in archivo:
            w1.write(line)
    
    else:
        os.close(w1)
        os.close(r2)
                
        r1 = os.fdopen(r1)
        leido = r1.read()
        
        w2 = os.fdopen(w2,'w')
        w2.write(leido[::-1])

    
    r2 = os.fdopen(r2)
    print(r2.read())