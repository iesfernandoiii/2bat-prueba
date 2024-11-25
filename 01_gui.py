# Importaciones s -----------------------------------------------
from guizero import App, Text, PushButton, Box, TextBox
import socket

puerto = 12345
lst_client_socket = []

# Funcioness ----------------------------------------------------
def avanzar():
    command = "avanzar"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def retroceder ():
    command = "retroceder"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def izquierda():
    command = "izquierda"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def derecha ():
    command = "derecha"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def arriba ():
    command = "arriba"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def abajo ():
    command = "abajo"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def parar():
    command = "parar"
    print(command)
    # Enviar el comando al servidor
    lst_client_socket[0].send(command.encode())

def conectar():
    if comprueba_ip(input_ip.value):
        print("conectar a:",input_ip.value)
        try:
            # Crear el socket del cliente
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Máximo 7 segundos para conectar
            client_socket.settimeout(7)
            client_socket.connect((input_ip.value, puerto))
            lst_client_socket.append(client_socket)        
            btn_conectar.disable()
            btn_desconectar.enable()
            lbl_conectado.value = "Conectado..."
        except socket.error as e:
            print("Error al conectar...")
            print(str(e))
            lbl_conectado.value = "Error al conectar..."
    else:
        lbl_conectado.value = "IP incorrecta"

def desconectar():
    print("desconectar")
    lst_client_socket[0].close()
    lst_client_socket.pop()
    btn_conectar.enable()
    btn_desconectar.disable() 
    lbl_conectado.value = "¡Desconectado!"

def comprueba_ip(dir_ip):
    lst_ip=dir_ip.strip().split(".")
    if len(lst_ip) > 4:
        print("IP más partes de las esperadas")
        return False
    try:
        lst_enteros = []
        for element in lst_ip:
            lst_enteros.append(int(element))
        return True
    except Exception as e:
        print("IP no todo numeros")
        print(str(e))
        return False 

# App -----------------------------------------------------------
app = App(title="GUI Controller for Robot Cars", width=500, height=500, layout="grid")
app.bg = "#ffffe6"

# Elementos dentro de la app  -----------------------------------
box_conectar = Box(app,layout="grid", grid=[0,0])
box_controles = Box(app,layout="grid", grid=[0,1])
box_grua = Box(app,layout="grid", grid=[0,2])

titulo = Text(box_conectar, "Conecta con el robot",grid=[0,0])
input_ip = TextBox(box_conectar,text="IP de la RPi",grid=[1,1],width=30)
input_ip.bg = "white"
lbl_conectado = Text(box_conectar, text="¡Desconectado!",grid=[1,2])


btn_conectar = PushButton(box_conectar, text="Conectar",grid=[0,1])
btn_desconectar = PushButton(box_conectar, text="Desconectar",grid=[0,2],enabled=False)
btn_arriba= PushButton(box_controles, text="Avanzar", grid=[1,0])
btn_abajo= PushButton(box_controles, text="Retroceder", grid=[1,2])
btn_izquierda= PushButton(box_controles, text="Izquierda", grid=[0,1])
btn_derecha= PushButton(box_controles, text="Derecha", grid=[2,1])
btn_parar= PushButton(box_controles, text="Stop", grid=[1,1])

btn_grua_arriba = PushButton(box_grua, text="Subir Brazo",grid=[0,0])
btn_grua_abajo = PushButton(box_grua, text="Bajar Brazo",grid=[1,0])


for btn in (btn_conectar,btn_abajo,btn_arriba,btn_izquierda,btn_derecha,btn_parar,btn_desconectar,btn_grua_abajo,btn_grua_arriba):
    btn.bg = "lightgrey"

# Eventos -------------------------------------------------------
btn_conectar.when_clicked = conectar
btn_desconectar.when_clicked = desconectar

btn_arriba.when_left_button_pressed = avanzar
btn_abajo.when_left_button_pressed = retroceder
btn_izquierda.when_left_button_pressed = izquierda
btn_derecha.when_left_button_pressed = derecha
btn_parar.when_left_button_pressed = parar

btn_grua_arriba.when_left_button_pressed = arriba
btn_grua_abajo.when_left_button_pressed = abajo

btn_arriba.when_left_button_released = parar
btn_abajo.when_left_button_released = parar
btn_izquierda.when_left_button_released = parar
btn_derecha.when_left_button_released = parar
btn_parar.when_left_button_released = parar
btn_grua_abajo.when_left_button_released = parar
btn_grua_arriba.when_left_button_released = parar


# Mostrar la app ------------------------------------------------
app.display()

