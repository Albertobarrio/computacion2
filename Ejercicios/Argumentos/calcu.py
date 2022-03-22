#!/usr/bin/python3

import getopt
from json.tool import main
import sys

# Excepcion en caso de operador incorrecto
class InvalidOperator(Exception):
    pass

def main():
    opts, args = getopt.getopt(sys.argv[1:], 'o:n:m:')

    for op, ar in opts:
        try:
            if(op == '-o'):
                if (ar not in ['+','-','*','/']):
                    raise InvalidOperator() 
                operador = ar
            elif(op == '-n'):
                numero1 = int(ar)
            elif(op == '-m'):
                numero2 = int(ar)
        except ValueError:
            print('Error a ingresado un numero')
            sys.exit()
        except InvalidOperator:
            print('Operador invalido')
            sys.exit()
    
    if operador == '+':
        sumar(numero1,numero2)
    elif operador == '-':
        restar(numero1,numero2)
    elif operador == '*':
        multiplicar(numero1,numero2)
    elif operador == '/':
        dividir(numero1,numero2)
    else:
        print("Operador incorrecto")

def sumar(a,b):
    print(a + b)

def restar(a,b):
    print(a - b)

def multiplicar(a,b):
    print(a * b)

def dividir(a,b):
    print(a / b)


if __name__ == '__main__':
    main()