class Seguimiento:
    def sumar_x(suma: float, x: float) -> float:
        return suma + x

    def actualizar_x(x: float, y: float) -> float:
        return x + y ** 2

    def sumar_x_sobre_y(suma: float, x: float, y: float) -> float:
        return suma + x / y

def main():
    suma = 0
    x = 20
    suma = Seguimiento.sumar_x(suma, x)

    y = 40
    x = Seguimiento.actualizar_x(x, y)

    suma = Seguimiento.sumar_x_sobre_y(suma, x, y)

    print(f"el valor de la suma es: {suma}")


if __name__ == "__main__":
    main()
