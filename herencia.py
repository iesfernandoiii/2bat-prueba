# ------------------------------------------------------------- 
# Definición de la clase padre 
# ------------------------------------------------------------- 
class Animal: 
    
    def __init__(self, especie, edad): 
        self.especie = especie 
        self.edad = edad 

    # Método genérico pero con implementación particular 
    def hablar(self): 
        # Método vacío 
        pass 

    # Método genérico pero con implementación particular 
    def moverse(self): 
        # Método vacío 
        pass 

    # Método genérico con la misma implementación 
    def describeme(self): 
        print("Soy un Animal del tipo", type(self).__name__) 

# ------------------------------------------------------------- 
# Definición de clases hijas 
# ------------------------------------------------------------- 
class Perro(Animal): 
    # Nuevo atributo 
    total_pasos = 0 

    # El método __init__ es llamado al crear el objeto 
    def __init__(self, especie, edad, nombre, raza): 
        # Se reutilizan los atributos de la clase padre 
        super().__init__(especie, edad) 
        # Atributos propios de la clase hija 
        self.nombre = nombre 
        self.raza = raza 
        print("Creando perro...") 

    # Redefinir el método hablar 
    def hablar(self): 
        print("Guau,guau") 

    # Redefinir el método moverse 
    def moverse(self,pasos=0): 
        self.total_pasos = self.total_pasos + pasos 
        print(self.nombre,"camina",pasos,"pasos.Ya lleva dados",self.total_pasos,"pasos") 

# ------------------------------------------------------------- 
class Vaca(Animal): 

    total_pasos = 0 

    def hablar(self): 
        print("Muuu!") 

    def moverse(self): 
        self.total_pasos = self.total_pasos + 1 
        print("La vaca, que no tiene nombre, camina pasito a pasito.Ya lleva dados",
              self.total_pasos,"pasos") 

# ------------------------------------------------------------- 
class Abeja(Animal): 
    # Nuevo atributo 
    muerta = False 

    def hablar(self): 
        print("Bzzzz!") 

    def moverse(self,metros=0): 
        print("Voy volando a",metros,"metros del suelo") 

    # Nuevo método 
    def picar(self): 
        if not self.muerta: 
            print("Que te pico...¡Picar!") 
            self.muerta = True 
        else: 
            print("Ya no puedo picar, me he muerto :(") 
# ------------------------------------------------------------- 

# Crear objetos de las clases 
gato = Animal("Felis", 5) 
mi_perro = Perro("Canis", 5, "Toby","Chiuaua") 
una_vaca = Vaca("Bos", 12) 
una_abeja = Abeja("Apis", 1) 

# Usando métodos 
gato.describeme() 
una_vaca.describeme() 

gato.hablar() # NO aparece nada 
mi_perro.hablar() 
una_vaca.hablar() 
una_abeja.hablar() 

for bicho in [mi_perro,una_vaca,una_abeja]:
    bicho.hablar()

gato.moverse()# NO aparece nada 
mi_perro.moverse(7) 
una_vaca.moverse() 
una_abeja.moverse(3) 

una_abeja.picar() 
una_abeja.picar()# Ya NO pica... 