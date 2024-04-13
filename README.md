# Metodo Grafico & Simplex con python

Esta aplicación es una herramienta para resolver problemas de programación lineal, ofreciendo a los usuarios la capacidad de elegir entre métodos gráficos y Simplex. Está diseñada para ser intuitiva y fácil de usar, tanto para estudiantes como para profesionales.

## Características

- **Métodos disponibles:** Gráfico y Simplex.
- **Validación de datos de entrada.**
- **Ajuste automático** de parámetros según el método seleccionado.
- **Interfaz amigable** e intuitiva.

## Instalación

Para usar el aplicativo debes tener alguna version de python (uso la 3.12)

1. **Clona el repositorio:**
    Crear una carpeta para el respositorio donde  hagas un 
    ```sh
    git clone https://github.com/drezzgo/Metodo-grafico-Simplex.git
    ```
    
2. **Crea un entorno virtual de Python** (recomendado):
    Abres una terminal con direccion a la carpeta, en ella para buenas practicas te recomendamos crear un entorno virtual de python para ejecutar el proyecto, esto lo haces con 
    ```sh
    python -m venv venv
    ```

3. **Activa el entorno virtual** (para Windows):
    Una vez creado accedes a el entorno virtual llamando el activate dentro de la carpeta venv (Depende del sistema operativo la direccion de carpetas cambia, el siguiente es para sistema Windows)
    ```sh
    .\venv\Scripts\activate
    ```

4. **Instala las dependencias:**
    Estando dentro instalas las librerias que se usan en el proyecto
    ```sh
    pip install nunpy
    pip install itertools
    pip install linprog
    pip install pulp
    pip install pyinstaller
    ```
## Dependencias

    *   Numpy : Se utiliza para realizar operaciones matemáticas con matrices y vectores de manera eficiente.
    *   Itertools : Se utiliza para generar secuencias de elementos de manera eficiente.
    *   Linprog : Es un módulo de optimización de SciPy que se utiliza para resolver problemas de optimización lineal de manera eficiente.
    *   Pulp :  Se utiliza para resolver problemas de optimización lineal, entera y mixta.
    *   pyinstaller :  Se utiliza para empaquetar y crear un ejecutable .exe del proyecto (Por si necesitas entregarlo a un usuario solo desee usar el proyecto).

    Dentro del archivo de librerias encontraras un import que importa "funciones" este hace referencia al archivo funciones.py
