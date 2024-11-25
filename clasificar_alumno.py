# Inicio
# Obtener nombre y sexo
apellido = input("Dime el primer apellido:").lower()
sexo = input("Dime el sexo (H)ombre o (M)ujer:").upper()
#¿Es mujer y apellido entre a..m?
if ((sexo == "M") and (apellido[0] <= "m")) or ((sexo == "H") and (apellido[0] > "n")):
    print("Grupo A")
elif ((sexo == "M") and (apellido[0] > "m")) or ((sexo == "H") and (apellido[0] <= "n")):
    print("Grupo B")


# Fin