# importaciones
from os import system, name

# define funcion limpiar
def limpiar():

    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#pedir pizza
lista_ingredientes_vegetarianos = ["Pimiento","Tofu","Brocoli","Romanescu"]
lista_ingredientes_normales = ["Peperoni","Jamón","Salmón","Atun","Pollo"]
lista_ingredientes_obligatorios = ["Base de harina de espelta","Tomate","Mozzarella"]
lista_a_usar = []

#¿Quiere pizza vegetariana?
# Mostrar menú
print("¿Qué tipo de pizza prefieres?")
print("1. (V)egetariana")
print("2. (N)ormal")
tipo_pizza = input()
limpiar()

if tipo_pizza == "V" or tipo_pizza == "1":
    lista_a_usar = lista_ingredientes_vegetarianos
else:
    lista_a_usar = lista_ingredientes_normales

#Mostrar ingredientes
i = 1
print("Elija un ingrediente de los siguientes:")
for elemento in lista_a_usar:
    print(i,".",elemento)
    i = i + 1

#Elegir ingrediente
ingrediente_elegido = int(input())

limpiar()

#Mostrar todos los ingredientes de la pizza elegida
print("Su pizza lleva los siguientes ingredientes:")
for elemento in lista_ingredientes_obligatorios:
    print(elemento)
print(lista_a_usar[ingrediente_elegido-1])
