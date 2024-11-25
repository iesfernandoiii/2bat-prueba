from datetime import *

#-------------------------------------------------------------------------
class Cliente():

    numBicis = 0
    tipoAlquiler = 0 # 1: Alquiler por horas, 2: Alquiler por días, 3: Alquiler por semanas
    tiempoAlquiler = 0

    def __init__(self,tipo=0):
        self.tipoAlquiler = tipo
    
    def AlquilarBici(self):
        
        numero = input("¿Cuántas bicis quiere alquilar?\n")
        
        try:
            el_numero = int(numero)
            if el_numero < 1:
                print("El nº de bicis debe ser nº entero positivo mayor que 0")    
            else:
                self.numBicis = el_numero
                self.tiempoAlquiler = datetime.now()            
        except ValueError:
            print(numero,"NO es un nº entero positivo")
        return self.numBicis
    
    def DevolverBici(self):
        print("Va usted a devolver:",self.numBicis,"bicis")
        return (self.numBicis,self.tipoAlquiler,self.tiempoAlquiler)

#-------------------------------------------------------------------------
class Tienda():

    stock = 0
    preciohoras = 0
    preciodias = 0
    preciosemanas = 0
    descuento = 0

    # Creamos la tienda con el strock inicial, los precios y los descuentos
    def __init__(self,stock_inicial,ph=5,pd=20,ps=60,desc=30):
        self.stock = stock_inicial
        self.preciohoras = ph
        self.preciodias = pd
        self.preciosemanas = ps
        self.descuento = desc

    # Alquilar bici por horas
    def AlquilarPorHoras(self,bicis):
        if self.stock >= bicis:
            print("Has alquilado",bicis,"por horas.Se cobrará a",self.preciohoras,"la hora cada bici.")
            print("Esperamos que disfrute de nuestros servicios")
            self.stock = self.stock - bicis
        else:
            print("No ha suficientes bicis disponibles. Disculpe las molestias")

    # Alquilar bici por dias
    def AlquilarPorDias(self,bicis):
        if self.stock >= bicis:
            print("Has alquilado",bicis,"por días.Se cobrará a",self.preciodias,"al día cada bici.")
            print("Esperamos que disfrute de nuestros servicios")
            self.stock = self.stock - bicis
        else:
            print("No ha suficientes bicis disponibles. Disculpe las molestias")
    
    # Alquilar bici por semanas
    def AlquilarPorSemanas(self,bicis):
        if self.stock >= bicis:
            print("Has alquilado",bicis,"por semanas.Se cobrará a",self.preciosemanas,"a la semana cada bici.")
            print("Esperamos que disfrute de nuestros servicios")
            self.stock = self.stock - bicis
        else:
            print("No ha suficientes bicis disponibles. Disculpe las molestias")
    
    # Devolver bicis y generar la factura
    def GenerarFactura(self,tupla,fecha):
        #Mirar el tipo de alquiler
        if tupla[1] == 1:
        #Si es por horas
            total_factura = tupla[0] * self.preciohoras * (int((fecha - tupla[2]).total_seconds()//3600))
        elif tupla[1] == 2:
        #Si es por días
            total_factura = tupla[0] * self.preciodias * (fecha - tupla[2]).days
        elif tupla[1] == 3:
        #Si es por semanas
            total_factura = tupla[0] * self.preciosemanas * ((fecha - tupla[2]).days//7)
        else:
            print("No reconozco ese tipo de alquiler. ¿Seguro que alquiló con nosotros?")
            return
        # Aplicar descuento
        #Si tiene entre 3 y 5 bicis
        if tupla[0] >= 3 and tupla[0] <=5:
            print("Enhorabuena, podemos aplicarle un descuento en su factura del",self.descuento,"%")
            total_factura = total_factura - (total_factura * self.descuento / 100)

        # Y reponer el stock
        self.stock = self.stock + tupla[0]
        # Mostramos cuánto es en total
        print("El importe a pagar es de:",round(total_factura,2),"€")
        return total_factura
        
    # Consultar el stock de bicis disponible
    def ConsultarStock(self):
        print("El stock actual es de:",self.stock," bicis.")




