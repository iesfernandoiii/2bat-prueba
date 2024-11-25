
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

# Variables
# ----------------------------------------------------------
palabras_disponibles = ["caballo","perro","gato","loro","pez","conejo","coballa"]

# Programa Principal
# ----------------------------------------------------------
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
    # 4. Preguntar por la letra
    letra_elegida = elijeLetra(lista_letras_acertadas + lista_letras_falladas)
    # 5. Comprobar si está o no en la palabra
    if letra_elegida in lista_letras_palabra:
        # 6. Si sí que está, 
        #   sustituirla en los guiones
        i = 0
        for elemento in lista_letras_palabra:
            if elemento == letra_elegida:
                lista_guiones[i] = letra_elegida
            i = i + 1
        #   añadirla a letras acertadas
        lista_letras_acertadas.append(letra_elegida)
    # 7. Si NO está
    else:
    #   añadirla a letras falladas
        lista_letras_falladas.append(letra_elegida)
        
    # Pintar el "hud" ()
    print(AHORCADO[len(lista_letras_falladas)])
    # Pinto letras falladas
    print("Letras falladas:"," ".join(lista_letras_falladas))
    # Pintar guiones
    print("")
    print(" ".join(lista_guiones))
    print("")
    # 8. Comprobar si he ganado o perdido
    #   si he ganado --> Mensaje ganar y FIN
    if "_" not in lista_guiones:
        print("Enhorabuena, has ganado!")
        parar = True
    #    si he perdido --> Mensaje has perdido y fin
    elif len(lista_letras_falladas) >= 6:
        print("Lo siento, has perdido!")
        parar = True
        
