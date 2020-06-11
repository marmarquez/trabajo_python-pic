# import tkinter as tk
from tkinter import *
from tkinter.font import Font

import usb.core
import usb.util
import os
# import sys
os.system('clear')

# creando ventana de GUI
root = Tk()				
root.title('LED ON-OFF with Python')
root.geometry("400x280")
root.configure(background="LightSteelBlue3")		# LightSkyBlue3

# text = Text(root)

myFont = Font(family="Calibri", size=20)

flag = 1		# auxiliar para el boton
flag2 = 0		# auxiliar para la conexion usb

status = "Desconectado"

# -----------------------------------------------------------------------------------
# funcion que se ejecuta para enviar mensaje al mcu al presionar el boton2
def mensajeLed():

	global flag
	global flag2 

	if flag2 == 1:  # si esta conectado
		while 1==1:
			if flag == 1:		# encender led
				myButton2.config(bg='green')
				myButton2.config(text='LED ON')
				flag = 2
				dev.write(1,'ON')
				# puerto.write(b'on')				# manda msj de encender
				break

			if flag == 2:		# apagar led
				myButton2.config(bg='red')
				myButton2.config(text='LED OFF')
				flag = 1
				dev.write(1,'OFF')
				# puerto.write(b'off')		   # manda msj de apagar
				break
	else: # si no esta conectado
		# abrir nueva ventana de dialogo
		error2 = Tk()				
		error2.title('errox02')
		error2.geometry("250x100")
		error2.configure(background="goldenrod3")

		# por favor ingrese un puerto valido
		myLabel5 = Label(error2,text="Debe conectarse a un puerto")
		myLabel5.pack(padx=10,pady=30)

# -------------------------------------------------------------------------------------
# funcion que se ejecuta al presionar el boton1 para conectar con el puerto

def conectar():
	
	global flag2

	# find our device
	dev = usb.core.find(idVendor=0x048D, idProduct=0x003F)

	# was it found?
	if dev is None:
	    #raise ValueError('Device not found')
		
		# abrir nueva ventana de dialogo
		error = tk.Tk()				
		error.title('errox01')
		error.geometry("300x100")
		error.configure(background="goldenrod3")

		# por favor ingrese un puerto valido
		myLabel4 = Label(error,text="No se encuentra el puerto establecido")
		myLabel4.pack(padx=10,pady=30)

	else:
		flag2 = 1			# conectado
		status = "Conectado"

		myLabel2.config(text="Estado de conexión:  " + status)

		# configuraciones iniciales del puerto establecido
		dev.set_configuration()

# ---------------------------------------------------------------------------
# construccion de la ventana de GUI

myLabel3 = Label(root,text="Presione el botón para Encender o Apagar el LED:",bg="LightSteelBlue3")
myLabel3.pack(padx=15,pady=20)

myButton2 = Button(root, text="LED OFF",width=10,bg='red',command=mensajeLed)
myButton2.pack(padx=20,pady=30)

myLabel = Label(root,text="Estado de conexión:  " + status,bg="LightSteelBlue3")
myLabel.pack(padx=10,pady=20)

myButton1 = Button(root, text="Conectar",command=conectar)
myButton1.pack(padx=10,pady=10)

root.mainloop()