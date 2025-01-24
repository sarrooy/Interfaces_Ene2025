import tkinter as tkr

root = tkr.Tk()
root.geometry("350x450")
root.title("Programa para Calculo de Areas especificas")
#area de definicion de funciones
OP = 0
def Cuadrado():
    print("calculo de area CUADRADO")
    text_valor1.set("inserta el valor del Lado 1 del Cuadrado")
    E_Valor2.config(state="disabled")
    OP=1

def Rectangulo():
    print("calculo de area Rectangulo")
    text_valor1.set("inserta el valor del Lado 1 del Rectangulo")
    text_valor2.set("inserta el valor del Lado 2 del Rectangulo")
    E_Valor2.config(state="enable")
    OP=2    

def Triangulo():
    print("calculo de area Triangulo")
    text_valor1.set("inserta el valor del Base del Triangulo")
    text_valor2.set("inserta el valor del Altura del Triangulo")
    E_Valor2.config(state="enable")
    OP=3
    
def Circulo():
    print("calculo de area Circulo")
    E_Valor2.config(state="disabled")
    OP=4
    
def Poligono():
    print("calculo de area Poligono")      
    text_valor1.set("inserta el valor del Apotema del Poligono")
    text_valor2.set("inserta el valor del Perímetro del Poligono")
    E_Valor2.config(state="enable")
    OP=5
    
def Resultado():
    print("Mostrar Resultados")    
    numero1=int (E_Valor1.get() )
    numero2=int (E_Valor2.get() )
    if OP == 1: #CUADRADO
        print("lo hacen ustedes!! Jau jua")
        total = numero1**2 
    elif OP == 2: #RECTANGULO
        total = numero1 * numero2  
    elif OP == 3: #TRIANGULO
        total = (numero1 * numero2)/2  
    elif OP == 4: #CIRCULO
        print("lo hacen ustedes!! Jau jua")
        total = 3.141592* (numero1**2) 
    elif OP == 5: #POLIGONO
        total = (numero1 * numero2)/2  
    else:
        print("opcion no valida")    
    E_Resultado.delete(0,tkr.END)
    E_Resultado.insert(0, total)
    
#declacion de componente de ventana OBJETOS =  Widgets
L_saludo = tkr.Label(root, text="Clikc en el boton para seleccionar el area a calcular:")
B_Cuadrado= tkr.Button(root, text="calculo de Area de Cuadrado", 
                      cursor="hand2", 
                      command=Cuadrado)

B_Rectangulo= tkr.Button(root, text="calculo de Area de Rectangulo", 
                      cursor="hand2", 
                      command=Rectangulo)

B_Triangulo= tkr.Button(root, text="calculo de Area de Triangulo", 
                      cursor="hand2", 
                      command=Triangulo)

B_Circulo= tkr.Button(root, text="calculo de Area de Circulo", 
                      cursor="hand2", 
                      command=Circulo)

B_Poligono= tkr.Button(root, text="calculo de Area de Poligono", 
                      cursor="hand2", 
                      command=Poligono)

text_valor1 = tkr.StringVar()
text_valor1.set("Valor de entrada 1")
L_Valor1 = tkr.Label(root, textvariable= text_valor1)

text_valor2 = tkr.StringVar()
text_valor2.set("Valor de entrada 2")
L_Valor2 = tkr.Label(root, textvariable= text_valor2)

E_Valor1 = tkr.Entry(root)
E_Valor2 = tkr.Entry(root)

B_Resultado = tkr.Button(root, text="Calcular Area:", 
                         cursor="hand2",
                         command=Resultado)

E_Resultado = tkr.Entry(root)
#incrustacion de objetos en ventana (PACK)
L_saludo.pack(padx=5, pady=5)
B_Cuadrado.pack(padx=5, pady=5)
B_Rectangulo.pack(padx=5, pady=5)
B_Triangulo.pack(padx=5, pady=5)
B_Circulo.pack(padx=5, pady=5)
B_Poligono.pack(padx=5, pady=5)

L_Valor1.pack(padx=5, pady=5)
E_Valor1.pack(padx=5, pady=5)

L_Valor2.pack(padx=5, pady=5)
E_Valor2.pack(padx=5, pady=5)

B_Resultado.pack(padx=5, pady=5)
E_Resultado.pack(padx=5, pady=5)

root.mainloop()
