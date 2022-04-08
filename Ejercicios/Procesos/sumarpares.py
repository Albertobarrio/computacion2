import argparse
import os
import time


def sumar(pid):
    suma = 0
    for i in range(pid):
        if i % 2 == 0:
            suma += i
    return suma


def main():
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
                            help='Numero de procesos hijos')

    cli_parser.add_argument('-v',
                            '--verboso',
                            action='store_true',
                            help='Activar modo verboso')

    # Obtenemos los argumentos
    try:
        args = cli_parser.parse_args()
        if (args.numero <= 0):
            raise ValueError
    except ValueError:
        print("El numero debe ser mayor a cero")

    # Ejecutamos tantas vece segun el valor de n
    for _ in range(args.numero):
        if os.fork() == 0:
            if args.verboso:
                print(f"Starting Process {os.getpid()}")
                print(f"{os.getpid()} - {os.getppid()}: {sumar(os.getpid())}")
                print(f"Ending Process {os.getpid()}")
            else:
                print(f"{os.getpid()} - {os.getppid()}: {sumar(os.getpid())}")
            os._exit(0)
    # El padre va a esperar a que se ejecuten todos los hijos
    os.wait()
if __name__ == "__main__":
    main()
