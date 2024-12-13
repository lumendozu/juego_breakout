from tkinter import *
#Velocidad modo Facil
vf1=8
vf2=5
#velocidad modo Medio
vm1=13
vm2=8
#velocidad modo Dificil
vd1=13
vd2=10
#Dificultad(Facil)
def facil():
	#hasta donde va a rebotar la pelota
	x=520
	y=550
#ventana donde va a rebotar la pelota
	Markus2=Canvas()
	Markus2.pack(expand=YES, fill=BOTH)
	Markus2.configure(bg="green")
#creo la pelota y la linea
	pelota= Markus2.create_oval(60,10,80,30,fill='white')
# linea que se mueve
	rectangulo= Markus2.create_rectangle(200,480,300,490,fill='black')
	#linea arriba(Decoración)
	rectangulo2= Markus2.create_rectangle(520,7,0,0,fill="white")
	#linea izquierda(Decoración)
	rectangulo3=Markus2.create_rectangle(7,700,0,0,fill="white")
	#linea derecha(Decoración)
	rectangulo4=Markus2.create_rectangle(511,700,520,0,fill="white")
#linea abajo (Decorción)
	rectangulo5= Markus2.create_rectangle(520,700,0,750,fill='white')
#función para mover la pelota
	def mover_pelota():
#global variables fuera de la función
		global vf1,vf2
		Markus2.move(pelota,vf1,vf2)
#pi=posición izquierda,pa=posición arriba,pd=posición derecha,pab=posición abajo
		(pi,pa,pd,pab)=Markus2.coords(pelota)
#x1=posición izquierda,x2=posición arriba,x3=posición derecha,x4=posición abajo
		(x1,x2,x3,x4)=Markus2.coords(rectangulo)
#r1=posición izquierda,r2=posición arriba,r3=posición derecha,r4=posición abajo
		(r1,r2,r3,r4)=Markus2.coords(rectangulo2)
#l1=posición izquierda,l2=posición arriba,l3=posición derecha,l4=posición abajo
		(l1,l2,l3,l4)=Markus2.coords(rectangulo3)
#a1=posición izquierda,a2=posición arriba,a3=posición derecha,a4=posición abajo
		(a1,a2,a3,a4)=Markus2.coords(rectangulo3)
#cuando la pelota llegue a un extreme la velocidad cambia a negativo
		if pi<=0 and pa<=l4 and pab>=l2 :
		  vf1= -vf1
		elif pd>=520 and pa<=l4 and pab>=l2 :
			vf1= -vf1
		elif pa<=0 and pd>=r1 and pi<=r3:
			vf2= -vf2
		elif pab>x2 and pd==x3:
			vf1=8
			vf2=5
			#480
		elif pab>=480:
			if pab>=480 and pd>=x1 and pi<=x3:
				vf2=-vf2
			elif pa>=x4:
				Markus.destroy()
					

#after:ejecuta una función en en un determinado tiempo
		Markus2.after(30, mover_pelota)
	Markus2.after(10,mover_pelota)
	#muevo la linea de canvas
	def izquierda ():
		(x1,y1,x2,y2)=Markus2.coords(rectangulo)
		if x1>0:
			Markus2.move(rectangulo,-50,0)
	def derecha():
		(x1, y1, x2, y2)=Markus2.coords(rectangulo)
#si la posicion derecha de la linea canvas se pasa de geometry detener rectangulo
		if x2<505:
			Markus2.move(rectangulo,50, 0)
	#creo los botones que mueven la linea
	b5=Button(Markus,text="→",command=derecha)
	b5.place(x=400, y=630, width=80, height=50)
	b5.configure(bg="red")

	b6=Button(Markus,text="←",command=izquierda)
	b6.place(x=30, y=630, width=80, height=50)
	b6.configure(bg="red")

#Dificultad(Medio)
def Medio():
	#hasta donde va a rebotar la pelota
	x=520
	y=550
