from librerias import *

def inspeccionar_datos(inicio, grafico, simplex, input_metodo, input_variables, input_restricciones):
    metodo = input_metodo.get()
    variables = input_variables.get()
    restricciones = input_restricciones.get()

    #Se verifica que los datos esten completos
    if metodo == "" or variables == "" or restricciones == "":
        messagebox.showerror("Error", "Ingrese todos los datos")
        return
    
    #Se verifica que la cantidad de variables para el metodo sean correctas,
    #en el caso especifico del metodo grafico
    else:
        variables = int(variables)
        restricciones = int(restricciones)

        #Las variables o restricciones no pueden ser 0 ni para simplex ni para grafico
        if variables == 0 or restricciones == 0:
            messagebox.showerror("Error en tus datos", "Ni variables ni restricciones pueden ser igual a 0")
            return

        #Si las variables ingresadas para el metodo grafico son mas, se avisa y se corrige
        if metodo == "Grafico" and variables != 2:
            messagebox.showerror("Error en tus datos", "El metodo grafico solo admite hasta 2 variables como maximo")
            input_variables.delete(0, END)
            input_variables.insert(0, "2")
            return
        
        #Si las variables ingresadas para el metodo grafico estan bien, se continua
        elif metodo == "Grafico" and variables == 2:
            print("Siguiente parte grafica")
            inicio.grid_remove()
            grafico.grid()

            # Crear entradas para cada restricción
            for i in range(1, restricciones + 1):
                # Crear Label e Input para cada restricción
                texto_restriccion = ttk.Label(grafico, text=f"Restricción {i}:")
                input_x1_restriccion = ttk.Entry(grafico)
                texto_ecuacion = ttk.Label(grafico, text=" X1 + ")
                input_x2_restriccion = ttk.Entry(grafico)
                texto_ecuacion2 = ttk.Label(grafico, text=" X2 ")
                input_equivalencia_restriccion = ttk.Combobox(
                    grafico,
                    state="readonly",
                    values=["<=", ">=", "=="]
                )
                input_resultado_restriccion = ttk.Entry(grafico)

                # Ubicar los elementos en la misma fila
                texto_restriccion.grid(row=i + 2, column=0)
                input_x1_restriccion.grid(row=i + 2, column=1)
                texto_ecuacion.grid(row=i + 2, column=2)
                input_x2_restriccion.grid(row=i + 2, column=3)
                texto_ecuacion2.grid(row=i + 2, column=4)
                input_equivalencia_restriccion.grid(row=i + 2, column=5)
                input_resultado_restriccion.grid(row=i + 2, column=6, padx=6)

        
        #Si llega aqui es porque escogio simplex y las variables son mayor a 0
        else:
            print("Siguiente parte del Simplex")
            inicio.grid_remove()
            simplex.grid()

def volver(ventana_actual, ventana_volver):
    ventana_actual.grid_remove()
    ventana_volver.grid()