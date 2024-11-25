# Definir un clase para crear objetos de tipo perro
# Atributos
# - Raza
# - Nombre
# - Color del pelaje
# - Velocidad
# Métodos
# - Andar
# - Hablar

# Definir la clase
class Perro:
    
    # Constructor
    def __init__(self,raza,nombre,color,velocidad):
        self.raza = raza
        self.nombre = nombre
        self.color = color
        self.velocidad = velocidad
        self.posicion = 0
    
    def andar(self):
        self.posicion = self.posicion + self.velocidad





# ------------ PROGRAMA PRINCIPAL ------------------
# Crear objetos de tipo perro
mi_perro = Perro("Pastor Aleman","Tobby","Marrón",5)
el_perro_de_raquel = Perro("Maltés","Kira","Blanco",3)

mi_perro.andar()
