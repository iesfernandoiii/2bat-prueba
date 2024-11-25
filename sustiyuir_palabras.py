# 1. Pedir las 2 palabras y Pedir el nombre del fichero
ruta =  input("Dime un fichero a cambiar:")
palabra1 = input("Dime una palabra que aparezca en el texto:")
palabra2 = input("Dime la palabra que la sustituye:")
nueva_ruta = ruta + "_modificado.txt"

cuenta = 0

# 3. Abrir fichero en modo lectura y leer linea a linea
with open(ruta,mode="r",encoding="utf-8") as fichero1:
    with open(nueva_ruta,mode="w",encoding="utf-8") as fichero2:
        # Para cada linea del fichero
        for linea_leida in fichero1: 
            # Contar las veces que se va a sustituir la palabra en la línea
            cuenta = cuenta + linea_leida.count(palabra1)
            # 3.1. Sustitutir en esa linea las palabras que toquen
            nueva_linea = linea_leida.replace(palabra1,palabra2)
            # 3.2. Escribir esa linea (modificada o no) en un nuevo fichero
            print(nueva_linea.rstrip(),file=fichero2)

print("Se ha sustituido ",cuenta," veces la palabra.")
