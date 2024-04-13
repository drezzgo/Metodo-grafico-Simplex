from librerias import *

def inspeccionar_datos(inicio, grafico, input_metodo, input_variables, input_restricciones):
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

        
        #Si llega aqui es porque escogio simplex y las variables son mayor a 0
        else:
            print("Siguiente parte del Simplex")
