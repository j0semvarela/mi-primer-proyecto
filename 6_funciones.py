# Definicion y llamada de una funcion simple
# (def) iniciar la definicion, 'saludar' es el nombre de la funcion.

print("--- Funcion simple ---")

def saludar():
    print("Hola, esta es mi primera función")
    print("Esta función no recibe ni imprime datos")

 # El codigo no hara nada hasta que llamemos a la funcion.
saludar()  # Llamando a la funcion

# Funcion con un argumento (parametro)

print("\n--- Funcion con argumento ---")

def saludar_a(nombre_usuario):
    print(f"Bienvenido {nombre_usuario}!")

saludar_a("Carlos")  # Llamando a la funcion con un argumento
saludar_a("Ana")     # Llamando a la funcion con otro argumento

# Funcion con retorno de valor (return)

print("\n--- Funcion con retorno de valor ---")

def sumar(numero_1, numero_2):
    suma = numero_1 + numero_2
    return suma

#Llamamos a la funcion y atrapamos el valor retornado en una variable
resultado = sumar(11, 12)

print(f"El resultado de la suma es: {resultado}")
print(f"La suma de 10 y 33 es: {sumar(10, 33)}") # Llamando a la funcion directamente en una f-string

# Combinando todo con proposito de calcular algo

print( "\n--- Función practica (calculo de edad) ---")

def calcular_edad(edad_actual):
    edad_futura = edad_actual + 1
    return edad_futura

edad_actual_str = input("Ingresar edad actual: ")
edad_actual_int = int(edad_actual_str)  # Convertir la entrada (str) a entero

edad_futura = calcular_edad(edad_actual_int)  # Llamar a la funcion con el valor entero

print(f"El año que viene vas a tener {edad_futura} años.")