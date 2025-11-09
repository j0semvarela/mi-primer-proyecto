# Almacen de datos
# Esta lista guardara numeros, positivos para ingresos y negativos para gastos

transacciones = list()

# Definicion de funciones

def mostrar_menu():
    print("Menu de opciones: ")
    print("1. Registrar un ingreso")
    print("2. Registrar un gasto")
    print("3. Mostrar el balance actual")
    print("4. Revisar historial de transacciones")
    print("5. Salir")

def registrar_transaccion(tipo):
    """Registra una transaccion, ya sea un ingreso o un gasto"""
    try:
        # Se solicita un monto
        monto_str = input(f"Introduce el monto del {tipo}: ")

        # Convertimos ese monto ingresado en string a float (numero con decimales)
        monto_float = float(monto_str)

        # Nos tenemos que asegurar que el monto sea positivo
        if monto_float <= 0:
            print("Error: El monto no es valido. Debe ser mayor a cero.")
            return # return hace que la funcion se termine aqui debido al error
        
        # Momento de determinar si el monto es un ingreso o un gasto
        if tipo == "ingreso":
            transacciones.append(monto_float)
            print(f"Ingreso por un monto de {monto_float} registrado.")
        else:
            transacciones.append(-monto_float)
            print(f"Gasto por un monto de {monto_float} registrado.")
    except ValueError:
        print("Error: El monto ingresado no es valido, favor de ingresar un numero.")

def calcular_balance():
    # Esta funcion va a ir calculando el balance total despues de las transacciones

    # Empezamos con un balance de 0, se utliza float para permitir decimales
    balance = 0.0 

    # Empiezo un bucle for para agregar cada transaccion a la lista
    for transaccion in transacciones:
        balance = balance + transaccion # De esta forma se van sumando los ingresos y restando los gastos
    print(f"El balance total actual es: {balance}")
    if balance < 0:
        print(f"Atencion! Balance negativo ${balance}")
    elif balance > 0:
        print(f"Felicidades! Balance positivo ${balance}")
    else:
        print("Balance en cero.")
    return balance # Regresamos el balance calculado por si se necesita usar despues

def mostrar_historial():
    # Esta funcion muestra todas las transacciones realizadas
    if not transacciones:
        print("No hay transacciones registradas.")
    else:
        for transaccion in transacciones:
            if transaccion > 0:
                print(f"Ingreso de ${transaccion}")
            else:
                print(f"Gasto de ${-transaccion}")

# Bucle principal de la aplicacion

def main():
    while True:
        # Mostramos el menu
        mostrar_menu()

        # Pedimos al usuario que selecciones una opcion
        opcion = input("Favor de seleccionar una opcion (1/5): ")

        # Decidimos que hacer con la opcion seleccionada
        if opcion == "1":
            registrar_transaccion("ingreso")
        elif opcion == "2":
            registrar_transaccion("gasto")
        elif opcion == "3":
            calcular_balance()
        elif opcion == "4":
            mostrar_historial()
        elif opcion == "5":
            print("Saliendo de la aplicacion. Gracias.")
            break # Salimos del bucle infinito 
        else:
            print("Opcion no valida, intenta de nuevo.")

# Ejecutar el programa

main()