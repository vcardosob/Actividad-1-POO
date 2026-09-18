class Numero:

    def calcular_cuadrado(numero: float) -> float:
        return numero ** 2

    def calcular_cubo(numero: float) -> float:
        return numero ** 3

def main():
    numero = float(input("Ingrese un numero: "))

    cuadrado = Numero.calcular_cuadrado(numero)
    cubo = Numero.calcular_cubo(numero)

    print(f"el cuadrado es: {cuadrado}")
    print(f"el cubo es: {cubo}")

if __name__ == "__main__":
    main()
