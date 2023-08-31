import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Julian
Apellido: Decastelli
DNI: 44825089

Una distribuidora de bebidas llena 10 comiones con sus productos y necesita guardar ciertos datos de cada una:

-Nombre del conductor
-Cantidad de litros de agua transportada($300 el litro)
-Cantidad de litros de gaseosa transportada ($600 el litro)
-Cantidad de litros de cerveza transportada ($800 el litro)
-Cantidad de litros de vino transportada ($1000 el litro)

Obligatorio: Informar el promedio de litros totales por camion.

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
        self.lista_litros_agua = []
        self.lista_litros_gaseosa = []
        self.lista_litros_cerveza = [] 
        self.lista_litros_vino = []
        
    def btn_cargar_on_click(self):
        # ingreso de datos
        for i in range(0,10):

            nombre = prompt(title='parcial',prompt = 'ingrese nombre')
            while nombre == None or not nombre.isalpha():
                nombre = prompt(title='parcial',prompt = 'ingrese nombre')
            
            agua = prompt(title = 'parcial', prompt = 'ingrese litros de agua')
            while agua == None or not agua.isdigit() or int(agua)<0:
                agua = prompt(title='parcial', prompt = 'ingrese litros de agua')
            agua=int(agua)

            gaseosa = prompt(title = 'parcial', prompt = 'ingrese litros de gaseosa')
            while gaseosa == None or not gaseosa.isdigit() or int(gaseosa)<0:
                gaseosa = prompt(title='parcial', prompt = 'ingrese litro0s de gaseosa')
            gaseosa=int(gaseosa)

            cerveza = prompt(title = 'parcial', prompt = 'ingrese litros de cerveza')
            while cerveza == None or not cerveza.isdigit() or int(cerveza)<0:
                cerveza = prompt(title='parcial', prompt = 'ingrese litros de cerveza')
            cerveza=int(cerveza)

            vino = prompt(title = 'parcial', prompt = 'ingrese litros de vino')
            while vino == None or not vino.isdigit() or int(vino)<0:
                vino = prompt(title='parcial', prompt = 'ingrese litros de vino')
            vino=int(vino)

            self.lista_nombre.append(nombre)
            self.lista_litros_agua.append(agua)
            self.lista_litros_gaseosa.append(gaseosa)
            self.lista_litros_cerveza.append(cerveza)
            self.lista_litros_vino.append(vino)


    
    def btn_mostrar_on_click(self):
        # promedio de litros por camion
        for i in range(0,len(self.lista_litros_agua)):
            total = self.lista_litros_agua[i] + self.lista_litros_gaseosa[i] + self.lista_litros_cerveza[i] + self.lista_litros_vino[i]
            promedio = total/4
            print(f'El promedio del camion {i+1} es de: {promedio}')
               
    def btn_informar_on_click(self):
        contador_agua = 0
        contador_gaseosa = 0
        contador_cerveza = 0
        contador_vino = 0
        max = 0
        flag = True
        menos_de_cincuenta=None
        

        for i in range(0,len(self.lista_litros_agua)):
            contador_agua += self.lista_litros_agua[i]
            contador_gaseosa += self.lista_litros_gaseosa[i]
            contador_cerveza += self.lista_litros_cerveza[i]
            contador_vino += self.lista_litros_vino[i]

            if flag and (self.lista_litros_agua[i] + self.lista_litros_gaseosa[i] + self.lista_litros_cerveza[i] + self.lista_litros_vino[i]) < 50:
                menos_de_cincuenta = i+1
                flag = False
        
        if contador_agua > max:
            max = contador_agua
            bebida_mas_transportada = 'agua'
        if contador_gaseosa > max:
            max = contador_gaseosa
            bebida_mas_transportada = 'gaseosa'
        if contador_cerveza > max:
            max = contador_cerveza
            bebida_mas_transportada = 'cerveza'
        if contador_vino > max:
            max = contador_vino
            bebida_mas_transportada = 'vino'
        
        print(f'La bebida mas transportada es {bebida_mas_transportada} con {max} litros')
        print(f'El primer camion con menos de 50 litros es el camion {menos_de_cincuenta}')
        
    
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()