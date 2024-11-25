import random

# -------------------------------------
# Clase CARTA
class Carta():
    valores = [None,None,2,3,4,5,6,7,8,9,10,11,12,13]
    palos = ["Oros","Bastos","Copas","Espadas"]

    def __init__(self,valor,palo):
        self.valor = valor
        self.palo = palo
    
    def mayor_que(self,otra_carta):
        if self.valor > otra_carta.valor:
            return True
        else:
            return False
        
    def menor_que(self,otra_carta):
        if self.valor < otra_carta.valor:
            return True
        else:
            return False    

    def igual_que(self,otra_carta):
        if self.valor == otra_carta.valor:
            return True
        else:
            return False

    # Descripción de cada carta
    def __repr__(self):
        d = str(self.valor) + " de " + self.palo
        return d
        

# -------------------------------------
# Clase BARAJA
class Baraja():
    
    def __init__(self):
        self.mazo = []
        for i in range (2,14):
            for j in range (4):
                nueva_carta = Carta(i,Carta.palos[j])
                self.mazo.append(nueva_carta)
    
    def barajar(self):
        random.shuffle(self.mazo)
    
    def quitar_carta(self):
        una_carta = self.mazo.pop()
        return una_carta

# -------------------------------------
# Clase JUGADOR
class Jugador():

    rondas = 0

    def __init__(self):
        self.nombre = input("Dime tu nombre:")

    def gana_ronda(self):
        self.rondas = self.rondas + 1
        print("El jugador",self.nombre,"lleva ganadas",str(self.rondas))

# -------------------------------------
# Clase JUEGO
class Juego():

    def __init__(self):
        # Crear una baraja
        self.la_baraja = Baraja()
        # Barajar
        self.la_baraja.barajar()
        # Crear un jugador
        self.jugador1 = Jugador()
        print("Primer jugador creado, vamos con el siguiente...")
        # Crear otro jugador
        self.jugador2 = Jugador()
        print("Segundo jugador creado, ya podemos jugar...")

    def jugar(self):
        # para cada ronda
        while len(self.la_baraja.mazo) > 0:
            # jugador 1 coge una carta
            self.carta_j1 = self.la_baraja.quitar_carta()
            # jugador 2 coge una carta
            self.carta_j2 = self.la_baraja.quitar_carta()
            print("El jugador",self.jugador1.nombre,"ha cogido un",self.carta_j1)
            print("El jugador",self.jugador2.nombre,"ha cogido un",self.carta_j2)
            # comparamos las cartas
            if self.carta_j1.mayor_que(self.carta_j2):
                # Gana jugador 1
                print("Gana la ronda el jugador",self.jugador1.nombre)
                self.jugador1.gana_ronda()
            elif self.carta_j1.menor_que(self.carta_j2):
                # Gana jugador 2
                print("Gana la ronda el jugador",self.jugador2.nombre)
                self.jugador2.gana_ronda()                
            else:
                # Empate
                print("Ha habido un empate...")
        
        # Buscamos el ganador
        if self.jugador1.rondas > self.jugador2.rondas:
            print("Gana el juego",self.jugador1.nombre,"con",str(self.jugador1.rondas))
        elif self.jugador1.rondas < self.jugador2.rondas:
            print("Gana el juego",self.jugador2.nombre,"con",str(self.jugador2.rondas))
        else:
            print("Hay un empate entre",self.jugador1.nombre,"y",
                  self.jugador2.nombre,"con",str(self.jugador1.rondas))

#----------------------------------------
# PROGRAMA PRINCIPAL
mi_juego = Juego()