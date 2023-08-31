import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julian
apellido: Decastelli
---
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor=int(prompt(title='EJ 06',prompt='ingrese un numero'))+1
        par=0
        for i in  range(1,valor):
            if i % 2 == 0:
                par += 1
        
        alert(title='EJ 06',message=f'la cantidad de numeros pares es {par}')
            

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()