from tienda import *
from datetime import datetime
from os import system, name

def clear(): 
    # Para windows 
    if name == 'nt': 
        _ = system('cls') 
    # Para mac y linux(aquí, os.name es 'posix') 
    else: 
        _ = system('clear') 

def main():

    mi_tienda = Tienda(stock_inicial=25,pd=7,ph=25,ps=70)
    mi_cliente = Cliente()

    while True:

        print("====== Tienda de alquiler de bicis =======")
        print("1. Mostar bicis disponibles")
        print("2. Alquilar bici por horas a",mi_tienda.preciohoras,"€")
        print("3. Alquilar bici por días a",mi_tienda.preciodias,"€")
        print("4. Alquilar bici por semanas a",mi_tienda.preciosemanas,"€")
        print("5. Devolver bici con fecha de ahora")
        print("6. Devolver bici con fecha diferida")
        print("7. Salir")
        
        opcion = input("Elige una opción: ")

        # Mostrar bicis
        if opcion == "1":
            mi_tienda.ConsultarStock()
        #Alquilar x horas
        elif opcion == "2":
            mi_cliente.tipoAlquiler = 1
            mi_tienda.AlquilarPorHoras(mi_cliente.AlquilarBici())
        #Alquilar x dias
        elif opcion == "3":
            mi_cliente.tipoAlquiler = 2
            mi_tienda.AlquilarPorDias(mi_cliente.AlquilarBici())        
        #Alquilar x semanas
        elif opcion == "4":
            mi_cliente.tipoAlquiler = 3
            mi_tienda.AlquilarPorSemanas(mi_cliente.AlquilarBici())        
        #Devolver ahora
        elif opcion == "5":
            mi_tienda.GenerarFactura(mi_cliente.DevolverBici(),datetime.now())
        #Devolver luego
        elif opcion == "6":
            fecha_diferida = input("¿En qué fecha piensas devolver las bicis?\n")
            fecha_diferida = datetime.strptime(fecha_diferida,"%H:%M %d/%m/%Y")
            mi_tienda.GenerarFactura(mi_cliente.DevolverBici(),fecha_diferida)
        #Salir                 
        elif opcion == "7":
            break
        # Caso por defecto
        else:
            print("Lo siento, no entiendo la orde. Elija un nº del 1 al 7")
            clear()

    
    print("Gracias por usar nuestro sistema de alquiler")

# Programa pincipal
if __name__=="__main__":
    main()

