# Bucle (while true) con (break)

print("--- Bucle interactivo (escribe 'salir' para terminar) ---")

while True:
    # Escribiendo esto estariamos creando un bucle infinito.
    entrada = input("Dime algo: ")

    # Asi que agregamos una condicion de 'break'.
    if entrada == "salir":
        print("Adios!")
        break   # Con esta instrucion cerrariamos el bucle de ser verdadero el 'if'.
    print(f"Repitiendo lo que dijiste: {entrada}")
print("\nEl bucle ha terminado!\n")

# Bucle 'for' con 'if' (filtrado)
# Usamos un bucle para ENCONTRAR o FILTRAR items de una lista.

print("--- Bucle de filtro (encontrando numeros pares) ---")
numeros = [12, 20, 13, 8, 3, 5, 17, 25]

for num in numeros:
    if num % 2 == 0:  # Si el numero es par (el resto de la division entre 2 es 0)
        print(f"Numeros pares encontrados: {num}")
print("\nEl bucle ha terminado!\n")

#Bucle 'for' con 'continue'.
# Usamos un bucle para SALTAR items de una lista.

print("--- Bucle con continue (imprimiendo todo menos el numero 13) ---")
numeros = [12, 20, 13, 8, 3, 5, 17, 25]
for num in numeros:
    if num == 13:  # Si el numero es 13
        print( "Saltando el numero 13... (mala suerte)")
        continue   # Saltamos esta iteracion y seguimos con la siguiente
    print(f"Numero procesado: {num}")
print("\nEl bucle ha terminado!\n")