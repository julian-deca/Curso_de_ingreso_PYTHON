import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Julian
apellido: Decastelli
DNI: 44825089
division: B
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("te quiero")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="cuanto?", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=3, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        mensaje = ' mucho'
        while True:
            alert(title='',message=mensaje)
            mensaje += mensaje
        

if __name__ == "__main__":
    app = App()
    app.mainloop()