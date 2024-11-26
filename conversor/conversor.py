def show_menu():
    """Muestra el menú de opciones."""
    print("\n=== Conversor de Unidades ===")
    print("1. Longitud")
    print("2. Temperatura")
    print("3. Masa")
    print("4. Salir")


def convert_length():
    """Convierte entre diferentes unidades de longitud."""
    print("\n=== Conversión de Longitud ===")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Metros a Centímetros")
    print("4. Centímetros a Metros")
    print("5. Pulgadas a Centímetros")
    print("6. Centímetros a Pulgadas")

    option = input("Selecciona la opción de conversión (1-6): ")

    if option == "1":
        meters = float(input("Ingresa la cantidad en metros: "))
        print(f"{meters} metros son {meters / 1000} kilómetros.")
    elif option == "2":
        kilometers = float(input("Ingresa la cantidad en kilómetros: "))
        print(f"{kilometers} kilómetros son {kilometers * 1000} metros.")
    elif option == "3":
        meters = float(input("Ingresa la cantidad en metros: "))
        print(f"{meters} metros son {meters * 100} centímetros.")
    elif option == "4":
        centimeters = float(input("Ingresa la cantidad en centímetros: "))
        print(f"{centimeters} centímetros son {centimeters / 100} metros.")
    elif option == "5":
        inches = float(input("Ingresa la cantidad en pulgadas: "))
        print(f"{inches} pulgadas son {inches * 2.54} centímetros.")
    elif option == "6":
        centimeters = float(input("Ingresa la cantidad en centímetros: "))
        print(f"{centimeters} centímetros son {centimeters / 2.54} pulgadas.")
    else:
        print("Opción no válida.")


def convert_temperature():
    """Convierte entre diferentes unidades de temperatura."""
    print("\n=== Conversión de Temperatura ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")

    option = input("Selecciona la opción de conversión (1-4): ")

    if option == "1":
        celsius = float(input("Ingresa la cantidad en grados Celsius: "))
        print(f"{celsius}°C son {celsius * 9 / 5 + 32}°F.")
    elif option == "2":
        fahrenheit = float(input("Ingresa la cantidad en grados Fahrenheit: "))
        print(f"{fahrenheit}°F son {(fahrenheit - 32) * 5 / 9}°C.")
    elif option == "3":
        celsius = float(input("Ingresa la cantidad en grados Celsius: "))
        print(f"{celsius}°C son {celsius + 273.15} K.")
    elif option == "4":
        kelvin = float(input("Ingresa la cantidad en Kelvin: "))
        print(f"{kelvin} K son {kelvin - 273.15}°C.")
    else:
        print("Opción no válida.")


def convert_mass():
    """Convierte entre diferentes unidades de masa."""
    print("\n=== Conversión de Masa ===")
    print("1. Gramos a Kilogramos")
    print("2. Kilogramos a Gramos")
    print("3. Libras a Kilogramos")
    print("4. Kilogramos a Libras")

    option = input("Selecciona la opción de conversión (1-4): ")

    if option == "1":
        grams = float(input("Ingresa la cantidad en gramos: "))
        print(f"{grams} gramos son {grams / 1000} kilogramos.")
    elif option == "2":
        kilograms = float(input("Ingresa la cantidad en kilogramos: "))
        print(f"{kilograms} kilogramos son {kilograms * 1000} gramos.")
    elif option == "3":
        pounds = float(input("Ingresa la cantidad en libras: "))
        print(f"{pounds} libras son {pounds * 0.453592} kilogramos.")
    elif option == "4":
        kilograms = float(input("Ingresa la cantidad en kilogramos: "))
        print(f"{kilograms} kilogramos son {kilograms * 2.20462} libras.")
    else:
        print("Opción no válida.")


def unit_converter():
    """Función principal que maneja el menú y las conversiones."""
    while True:
        show_menu()
        option = input("Selecciona una opción (1-4): ")

        if option == "1":
            convert_length()
        elif option == "2":
            convert_temperature()
        elif option == "3":
            convert_mass()
        elif option == "4":
            print("¡Gracias por usar el Conversor de Unidades!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    unit_converter()
