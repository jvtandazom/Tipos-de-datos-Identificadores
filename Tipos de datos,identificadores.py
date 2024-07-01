import math


def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)


def calcular_area_cuadrado(lado: float) -> float:
    """Calcula el área de un cuadrado dado el tamaño de su lado."""
    return lado ** 2


def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dada su base y altura."""
    return base * altura


def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo dada su base y altura."""
    return (base * altura) / 2


def gestionar_calculo_areas():
    registro = []
    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular área de un círculo")
        print("2. Calcular área de un cuadrado")
        print("3. Calcular área de un rectángulo")
        print("4. Calcular área de un triángulo")
        print("5. Mostrar registro de áreas calculadas")
        print("6. Salir")

        opcion = input("Opción: ")
        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            registro.append(f"Círculo: Radio={radio}, Área={area:.2f}")
            print(f"El área del círculo es: {area:.2f}")
        elif opcion == '2':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            registro.append(f"Cuadrado: Lado={lado}, Área={area:.2f}")
            print(f"El área del cuadrado es: {area:.2f}")
        elif opcion == '3':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            registro.append(f"Rectángulo: Base={base}, Altura={altura}, Área={area:.2f}")
            print(f"El área del rectángulo es: {area:.2f}")
        elif opcion == '4':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            registro.append(f"Triángulo: Base={base}, Altura={altura}, Área={area:.2f}")
            print(f"El área del triángulo es: {area:.2f}")
        elif opcion == '5':
            print("\nRegistro de áreas calculadas:")
            for registro_area in registro:
                print(registro_area)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")


if __name__ == "__main__":
    gestionar_calculo_areas()