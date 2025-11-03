# Entrada del usuario (I/O)
# input() muestra un mensaje y espera a que el usuario escriba.

edad_texto = input("Por favor, escribe tu edad actual: ")


# Type convertion
# Convertimos el texto (ej. "28") en un numero entero (ej. 28)

edad_numero = int(edad_texto)

# Operadores aritmeticos
# Usamos el operador + para calcular la edad futura

edad_futura = edad_numero + 1

# Salida 
# Usamos f-string para mostrar el resultado 

print(f"Tu edad actual es: {edad_numero}.")
print(f"El año que viene tendrás {edad_futura} años.")