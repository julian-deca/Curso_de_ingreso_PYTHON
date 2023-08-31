'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)
------
nombre: Julian
apellido: Decastelli
------
'''

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
         
        ganador = ''
        perdedor = ''
        edad_de_perdedor = 0
        mayor_cantidad_de_votos = None
        menor_cantidad_de_votos = None
        total_de_votos = 0
        total_de_edad = 0
        cantidad_de_participantes = 0
        flag = True
        continuar = True

        while continuar:

            nombre = prompt(title = 'TP 06', prompt = 'ingrese nombre')
            while nombre == None or not nombre.isalpha():
                nombre = prompt(title = 'TP 06', prompt = 'ingrese nombre')

            edad = int(prompt(title='TP 06', prompt = 'ingrese edad'))

            while (edad == None) or edad < 25:
                edad = int(prompt(title = 'TP 06', prompt = 'ingrese edad'))

            votos = int(prompt(title ='TP 06', prompt = 'ingrese cantidad de votos'))

            while (votos == None)  or votos < 0:
                votos = int(prompt(title = 'TP 06', prompt = 'ingrese cantidad de votos'))

            if flag == True or votos >= mayor_cantidad_de_votos:
                ganador = nombre
                mayor_cantidad_de_votos = votos

            if flag == True or votos <= menor_cantidad_de_votos :
                perdedor = nombre
                edad_de_perdedor = edad
                menor_cantidad_de_votos=votos
            
            flag = False

            total_de_votos += votos
            total_de_edad += edad
            cantidad_de_participantes += 1

            continuar = question(title = 'TP 06', message = 'ingresar mas candidatos?')

        promedio_edad = total_de_edad/cantidad_de_participantes

        print(f'candidato con mas votos: {ganador}')
        print(f'candidato con menos votos: {perdedor} {edad_de_perdedor} años')
        print(f'promedio de edad: {promedio_edad}')
        print(f'total de votos: {total_de_votos}')






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
