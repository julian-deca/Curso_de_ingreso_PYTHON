import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julian
apellido: Decastelli
---
A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
 algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    
-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 

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