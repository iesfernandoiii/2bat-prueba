# CAFETERÍA

# Definición de la clase café, con sus 2 atributos y 4 métodos
# ------------------------------------------------------------
class Cafe:
        # Constructor de la clase
        def __init__(self, nombre, precio):
                self.nombre = nombre
                self.precio = float(precio)

        def comprueba_presupuesto(self, presupuesto):
                # Comprueba si el presupuesto es válido
                if not isinstance(presupuesto, (int, float)):
                        print("Por favor, introduce un número")
                        exit()
                if presupuesto < 0: 
                    print("Perdona, no tienes dinero") 
                    exit() 
        def obtener_cambio(self, presupuesto):
                return presupuesto - self.precio
        
        def vender(self, presupuesto):
                self.comprueba_presupuesto(presupuesto)
                if presupuesto >= self.precio:
                        print("Te puedes permitir el cafe ", self.nombre)
                        if presupuesto == self.precio:
                                print("OK, compra lista")
                        else:
                                print("Tu cambio es: ", self.obtener_cambio(presupuesto))
                        print("Gracias por su compra")
                        exit()

# Utilización de la clase creada --> instanciación de la clase
# ------------------------------------------------------------
pequenyo = Cafe("Pequeño", 2)
normal = Cafe("Normal", 5)
grande = Cafe("Grande", 6)
extra_grande = Cafe("Megagrande",8)
 
try:
   presupuesto_usuario = int(input("¿Cuál es tu presupuesto (€)? "))
except ValueError:
   exit("Por favor, introduce un número")
  
for cafe in [extra_grande, grande, normal, pequenyo]:
   cafe.vender(presupuesto_usuario)







