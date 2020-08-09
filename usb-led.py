from tkinter import *				# LIBRERIA PARA GUI
from tkinter.font import Font
import serial                       # LIBRERIA PARA PUERTO SERIAL
import os

import serial.tools.list_ports

# definiendo objeto para la comunicacion
puerto = serial.Serial() 			# define el objeto puerto serial		
puerto.baudrate = 115200			# tasa de baud 115200
puerto.timeout = 5					# time out 15s

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
				myButton2.config(bg='green',text='LED ON')		# cambia msj de boton a ON
				flag = 2
				puerto.write(b'N')		   # manda msj de apagar
				break

			if flag == 2:		# apagar led
				myButton2.config(bg='red',text='LED OFF')		# cambia msj de boton a OFF
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

	#print ("ENTRO EN CONECTAR")	    # DEBUG

	if (puerto.is_open == 0):		# si el puerto esta desconectado... intenta conectar

		c = 1				# variable auxiliar para emitir mensaje de error en conexion

		#print ("PUERTO DESCONECTADO")		# DEBUG

		ports = list(serial.tools.list_ports.comports())	# lista de puertos disponibles

		for p in ports:				# intenta conectar con cada puerto

			puerto.port = str(p.device)			# identifica el puerto en cuestion

			#print (p.device)					# DEBUG
			#print(puerto)						# DEBUG

			if (puerto.port != ""):

				#print ("Conectando...")			# DEBUG
				#print(puerto.is_open)			# DEBUG

				try:
					puerto.open()				# abre puerto

					#print(puerto.is_open)		# DEBUG
					
					puerto.write(b'P')		   # manda msj para conectar	

					r = puerto.read()		   # lee el puerto
					r = r.decode("utf-8")	   # cambia de byte a string

					#print(r)					# DEBUG

					if (r == 'P'):					# si recibe una 'P'
						myLabel2.config(text='Conectado')		# conecto
						myButton1.config(text='Desconectar')		# cambia msj de boton a desconectar

						#print ("CONECTADO")								# DEBUG
						c = 0
						break									# no evalua mas puertos
					else:
						#print ("RECIBI OTRA COSA")				# DEBUG

						puerto.close()							# cierro puerto
						myLabel2.config(text='Desconectado')	# estado de conexion desconectado
				except:				# si hay problemas abriendo el puerto
					c = 1
		if ( c == 1):

			#print("Conexion fallo")
			puerto.close()		# no se logró conectar

			# abrir nueva ventana de dialogo: MENSAJE DE ERROR
			error = Tk()				
			error.title('errox04')
			error.geometry("200x100")

			myLabel4 = Label(error,text="Error en conexión")
			myLabel4.pack(padx=10,pady=30)
	else:							# si el puerto esta conectado... desconecta

		puerto.close()				# cierra puerto
		myLabel2.config(text='Desconectado')		
		myButton1.config(text='Conectar')
		#print("No se pudo conectar")			# DEBUG

# ---------------------------------------------------------------------------
# construccion de la ventana de GUI

myLabel3 = Label(root,text="Presione el botón para Encender o Apagar el LED:",bg="LightSteelBlue3")
myLabel3.pack(padx=15,pady=20)

myButton2 = Button(root, text="LED OFF",width=10,bg='red',command=mensajeLed)
myButton2.pack(padx=20,pady=20)

myLabel = Label(root,text="Estado de Conexión:", bg="LightSteelBlue3")
myLabel.pack(padx=10,pady=20)

myLabel2 = Label(root,text="Desconectado", bg="LightSteelBlue3")
myLabel2.pack(padx=10,pady=10)

myButton1 = Button(root, text="Conectar",command=conectar,width=12)
myButton1.pack(padx=10,pady=10)

root.mainloop()