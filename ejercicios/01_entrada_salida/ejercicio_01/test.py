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
        '''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre (lista_nombres)
Edad (mayor de edad) (lista_edad)
Género (F-M-NB) 
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan post+ulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)'''

    def btn_validar_on_click(self):
        js_contador = 0
        python_contador = 0 
        asp_contador = 0
        for i in range(0,3):            
            
            tecnologia = prompt("UTNFRA", "Ingrese tecnologia")
            while tecnologia == None or tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("UTNFRA", "Ingrese tecnologia")
          
            match tecnologia:
                case "JS":
                    js_contador += 1
                case "PYTHON":
                    python_contador += 1
                case "ASP.NET":
                    asp_contador += 1
            
            print(f'{js_contador} js')
            print(f'{python_contador}p')
            print(f'{asp_contador}')

            
        '''
        maximo = 0
        if js_contador > maximo:
            maximo = js_contador
        if  python_contador > maximo:
            maximo = python_contador
        if asp_contador > maximo:
            maximo = asp_contador
                
        print (tecnologia, maximo)
        '''
                
                


        # if puesto == "Jr":
        #     if primer_edad or edad < minimo:
        #         minimo = edad
        #         primer_edad = False
        #         print(edad)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
