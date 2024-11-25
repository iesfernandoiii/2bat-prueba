# 1. Obtener el nombre y ruta del fichero a leer
ruta = "frases.txt"
# 2. Abrirlo par lectura
with open(ruta,mode="r+",encoding="utf-8") as fichero1:
# 3. Para cada linea del fichero
    for la_linea in fichero1:        
    # 3.1. Leer la linea
    # 3.2. Mostrarla por pantalla
        print(la_linea.rstrip())
    
    print("\n", file=fichero1)

# 4. Pedir una frase al usuario (por  pantalla). OJO solo 5 frases
    for i in range (0,5):
        la_frase = input("Dime una frase:\n")
        # 3. Escribir esa frase en el fichero        
        print(la_frase, file=fichero1)
