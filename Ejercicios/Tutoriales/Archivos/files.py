# Cuestiones generales:
#   Todos los archivos tienen un header,data y EOF(End Of File)

with open('test.txt', 'r') as reader:
    # print(reader.read()) lee todo de un saque
    line = reader.readline()
    while line != '':    # El EOF es un string vacio
        print(line, end='') # El end='' es para impedri que python meta una linea en blaco nueva
        line = reader.readline()

# Otra formar de leer un archivo
with open('test.txt', 'r') as reader:
    for line in reader.readlines():  # readlines retorna una lista con la lineas
        print(line, end='')

# Otra forma simple leyendo el objeto directamente

with open('test.txt', 'r') as reader:
    for line in reader:
        print(line, end='')
