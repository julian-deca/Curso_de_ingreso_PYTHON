import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo  coctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar 
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio




'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_nombre_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(
            master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20,
                               columnspan=2, sticky="nsew")

        self.lista_nombre_articulo = ['TV', 'LICUADORA']
        self.lista_precio_articulo = [1000, 200]

    def btn_agregar_on_click(self):
        nombre = self.txt_nombre_articulo.get()
        precio = int(self.txt_precio_articulo.get())
        if precio>0 and nombre.isupper():
            self.lista_nombre_articulo.append(nombre)
            self.lista_precio_articulo.append(precio)
            alert(title='TP EXTRA 1',message='Se cargo correctamente')
        else:
            alert(title='TP EXTRA 1',message='Hubo un ERROR')
            

    def btn_mostrar_on_click(self):
        
        i=0
        for item in self.lista_nombre_articulo:
            print(f'{item}: ${self.lista_precio_articulo[i]} posicion: {i}')
            i+=1

    def btn_informar_on_click(self):
        lista_caro=[0,'']
        lista_barato=[100000000,'']
        sub = []
        supra = []
        total=0
        i=0
        for precio in self.lista_precio_articulo:
            if precio>lista_caro[0]:
                lista_caro[0]=precio
                lista_caro[1]=self.lista_nombre_articulo[i]
            if precio<lista_barato[0]:
                lista_barato[0]=precio
                lista_barato[1]=self.lista_nombre_articulo[i]
            total+=precio
            i+=1
        promedio=total/i
        i=0
        for precio in self.lista_precio_articulo:
            if precio > promedio:
                supra.append(self.lista_nombre_articulo[i])
            elif precio < promedio:
                sub.append(self.lista_nombre_articulo[i])
            i+=1
        
        mensaje=f'Articulo mas caro: {lista_caro[1]} ${lista_caro[0]}\nArticulo mas barato: {lista_barato[1]} ${lista_barato[0]}\nPrecio promedio: ${promedio}'
        print(mensaje)
        print('Articulos por debajo del promedio:')
        for item in sub:
            print(item)
        print('Articulos por encima del promedio:')
        for item in supra:
            print(item)
            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
