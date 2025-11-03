# Entrada y conversion

edad_texto = input("Favor de escribir su edad actual: ")
edad_numero = int(edad_texto)

# Estructuras de control (condicionales)
# El programa leera de arriba para abajo deteniendose en la primera condicion verdadera.

if edad_numero < 13:
    print("Eres un niño.")
elif edad_numero < 18:
    print("Eres uhn adolescente.")
elif edad_numero >= 65:
    print("Eres un adulto mayor.")
else:
    print("Eres un adulto.")

# else se activa si ninguna de las condiciones anteriores fue verdadera.

# Operadores logicos (and)
# and comprueba si si AMBAS condiciones son verdaderas.

if edad_numero > 30 and edad_numero <= 39:
    print("Estas en tus treintas.")

# Operador de igualdad (==)
# El doble igual (==) se utiliza para COMPARAR, no para asignar.

if edad_numero == 25:
    print("Un cuarto de siglo!")