#ventana donde va a rebotar la pelota
	Markus2=Canvas()
	Markus2.pack(expand=YES, fill=BOTH)
	Markus2.configure(bg="yellow")
#creo la pelota y la linea
	pelota= Markus2.create_oval(60,10,80,30,fill='white')
# linea que se mueve
	rectangulo= Markus2.create_rectangle(200,480,300,490,fill='black')
	#linea arriba(Decoración)
	rectangulo2= Markus2.create_rectangle(520,7,0,0,fill="black")
	#linea izquierda(Decoración)
	rectangulo3=Markus2.create_rectangle(7,700,0,0,fill="black")
	#linea derecha(Decoración)
	rectangulo4=Markus2.create_rectangle(511,700,520,0,fill="black")
#linea abajo (Decorción)
	rectangulo5= Markus2.create_rectangle(520,700,0,750,fill="black")
#función para mover la pelota
	def mover_pelota():
#global variables fuera de la función
		global vm1,vm2
		Markus2.move(pelota,vm1,vm2)
#pi=posición izquierda,pa=posición arriba,pd=posición derecha,pab=posición abajo
		(pi,pa,pd,pab)=Markus2.coords(pelota)
#x1=posición izquierda,x2=posición arriba,x3=posición derecha,x4=posición abajo
		(x1,x2,x3,x4)=Markus2.coords(rectangulo)
#r1=posición izquierda,r2=posición arriba,r3=posición derecha,r4=posición abajo
		(r1,r2,r3,r4)=Markus2.coords(rectangulo2)
#l1=posición izquierda,l2=posición arriba,l3=posición derecha,l4=posición abajo
		(l1,l2,l3,l4)=Markus2.coords(rectangulo3)
#a1=posición izquierda,a2=posición arriba,a3=posición derecha,a4=posición abajo
		(a1,a2,a3,a4)=Markus2.coords(rectangulo3)
#cuando la pelota llegue a un extreme la velocidad cambia a negativo
		if pi<=0 and pa<=l4 and pab>=l2 :
		  vm1= -vm1
		elif pd>=520 and pa<=l4 and pab>=l2 :
			vm1= -vm1
		elif pa<=0 and pd>=r1 and pi<=r3:
			vm2= -vm2
		elif pab>x2 and pd==x3:
			vm1=13
			vm2=18
			#480
		elif pab>=480:
			if pab>=480 and pd>=x1 and pi<=x3:
				vm2=-vm2
			elif pa>=x4:
				Markus.destroy
#after:ejecuta una función en en un determinado tiempo
		Markus2.after(30, mover_pelota)
	Markus2.after(10,mover_pelota)
	#muevo la linea de canvas
	def izquierda ():
		(x1,y1,x2,y2)=Markus2.coords(rectangulo)
		if x1>0:
			Markus2.move(rectangulo,-50,0)
	def derecha():
		(x1, y1, x2, y2)=Markus2.coords(rectangulo)
#si la posicion derecha de la linea canvas se pasa de geometry detener rectangulo
		if x2<505:
			Markus2.move(rectangulo,50, 0)
	#creo los botones que mueven la linea
	b5=Button(Markus,text="→",command=derecha)
	b5.place(x=400, y=630, width=80, height=50)
	b5.configure(bg="red")

	b6=Button(Markus,text="←",command=izquierda)
	b6.place(x=30, y=630, width=80, height=50)
	b6.configure(bg="red")

#Dificultad(Dificil)
def Dificil():
	#hasta donde va a rebotar la pelota
	x=520
	y=550
#ventana donde va a rebotar la pelota
	Markus2=Canvas()
	Markus2.pack(expand=YES, fill=BOTH)
	Markus2.configure(bg="red")
#creo la pelota y la linea
	pelota= Markus2.create_oval(60,10,80,30,fill='white')
