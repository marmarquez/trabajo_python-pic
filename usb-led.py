from tkinter import *
from tkinter.font import Font
import serial
import time
import os

import serial.tools.list_ports

# definiendo objeto para la comunicacion
puerto = serial.Serial() 		
puerto.baudrate = 115200
puerto.timeout = 200
s = 'N'										# buffer receptor

# creando ventana de GUI
root = Tk()				
root.title('LED ON-OFF with Python')
root.geometry("400x350")
root.configure(background="LightSteelBlue3")		

flag = 1		# auxiliar para el boton

# -----------------------------------------------------------------------------------
# funcion que se ejecuta para enviar mensaje al mcu al presionar el boton2
def mensajeLed():

	global flag, puerto

	if puerto.is_open == 1:  # si esta conectado
		while 1==1:
			if flag == 1:		# encender led
				myButton2.config(bg='green',text='LED ON')
				flag = 2
				puerto.write(b'N')		   # manda msj de apagar
				break

			if flag == 2:		# apagar led
				myButton2.config(bg='red',text='LED OFF')
				flag = 1
				puerto.write(b'F')		   # manda msj de apagar	   
				break
	else: # si no esta conectado
		# abrir nueva ventana de dialogo
		error2 = Tk()				
		error2.title('errox02')
		error2.geometry("250x100")

		# por favor ingrese un puerto valido
		myLabel5 = Label(error2,text="Debe conectarse a un puerto")
		myLabel5.pack(padx=10,pady=30)

# -------------------------------------------------------------------------------------
# funcion que se ejecuta al presionar el boton1 para conectar con el puerto

def conectar():
	
	if (puerto.is_open == 0):		# si el puerto esta desconectado... intenta conectar

		ports = list(serial.tools.list_ports.comports())	# lista de puertos disponibles

		
		for p in ports:				# intenta conectar con cada puerto

			print (p.device)
			puerto.port = str(p.device)


			print(puerto)

			if (puerto.port != ""):
				print ("Conectando...")


				print(puerto.is_open)
				try:
					puerto.open()
					print(puerto.is_open)
					
					puerto.write(b'P')		   # manda msj para conectar	
					time.sleep(3)			   # retardo para esperar respuesta
					s = puerto.read()		   # lee el puerto
					if (s == 'P'):					# si recibe una 'P'
						myLabel2.config(text='Conectado')		# conecto
						break
					else:
						puerto.close()
						myLabel2.config(text='Desconectado')
				except:
					print("Conexion fallo")
					puerto.close()		# no se logró conectar

					# abrir nueva ventana de dialogo
					error = Tk()				
					error.title('errox04')
					error.geometry("200x100")

					myLabel4 = Label(error,text="Error en conexión")
					myLabel4.pack(padx=10,pady=30)
			#time.sleep(1)
	else:							# si el puerto esta conectado... desconecta
		puerto.close()
		print("No se pudo conectar")

# ---------------------------------------------------------------------------
# construccion de la ventana de GUI

myLabel3 = Label(root,text="Presione el botón para Encender o Apagar el LED:",bg="LightSteelBlue3")
myLabel3.pack(padx=15,pady=20)

myButton2 = Button(root, text="LED OFF",width=10,bg='red',command=mensajeLed)
myButton2.pack(padx=20,pady=20)

myLabel = Label(root,text="Estado de Conexión:", bg="LightSteelBlue3")
myLabel.pack(padx=10,pady=20)

# portCom = Entry(root,width=12)
# portCom.pack(padx=12,pady=15)

# portC = portCom.get()		# se obtiene el puerto al que se quiere conectar

myLabel2 = Label(root,text="Desconectado", bg="LightSteelBlue3")
myLabel2.pack(padx=10,pady=10)

myButton1 = Button(root, text="Conectar",command=conectar,width=9)
myButton1.pack(padx=10,pady=10)

root.mainloop()