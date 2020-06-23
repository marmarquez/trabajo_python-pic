from tkinter import *
from tkinter.font import Font
import serial
import os

# definiendo objeto para la comunicacion
puerto = serial.Serial() 		
puerto.baudrate = 9600
puerto.timeout = 200

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
	
	# si hay algo en el cuadro de texto, intento establecer conexion
	if puerto.is_open == 0:			# si esta desconectado entro aqui
		if portCom.get() != "":

			puerto.port = portCom.get()

			try:
				puerto.open()
				myLabel2.config(text='Conectado')
			except:
				puerto.close()		# no se logró conectar

				# abrir nueva ventana de dialogo
				error = Tk()				
				error.title('errox04')
				error.geometry("200x100")

				myLabel4 = Label(error,text="Error en conexión")
				myLabel4.pack(padx=10,pady=30)

		# si la entrada de texto esta vacia	
		if portCom.get() == "":

			# abrir nueva ventana de dialogo
			error = Tk()				
			error.title('errox01')
			error.geometry("200x100")

			# por favor ingrese un puerto valido
			myLabel4 = Label(error,text="Inserte puerto válido")
			myLabel4.pack(padx=10,pady=30)
	else:					# si esta conectado entro aqui
		puerto.close()
		myLabel2.config(text='Desconectado')

# ---------------------------------------------------------------------------
# construccion de la ventana de GUI

myLabel3 = Label(root,text="Presione el botón para Encender o Apagar el LED:",bg="LightSteelBlue3")
myLabel3.pack(padx=15,pady=20)

myButton2 = Button(root, text="LED OFF",width=10,bg='red',command=mensajeLed)
myButton2.pack(padx=20,pady=20)

myLabel = Label(root,text="Inserte puerto:", bg="LightSteelBlue3")
myLabel.pack(padx=10,pady=20)

portCom = Entry(root,width=12)
portCom.pack(padx=12,pady=15)

portC = portCom.get()		# se obtiene el puerto al que se quiere conectar

myLabel2 = Label(root,text="Desconectado", bg="LightSteelBlue3")
myLabel2.pack(padx=10,pady=10)

myButton1 = Button(root, text="Conectar",command=conectar,width=9)
myButton1.pack(padx=10,pady=10)

root.mainloop()