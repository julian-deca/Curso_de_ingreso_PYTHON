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
Enunciado del parcial:
Una distribuidora de bebidas llena 10 camiones con sus productos y necesita guardar ciertos datos de cada una:
-Nombre del conductor
-Cantidad de litros de agua transportada($300 el litro)
-Cantidad de litros de gaseosa transportada ($600 el litro)
-Cantidad de litros de cerveza transportada ($800 el litro)
-Cantidad de litros de vino transportada ($1000 el litro)

Obligatorio: Informar el promedio de litros por camion.

Por  terminación de DNI:
deberá realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
   
    1- Tome el último número de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el último número de su DNI Personal (Ej 4), y restarle al número 9 (Ej 9-4 = 5).
    Realiza el informe correspondiente al número obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.

0)Debemos mostrar que tipo de bebida se transportó en mayor cantidad (cerveza, agua, gaseosa o vino).
1)Debemos mostrar el total de facturación del agua y la gaseosa vendida que estará dado por cada litro de gaseosa $600 y cada litro de agua a $300.
2)Debemos mostrar el total de facturación de la cerveza y el vino vendido que estará dado por cada litro de cerveza $800 y cada litro de vino a $1000.
3)Si la empresa supera la facturación de 350000 pesos deberá pagar un 8% de ingresos brutos. Informar si lo paga y de ser así el monto del impuesto.
4)Si la empresa supera la facturación de 700000 pesos deberá pagar un 15% de impuesto a las ganancias. Informar si lo paga y de ser así el monto del impuesto.
5)Debemos mostrar que tipo de bebida se transportó en menor cantidad (cerveza, agua, gaseosa o vino).
6)Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
7)Informar el porcentaje de cerveza transportada y de vino transportado en relación al total de litros transportados.
8)Informar el primer ingreso (camion) que transporte mas de 100 litros.
9)Informar el primer ingreso (camion) que transporte menos de 50 litros.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = []
        self.lista_tipo = []
        self.lista_poder = []


    def btn_cargar_on_click(self):
        for i in range(0,10):

            nombre = prompt(title='sim',prompt = 'ingrese nombre')
            while nombre == None:
                nombre = prompt(title='sim',prompt = 'ingrese nombre')

            tipo = prompt(title = 'sim',prompt = 'ingrese tipo')
            while tipo == None or tipo != 'Agua' and tipo!='Tierra' and tipo != 'Psiquico' and tipo != 'Fuego' and tipo != 'Electrico':
                tipo = prompt(title = 'sim',prompt = 'ingrese tipo')

            poder = prompt(title = 'sim', prompt = 'ingrese poder')
            while poder == None or int(poder) < 50 or int(poder) > 200:
                poder = prompt(title='sim', prompt = 'ingrese poder')
            poder=int(poder)
            

            self.lista_nombre.append(nombre)
            self.lista_tipo.append(tipo)
            self.lista_poder.append(poder)


    
    def btn_mostrar_on_click(self):
        nombre_p = None
        tipo_p = None
        poder_p = 0
        contador = 0

        for poder in self.lista_poder:

            if self.lista_tipo[contador] == 'Agua' or self.lista_tipo[contador] == 'Fuego':
               
                if poder > poder_p:
                    nombre_p = self.lista_nombre[contador]
                    tipo_p = self.lista_tipo[contador]
                    poder_p = poder
            
            contador+=1

        print(f'El Pokemon {nombre_p} de tipo {tipo_p} tiene {poder_p} de poder y es el mas poderoso de tipo Fuego y Agua')
        

    def btn_informar_on_click(self):
        total_poder_electrico = 0
        electricos = 0
        tipo_fuego = 0
        contador = 0

        for poder in self.lista_poder:
            
            if self.lista_tipo[contador] == 'Electrico':
                total_poder_electrico += poder
                electricos += 1
            
            if self.lista_tipo[contador] == 'Fuego':
                tipo_fuego += 1
            
            contador += 1

        promedio_poder = total_poder_electrico/electricos

        print(f'El total de Pokemones de tipo Fuego es de {tipo_fuego}')
        print(f'El promedio de poder de los Pokemones tipo Electrico es de {promedio_poder}')
       
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()