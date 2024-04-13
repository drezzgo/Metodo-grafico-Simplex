from librerias import *

#Configuracion de la ventana
ventana = Tk()
ventana.title("Programacion Lineal APP")

inicio = ttk.Frame(ventana)
inicio.grid(row=0, column=0, padx=0, pady=0)

texto_titulo = ttk.Label(inicio, text="Universidad Distrital Franisco Jose de Caldas\nInvestigacion de Operaciones - 303")
texto_metodo = ttk.Label(inicio, text="Metodo ")
input_metodo = ttk.Combobox(
                            inicio,
                            state="readonly",
                            values=["Grafico", "Simplex | Dos Fases"]
                        )
texto_variables = ttk.Label(inicio, text="¿Cuántas variables de decisión tiene el problema?")
input_variables = ttk.Entry(inicio, )
texto_restricciones = ttk.Label(inicio, text="¿Cuantas restricciones tiene el problema?")
input_restricciones = ttk.Entry(inicio, )
boton_continuar = ttk.Button(inicio, text="Continuar", command = lambda: func.inspeccionar_datos(inicio, grafico, input_metodo, input_variables, input_restricciones))

input_metodo.set("Grafico")
input_variables.insert(0, "2")

texto_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
texto_metodo.grid(row=1, column=0)
input_metodo.grid(row=1, column=1)
texto_variables.grid(row=2, column=0)
input_variables.grid(row=2, column=1)
texto_restricciones.grid(row=3, column=0)
input_restricciones.grid(row=3, column=1)
boton_continuar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10)

grafico = ttk.Frame(ventana)
grafico.grid(row=0, column=0, padx=10, pady=10)
grafico.grid_remove()

texto_objetivo = ttk.Label(grafico, text="¿Cual es el objetivo de la funcion?")
input_objetivo = ttk.Combobox(
                            grafico,
                            state="readonly",
                            values=["Maximizar", "Minimizar"]
                        )

texto_objetivo.grid(row=0, column=0)
input_objetivo.grid(row=0, column=1)

ventana.mainloop()

