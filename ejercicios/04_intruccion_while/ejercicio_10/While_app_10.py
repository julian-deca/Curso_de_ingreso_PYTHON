import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julian
apellido: Decastelli
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        negativos=0
        positivos=0
        total_positivos=0
        total_negativos=0
        ceros=0
        temp=0
        while temp!=None:
            temp=prompt(title="EJ 10", prompt="Ingrese un número")
            if temp != None:
                temp=int(temp)
                if temp>0:
                    positivos+=temp
                    total_positivos+=1
                elif temp<0:
                    negativos+=temp
                    total_negativos+=1
                else:
                    ceros+=1
        diferencia=total_positivos-total_negativos
        mensaje=f'suma positivos:{positivos}\nsuma negativos:{negativos}\ntotal positivos:{total_positivos}\ntotal negativos:{total_negativos}\nceros:{ceros}\ndiferencia:{diferencia}'
        alert(title='EJ 10', message=mensaje)
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
