# Escribe un programa que pida al usuario ingresar cinco frases y 
# las guarde en un archivo llamado frases.txt. 
# En este ejercicio se crea un nuevo archivo (o sobrescribe uno existente) y 
# escribe el texto proporcionado en él. 

# 1. Poner ruta y abrir fichero (modo escritura)
ruta = "frases.txt"
with open(ruta,mode="w",encoding="utf-8") as fichero2:
# 2. Pedir una frase al usuario (por  pantalla). OJO solo 5 frases
    for i in range (0,5):
        la_frase = input("Dime una frase:\n")
        # 3. Escribir esa frase en el fichero        
        print(la_frase, file=fichero2)
