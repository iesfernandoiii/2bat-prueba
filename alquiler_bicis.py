from datetime import *

# -----------------------------------------------------------------------
class AlquilerBicis:
    
    def __init__(self,stock=0,porhora=5,pordia=20,porsemana=60):
        """
        El constructor de la clase que instancia la tienda de alquiler de bicis.
        """
        self.stock = stock
        self.porhora= porhora
        self.pordia = pordia
        self.porsemana = porsemana         
    
    def mostrarstock(self):
        """
        Muestra las bicis disponibles para alquilar en la tienda.
        """
        print("Tenemos actualmente ",self.stock," bicis disponibles para alquilar.")
        return self.stock
    
    def alquilarBiciPorHoras(self, n):
        """
        Alquila (n) bicis por horas a un cliente.
        """
        # Rechazar entrada invalida 
        if n <= 0:
            print("¡El nº de bicis debe ser positivo!")
            return None
        # No se realiza el alquiler si el nº de bicis en stock es menor que las bicis solicitadas
        elif n > self.stock:
            print("¡Perdón! Actualmente solo disponemos de ",self.stock, " bicis disponibles para alquilar")
            return None
        # Alquilar las bicis
        else:
            ahora = datetime.now()                      
            print("Has alquilado ", n,  " bici(s) por horas hoy a las ",ahora.hour,":",ahora.minute)
            print("Se cobrará a ",self.porhora,"€ por cada hora y por cada bici.")
            print("Esperamos que disfrute de nuestro servicio.")
            self.stock = self.stock - n
            return ahora     
     
    def alquilarBiciPorDias(self, n):
        """
        Alquila (n) bicis por días a un cliente.
        """        
        if n <= 0:
            print("¡El nº de bicis debe ser positivo!")
            return None
        elif n > self.stock:
            print("¡Perdón! Actualmente solo disponemos de ",self.stock, " bicis disponibles para alquilar")
            return None
        else:
            ahora = datetime.now()                      
            print("Has alquilado ", n,  " bici(s) por días hoy a las ",ahora.hour,":",ahora.minute)
            print("Se cobrará a ",self.pordia,"€ por cada día y por cada bici.")
            print("Esperamos que disfrute de nuestro servicio.")
            self.stock = self.stock - n
            return ahora     
        
    def alquilarBiciPorSemanas(self, n):
        """
        Alquila (n) bicis por semanas a un cliente.
        """        
        if n <= 0:
            print("¡El nº de bicis debe ser positivo!")
            return None
        elif n > self.stock:
            print("¡Perdón! Actualmente solo disponemos de ",self.stock, " bicis disponibles para alquilar")
            return None
        else:
            ahora = datetime.now()                      
            print("Has alquilado ", n,  " bici(s) por días hoy a las",ahora.hour,":",ahora.minute)
            print("Se cobrará a ",self.porsemana,"€ por cada semana y por cada bici.")
            print("Esperamos que disfrute de nuestro servicio.")
            self.stock = self.stock - n
            return ahora     
    
    def devolverBici(self, pedido,fecha_devol=None):
        """
        1. Aceptar una bici alquilada por un cliente
        2. Reponer el stock disponible
        3. Sacar la factura al cliente
        """
       
        # extraer la tupla e iniciar la factura
        tiempoAlquiler, tipoAlquiler, numeroDeBicis = pedido
        factura = 0
        # generar la factura solo si los 3 parámetros tienen valores
        if tiempoAlquiler and tipoAlquiler and numeroDeBicis:
            self.stock = self.stock + numeroDeBicis
            # Si queremos indicar la fecha de devolución "a mano"
            if fecha_devol:
                ahora = fecha_devol
            else:
                ahora = datetime.now()
                
            periodoAlquiler = ahora - tiempoAlquiler
        
            # Cálculo de la factura por horas
            if tipoAlquiler == 1:
                factura = round(periodoAlquiler.seconds / 3600) * self.porhora * numeroDeBicis
                
            # Cálculo de la factura por días
            elif tipoAlquiler == 2:
                factura = round(periodoAlquiler.days) * self.pordia * numeroDeBicis
                
            # Cálculo de la factura por semanas
            elif tipoAlquiler == 3:
                factura = round(periodoAlquiler.days / 7) * self.porsemana * numeroDeBicis
            
            # Promoción especial para Familias, descuento del 30%
            # Cálculo del descuento
            if (3 <= numeroDeBicis <= 5):
                print("Ha sido seleccionado para aplicarle la promoción Familias 30 de descuento")
                factura = factura * 0.7
            print("Gracias por devolver la(s)",numeroDeBicis,"bici(s). Esperamos haya disfrutado del servicio.")
            print("El importe de su factura es de :",round(factura,2)," €.")
            return round(factura,2)
        
        else:
            print("¿Seguro que alquiló una bici con nososotros?")
            return None
        
# -----------------------------------------------------------------------
class Cliente:
    def __init__(self):
        """
        El constructor, que permite instanciar varios clientes.
        """
        
        self.bicis = 0
        self.tipoAlquiler = 0
        self.tiempoAlquiler = 0
        self.factura = 0
    
    def pedirtBici(self):
        """
        Toma el pedido de un cliente para un nº de bicis.
        """
                      
        bicis = input("¿Cuántas bicis quieres alquilar?\n")
        
        # Comprobar errores de entrada (numero entero)
        try:
            bicis = int(bicis)
        except ValueError:
            print("No es un entero positivo!")
            return -1
        if bicis < 1:
            print("¡Entrada errónea. El nº de bicis debe ser mayor que 0!")
            return -1
        else:
            self.bicis = bicis
        return self.bicis
     
    def devolverBici(self):
        """
        Permite a los clientes devolver las bicis a la tienda.
        """
        if self.tipoAlquiler and self.tiempoAlquiler and self.bicis:
            return self.tiempoAlquiler, self.tipoAlquiler, self.bicis  
        else:
            return 0,0,0
