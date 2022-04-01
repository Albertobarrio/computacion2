import os
# os.listdir lista todos los archivos del directorio
entries = os.listdir('Tutoriales/')
for archivo in entries:
    print(archivo)

# Una manera nueva es usar os.scandir
# que retorna un ScandirIterator que señala
# a cada uno de los nombres de los archivos
# leidos en el directorio
with os.scandir('Tutoriales/') as reader:
    for read in reader:
        print(read.name)