# linea que se mueve
	rectangulo= Markus2.create_rectangle(200,480,300,490,fill='black')
	#linea arriba 
	rectangulo2= Markus2.create_rectangle(700,10,0,0,fill="black")
	#linea izquierda(Decoración)
	rectangulo3=Markus2.create_rectangle(7,700,0,0,fill="black")
	#linea derecha(Decoración)
	rectangulo4=Markus2.create_rectangle(511,700,520,0,fill="black")
#linea abajo (Decorción)
	rectangulo5= Markus2.create_rectangle(520,700,0,750,fill="black")
#función para mover la pelota
	def mover_pelota():
#global variables fuera de la función
		global vd1,vd2
		Markus2.move(pelota,vd1,vd2)
#pi=posición izquierda,pa=posición arriba,pd=posición derecha,pab=posición abajo
		(pi,pa,pd,pab)=Markus2.coords(pelota)
#x1=posición izquierda,x2=posición arriba,x3=posición derecha,x4=posición abajo
		(x1,x2,x3,x4)=Markus2.coords(rectangulo)
#r1=posición izquierda,r2=posición arriba,r3=posición derecha,r4=posición abajo
		(r1,r2,r3,r4)=Markus2.coords(rectangulo2)
#l1=posición izquierda,l2=posición arriba,l3=posición derecha,l4=posición abajo
		(l1,l2,l3,l4)=Markus2.coords(rectangulo3)
#a1=posición izquierda,a2=posición arriba,a3=posición derecha,a4=posición abajo
		(a1,a2,a3,a4)=Markus2.coords(rectangulo3)
#cuando la pelota llegue a un extreme la velocidad cambia a negativo
		if pi<=0 and pa<=l4 and pab>=l2 :
		  vd1= -vd1
		elif pd>=520 and pa<=l4 and pab>=l2 :
			vd1= -vd1
		elif pa<=0 and pd>=r1 and pi<=r3:
			vd2= -vd2
		elif pab>x2 and pd==x3:
			vd1=13
			vd2=18
			#480
		elif pab>=480:
			if pab>=480 and pd>=x1 and pi<=x3:
				vd2=-vd2
			elif pa>=x4:
				Markus.destroy()
				
#after:ejecuta una función en en un determinado tiempo
		Markus2.after(30, mover_pelota)
	Markus2.after(10,mover_pelota)
	#muevo la linea de canvas
	def izquierda ():
		(x1,y1,x2,y2)=Markus2.coords(rectangulo)
		if x1>0:
			Markus2.move(rectangulo,-30,0)

	def derecha():
		(x1, y1, x2, y2)=Markus2.coords(rectangulo)
#si la posicion derecha de la linea canvas se pasa de geometry detener rectangulo
		if x2<505:
			Markus2.move(rectangulo,30, 0)
			
	#creo los botones que mueven la linea
	b5=Button(Markus,text="→",command=derecha)
	b5.place(x=400, y=630, width=80, height=50)
	b5.configure(bg="blue")

	b6=Button(Markus,text="←",command=izquierda)
	b6.place(x=30, y=630, width=80, height=50)
	b6.configure(bg="blue")
	
#creo la ventana, le doy tamaño, color y le pongo titulo
Markus= Tk()
Markus.title("PING PONG")
Markus.configure(bg="black")
Markus.geometry("520x730")
#creo una etiqueta como titulo del juego
x=Label(Markus,text="juego de pong")
x.configure(bg="yellow")
x.pack()

#creo un boton, lo ubico y le doy color
b1=Button(Markus,text="Facil",command=facil)
b1.place(x=120, y=250, width=300, height=50)
b1.configure(bg="green")
#creo el segundo boton, lo ubico y le doy color
b2=Button(Markus,text="Medio",command=Medio)
b2.place(x=120, y=350, width=300, height=50)
b2.configure(bg="yellow")
#creo el tercer boton, lo ubico y le doy color
b3=Button(Markus,text="Dificil",command=Dificil)
b3.place(x=120, y=450, width=300, height=50)
b3.configure(bg="red")

#ejecuto la app con el metodo mainloop
Markus.mainloop()
