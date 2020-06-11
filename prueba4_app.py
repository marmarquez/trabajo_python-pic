from tkinter import *
# import serial
import usb.core
import usb.util
import os
os.system('clear')

# creando ventana de GUI
root = Tk()				
root.title('LED ON-OFF with Python')
root.geometry("550x250")

flag = 1		# auxiliar para el boton
flag2 = 0		# auxiliar para la conexion usb

# find our device
dev = usb.core.find(idVendor=0x04D8, idProduct=0x003F)

# was it found?
if dev is None:
    raise ValueError('Device not found')
else:
	flag2 = 1			# conectado

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()


# -----------------------------------------------------------------------------------
# funcion que se ejecuta para enviar mensaje al mcu al presionar el boton2
def mensajeLed():

	global flag
	# global puerto 

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

		# por favor ingrese un puerto valido
		myLabel5 = Label(error2,text="Debe conectarse a un puerto")
		myLabel5.grid(padx=10,pady=20)

# -------------------------------------------------------------------------------------
# funcion que se ejecuta al presionar el boton1 para conectar con el puerto

# def conectar():

# 	# si hay algo en el cuadro de texto, intento establecer conexion
# 	if puerto.is_open == 0:			# si esta desconectado entro aqui
# 		if portCom.get() != "":

# 			puerto.port = portCom.get()

# 			try:
# 				puerto.open()
# 				myLabel2.config(text="Conectado")
# 				myButton1.config(text='Desconectar')
# 			except:
# 				puerto.close()
# 				# no se logró conectar

# 		# si la entrada de texto esta vacia	
# 		if portCom.get() == "":

# 			# abrir nueva ventana de dialogo
# 			error = Tk()				
# 			error.title('errox01')
# 			error.geometry("200x100")

# 			# por favor ingrese un puerto valido
# 			myLabel4 = Label(error,text="Inserte puerto válido")
# 			myLabel4.grid(padx=10,pady=20)
# 	else:					# si esta conectado entro aqui
# 		puerto.close()
# 		myLabel2.config(text="Desonectado")
# 		myButton1.config(text='Conectar')

# ---------------------------------------------------------------------------
# construccion de la ventana de GUI

myLabel = Label(root,text="Establecer conexión con el puerto:")
myLabel.grid(padx=10,pady=10)

portCom = Entry(root,width=10)
portCom.grid(padx=12,pady=12)

portC = portCom.get()		# se obtiene el puerto al que se quiere conectar

#myButton1 = Button(root, text="Conectar",command=conectar)
#myButton1.grid(padx=12,pady=15)

myLabel2 = Label(root,text="Desconectado")
myLabel2.grid(padx=12,pady=20)

myLabel3 = Label(root,text="Presione el boton para encender o apagar:")
myLabel3.grid(row=1,column=2)

myButton2 = Button(root, text="LED OFF",width=10,bg='red',command=mensajeLed)
myButton2.grid(row=2,column=2)

root.mainloop()
