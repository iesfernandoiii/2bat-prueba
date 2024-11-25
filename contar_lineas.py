# Funcion que cuenta líneas de un fichero
def cuenta(nombre_fichero):
    with open(nombre_fichero,mode="r",encoding="utf-8") as fichero1:
        lineas = fichero1.readlines()
        return len(lineas)    

# Programa principal
f = input("Dime el nombre de un fichero:")
print("El fichero ",f, " tiene ",cuenta(f), " líneas")