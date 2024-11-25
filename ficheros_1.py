import io
ruta = "primer_fichero.txt" 

with io.open(ruta, mode="r+", encoding="utf-8") as fichero: 
    for linea in fichero:
        # Imprimir en la pantalla
        print(linea,end="")
    # Agregar lineas las fichero - Imprimir en el fichero
    print("Mosca", file=fichero) 
    print("serpiente", file=fichero) 

print("ACABADO")