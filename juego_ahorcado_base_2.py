
# Juego que simula el ahorcado.
# Puedes cometer 6 fallos
# Importaciones
# ----------------------------------------------------------
import random
from os import system, name

# Constantes
# ----------------------------------------------------------
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# Funciones
# ----------------------------------------------------------
def clear(): 
  
    # Para windows 
    if name == 'nt': 
        _ = system('cls') 
    # Para mac y linux(aquí, os.name es 'posix') 
    else: 
        _ = system('clear') 

def elijeLetra(letrasUtilizadas): 
    # Devuelve la letra que el jugador introdujo. Esta función hace que el jugador introduzca una letra y no cualquier otra cosa 
    while True: 
        print ('Adivina una letra:') 
        letra = input() 
        letra = letra.lower() 
        if len(letra) != 1: 
            print ('Introduce una sola letra.') 
        elif letra in letrasUtilizadas: 
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?') 
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz': 
            print ('Elije una letra y no otro símbolo.') 
        else: 
            return letra 

def comprobar_letra(letra,l_l_palabra,l_l_falladas,l_l_acertadas,l_guiones):
    # Comprobar si está o no en la palabra
    # Si sí que está, sustituirla en los guiones
    if letra in l_l_palabra:
      
        i = 0
        for elemento in l_l_palabra:
            if elemento == letra:
                l_guiones[i] = letra
            i = i + 1
        #   añadirla a letras acertadas
        l_l_acertadas.append(letra_elegida)
    # Si NO está, añadirla a letras falladas
    else:
        l_l_falladas.append(letra_elegida)

def pintar_hud(l_l_falladas,l_guiones): 
    # Pintar el "hud" ()
    print(AHORCADO[len(l_l_falladas)])
    # Pinto letras falladas
    print("Letras falladas:"," ".join(l_l_falladas))
    # Pintar guiones
    print("")
    print(" ".join(l_guiones))
    print("")

def comprobar_fin(l_guiones,l_l_falladas):    
    # 8. Comprobar si he ganado o perdido
    #   si he ganado --> Mensaje ganar y FIN
    if "_" not in l_guiones:
        print("Enhorabuena, has ganado!")
        return True
    #    si he perdido --> Mensaje has perdido y fin
    elif len(l_l_falladas) >= 6:
        print("Lo siento, has perdido!")
        return True
    else:
        return False

# Variables
# ----------------------------------------------------------
palabras_disponibles = ["caballo","perro","gato","loro","pez","conejo","coballa"]

# Programa Principal
# ----------------------------------------------------------
#===========================================================================================
# INICIO El PROGRAMA
#===========================================================================================
# 1. Dibujar cadalso vacio
clear()
print(AHORCADO[0])
# 2. Pensar pala a adivinar
palabra_a_adivinar = palabras_disponibles[random.randint(0,len(palabras_disponibles)-1)]
# 3. Sustituir cada letra por guiones
lista_guiones = []
lista_letras_palabra = list(palabra_a_adivinar)
for letra in lista_letras_palabra:
    lista_guiones.append("_")
#print(lista_letras_palabra)
print("Letras falladas:")
print("")
print(" ".join(lista_guiones))
print("")
lista_letras_falladas = []
lista_letras_acertadas = []


# Bucle principal
parar = False
while not parar:
    # Preguntar por la letra
    letra_elegida = elijeLetra(lista_letras_acertadas + lista_letras_falladas)
    #===========================================================================================
    # Comprobar acierto o fallo
    comprobar_letra(letra_elegida,
                    lista_letras_palabra,
                    lista_letras_falladas,
                    lista_letras_acertadas,
                    lista_guiones)
    #===========================================================================================
    # Mostrar interfaz (hud)
    pintar_hud(lista_letras_falladas,
               lista_guiones)
    #===========================================================================================
    # Comprobar si ganas o pierdes
    parar = comprobar_fin(lista_guiones,
                          lista_letras_falladas)
        
