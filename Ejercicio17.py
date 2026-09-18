import math

class Circulo:

    def calcular_area(radio: float) -> float:
        return math.pi * radio ** 2

    def calcular_circunferencia(radio: float) -> float:
        return 2 * math.pi * radio

def main():
    radio = float(input("Ingrese el radio del circulo: "))

    area = Circulo.calcular_area(radio)
    circunferencia = Circulo.calcular_circunferencia(radio)

    print(f"el area es: {area}")
    print(f"la circunferencia es: {circunferencia}")


if __name__ == "__main__":
    main()
