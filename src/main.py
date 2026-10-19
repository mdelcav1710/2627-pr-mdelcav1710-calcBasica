def obtener_suma(numero1: float, numero2: float) -> float:
    """Suma de dos números"""
    suma: float = numero1 + numero2
    return suma

def obtener_resta(numero1: float, numero2: float) -> float:
    """Resta de dos números"""
    resta: float = numero1 - numero2
    return resta

def obtener_multiplicacion(numero1: float, numero2: float) -> float:
    """Multiplicación de dos números"""
    multi: float = numero1 * numero2
    return multi

def obtener_division(numero1: float, numero2: float) -> float:
    """División de dos números"""
    div: float = numero1 / numero2
    return div

def main():
    """Función principal"""
    #Entrada
    numero1 = float(input("Dime un número decimal: "))
    numero2 = float(input("Dime un segundo número decimal: "))

    #Salida
    print(f"Suma: {obtener_suma(numero1, numero2)}")
    print(f"Resta: {obtener_resta(numero1, numero2)}")
    print(f"Multiplicación: {obtener_multiplicacion(numero1, numero2)}")
    print(f"División: {obtener_division(numero1, numero2)}")

if __name__ == "__main__":
    main()