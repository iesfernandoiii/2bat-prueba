from datetime import *

fecha1 = "22/09/2024 13:22:15"
f1 = datetime.strptime(fecha1,"%d/%m/%Y %H:%M:%S")

fecha2 = "30/09/2024 16:22:15"
f2 = datetime.strptime(fecha2,"%d/%m/%Y %H:%M:%S")

f3 = f2-f1
print(f3)

print(f3.days)


print(f3.days//7)