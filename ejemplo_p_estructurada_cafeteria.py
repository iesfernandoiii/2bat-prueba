# CAFETERÍA
# Definir el precio de cada cafe
pequenyo = 2
normal = 5
grande = 6

# Solicitar el presupuesto al usuario 
presupuesto_usuario = input("¿Cuál es tu presupuesto (€)? ")
 
try:
   presupuesto_usuario = int(presupuesto_usuario)
except:
   print("Por favor, introduce un número")
   exit()

# Enregarle el cafe que se puede permitir y el cambio 
if presupuesto_usuario > 0:
   if presupuesto_usuario >= grande:
       print("Te puedes permitir el cafe grande")
       if presupuesto_usuario == grande:
           print("OK, compra lista")
       else:
           print("Tu cambio es: ", presupuesto_usuario - grande)
   elif presupuesto_usuario == normal:
       print("Te puedes permitir el cafe normal")
       print("OK, compra lista")
   elif presupuesto_usuario >= pequenyo:
       print("Te puedes permitir el cafe pequeño")
       if presupuesto_usuario == pequenyo:
           print("OK, compra lista")
       else:
           print("Tu cambio es: ", presupuesto_usuario - pequenyo)