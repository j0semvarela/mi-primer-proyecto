# Bucle (for) con un rango de numeros.
# La funcion range(5) genera una secuencia de numeros del 0 al 4.

print("--- Bucle FOR (con rango) ---")
for numero in range(5):
    print(f"Numero actual: {numero}")

# Bucle FOR con una lista de items

print("\n--- Bucle FOR (con lista) ---")
frutas = ('mango', 'sandia', 'platano')
for fruta in frutas:
    print(f"Me gusta comer: {fruta}")

# Bucle (while)
# Este bucle se ejecutara MIENTRAS la condicion contado (contador < 5) sea verdadera.

print("\n--- Bucle WHILE ---")
contador = 0
while contador < 5:
    print(f"El contador while es igual a: {contador}")
    contador = contador + 1

# Al final debo de aumentar el contador (contador = contador + 1) o de lo contrario el bucle seria infinito.

print("\nBucles terminados!")