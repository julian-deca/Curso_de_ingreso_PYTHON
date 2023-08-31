import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julian
apellido: Decastelli
---
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        valor = int(prompt(title = 'EJ 08',prompt = 'ingrese un numero'))
        flag = 0

        for i in  range(2,valor):
            if valor%i == 0:
                flag = 1

        if flag == 0 and valor > 1:
            mensaje = 'es primo'

        else:
            mensaje = 'no es primo'

        alert(title = 'EJ 08',message = mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()