#!/usr/bin/python3

import getopt
import sys


def sumar(a,b):
    print(a + b)

def restar(a,b):
    print(a - b)

def multiplicar(a,b):
    print(a * b)

def dividir(a,b):
    print(a / b)

# Rcivir argumentos

opts, args = getopt.getopt(sys.argv[1:], 'o:n:m:')


for op, ar in opts:
    if(op == '-o'):
        operador = ar
        print(ar)
    elif(op == '-n'):
        numero1 = int(ar)
        print(ar)
    elif(op == '-m'):
        numero2 = int(ar)
        print(ar)

if operador == '+':
    sumar(numero1,numero2)



# Funciones segun la operacion

