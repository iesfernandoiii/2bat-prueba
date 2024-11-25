# Clase coches
class Coche:
    """Describe los coches y las cosas que pueden hacer"""
    # Atributos de la clase
    n_ruedas = 4
    
    # Constructor
    def __init__(self,dni,marca,modelo,color,
                matricula,v_maxima,v_inicial=0):
        self.dni = dni
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.v_inicial = v_inicial
        self.v_maxima = v_maxima
    # Metodos

    # Acelerar
    def acelerar(self,inc_velocidad):
        # Sumar a la velocidad inicial el incremento de 
        # velocidad hasta la velocidad máxima
        if self.v_inicial + inc_velocidad <= self.v_maxima:
            self.v_inicial = self.v_inicial + inc_velocidad
        print("La velocidad actual del ",
              self.marca," ", self.modelo," es:",self.v_inicial)
    # Frenar
    def frenar(self,dis_velocidad):
        # Restar a la v_inicial la dis_velocidad
        # siempre que sea >= 0
        if self.v_inicial - dis_velocidad >= 0:
            self.v_inicial = self.v_inicial - dis_velocidad
        print("La velocidad actual del ",
              self.marca," ", self.modelo," es:",self.v_inicial)
    # Pintar
    def pintar(self,nuevo_color):
        print("El color actual del ",
              self.marca," ", self.modelo," es:",self.color)
        self.color = nuevo_color
        print("Ahora es de color:",self.color)

class Persona:
    """Define caracteristicas de las personas"""

    def __init__(self,dni,nombre,edad,sexo,direccion):
        if self.validad_dni(self,dni):
            self.dni = dni
        else:
            print("DNI no valido")
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
    
    def cambia_direccion(self,nueva_direccion):
        print("Cambiamos la dirección de:",self.direccion,
              " a ",nueva_direccion)
        self.direccion = nueva_direccion
    
    def cumplir_anyos(self,aumento=1):
        self.edad = self.edad + aumento
        print("Ahora tienes:",self.edad)

    # Validad DNI
    def validad_dni(self,nuevo_dni):
        # "11111111H"
        # 1. Si tiene 9 dígitos
        if len(nuevo_dni) > 9:
            return False
        # 2. Si los 8 primeros son números
        numero = nuevo_dni[:8]
        letra = nuevo_dni[8:]
        if not numero.isnumeric():
            return False
        # 3. Si el último es una letra
        if not letra.isalpha():
            return False
        return True
 
    # Saber si eres mayor de edad
    def mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

#----------------------------------------------------------------
# PROGRAMA PINCIPAL
coche_p = Coche("Peugeot","5008","Gris metalizado","5678-HGF",150,0)
coche_e = Coche("Ford","Fiesta","Rojo","555-HTF",120,23)

coche_p.acelerar(30)
coche_e.acelerar(50)
coche_p.pintar("Azul")
coche_e.frenar(10)
