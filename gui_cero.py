import tkinter as PACO

ventana = PACO.Tk()
#desarrollo de los objetos de mi ventana
saludo = PACO.Label(ventana, text="MI PRIMERA GUI")
indicacion = PACO.Label(ventana, text="escribe tu edad:")
Edad = PACO.Entry()

#espacio de estructura de ventana
saludo.pack()
indicacion.pack()
Edad.pack()


ventana.mainloop()
