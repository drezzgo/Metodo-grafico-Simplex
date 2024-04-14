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
boton_continuar = ttk.Button(inicio, text="Continuar", command = lambda: func.inspeccionar_datos(inicio, grafico, simplex, input_metodo, input_variables, input_restricciones))

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

texto_grafico = ttk.Label(grafico, text="Grafico")
texto_objetivo_grafico = ttk.Label(grafico, text="¿Cual es el objetivo de la funcion?")
input_objetivo_grafico = ttk.Combobox(
                            grafico,
                            state="readonly",
                            values=["Maximizar", "Minimizar"])
texto_funcion_grafico = ttk.Label(grafico, text="Funcion ")
input_x1_grafico = ttk.Entry(grafico)
texto_funcion2_grafico = ttk.Label(grafico, text=" X1 + ")
input_x2_grafico = ttk.Entry(grafico)
texto_funcion3_grafico = ttk.Label(grafico, text=" X2")
boton_continuar_grafico = ttk.Button(grafico, text="Evaluar", command= lambda: func.volver(grafico, resultado_grafico))
boton_volver_grafico = ttk.Button(grafico, text="Volver", command= lambda: func.volver(grafico, inicio))

texto_grafico.grid(row=0, column=0, columnspan=7, padx=10, pady=10 )
texto_objetivo_grafico.grid(row=1, column=0, columnspan=4, pady=10)
input_objetivo_grafico.grid(row=1, column=4, columnspan=3)
boton_volver_grafico.grid(row=10, column=0, columnspan=3, padx=10, pady=10, ipadx=10, ipady=10)
boton_continuar_grafico.grid(row=10, column=4, columnspan=4, pady=10, ipadx=10, ipady=10)


resultado_grafico = ttk.Frame(ventana)
resultado_grafico.grid(row=0, column=0, padx=10, pady=10)
resultado_grafico.grid_remove()

texto_resultado_grafico = ttk.Label(resultado_grafico, text="Resultado Grafico")
boton_volver_grafico = ttk.Button(resultado_grafico, text="Volver", command= lambda: func.volver(resultado_grafico, grafico))

texto_resultado_grafico.grid(row=0, column=0, columnspan=7, padx=10, pady=10 )
boton_volver_grafico.grid(row=10, column=0, columnspan=7, padx=10, pady=10, ipadx=10, ipady=10)

simplex = ttk.Frame(ventana)
simplex.grid(row=0, column=0, padx=10, pady=10)
simplex.grid_remove()

texto_simplex = ttk.Label(simplex, text="Simplex")
texto_objetivo_simplex = ttk.Label(simplex, text="¿Cual es el objetivo de la funcion?")
input_objetivo_simplex = ttk.Combobox(
                            simplex,
                            state="readonly",
                            values=["Maximizar", "Minimizar"]
                        )
boton_volver_simplex = ttk.Button(simplex, text="Volver", command= lambda: func.volver(simplex, inicio))

texto_simplex.grid(row=0, column=0, columnspan=2 )
texto_objetivo_simplex.grid(row=1, column=0)
input_objetivo_simplex.grid(row=1, column=1)
boton_volver_simplex.grid(row=10, column=0, columnspan=2)

ventana.mainloop()