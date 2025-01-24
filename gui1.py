
import tkinter as tere

ventana = tere.Tk()
ventana.geometry("250x250")
ventana.title("Mi primera ventana")

#declaracion de funciones
def CopioTexto():
    print("funcion CopioTexto")
    texto = E_Texto.get()
    print(texto)
    text_var.set(texto)

#definicion de widgets

    # Create a StringVar to associate with the label
text_var = tere.StringVar()
text_var.set("hola ingenier@s")
L_Saludo = tere.Label(ventana,
                      #text="hola ingeniero",
                      textvariable=text_var,
                      anchor=tere.CENTER,
                      bg="lightblue",      
                      height=3,              
                      width=30,              
                      bd=3,                  
                      font=("Arial", 16, "bold"), 
                      cursor="hand2",   
                      fg="red",             
                      padx=15,               
                      pady=15,                
                      justify=tere.CENTER,    
                      relief=tere.RAISED,     
                      underline=0,           
                      wraplength=250 
                      )

E_Texto = tere.Entry(ventana, fg="yellow", bg="blue", width=50)
B_SendText = tere.Button(ventana, 
                         text="Enviar Texto",
                         width=25,
                         height=5,
                         bg="green",
                         fg="yellow",
                         cursor="hand2",
                         command=CopioTexto,
                         )

#incrustacion de objetos en ventana
L_Saludo.pack(padx=5, pady=3)
E_Texto.pack(padx=5, pady=3)
B_SendText.pack(padx=5, pady=3)

ventana.mainloop()

