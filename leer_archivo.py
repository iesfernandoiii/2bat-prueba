# 1. Obtener el nombre y ruta del fichero a leer
ruta = "animales.txt"
# 2. Abrirlo par lectura
with open(ruta,mode="r",encoding="utf-8") as fichero1:
# 3. Para cada linea del fichero
    for la_linea in fichero1:        
    # 3.1. Leer la linea
    # 3.2. Mostrarla por pantalla
        print(la_linea.rstrip())