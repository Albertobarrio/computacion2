import argparse
import os
import time


def hijo(pid):
    suma = 0
    for i in range(pid):
        if i % 2 == 0:
            suma += i
    time.sleep(0.25)
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
        pidpadre = os.getpid()
        if os.fork() == 0:
            pidhijo = os.getpid()
            if args.verboso:
                print(f"Starting Process {pidhijo}")
                print(f"{pidhijo} - {pidpadre}: {hijo(pidhijo)}")
                print(f"Ending Process {pidhijo}\n")
            else:
                print(f"{pidhijo} - {pidpadre}: {hijo(pidhijo)}")
            os._exit(0)
        os.wait()


if __name__ == "__main__":
    main()
