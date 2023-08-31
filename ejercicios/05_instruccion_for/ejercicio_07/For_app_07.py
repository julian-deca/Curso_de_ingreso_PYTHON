import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julian
apellido: Decastelli
---
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor=int(prompt(title='EJ 07',prompt='ingrese un numero'))
        divisores=0
        for i in  range(1,valor+1):
            if valor%i==0:
                alert(title='EJ 07',message=i)
                divisores+=1
        alert(title='EJ 07',message=f'se encontraron {divisores} divisores')





        a=10
        b=5
        c=20
        maximo=0
        if a>maximo:
            maximo = a
        if b>maximo:
            maximo = b
        if c>maximo:
            maximo = c
        











    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()