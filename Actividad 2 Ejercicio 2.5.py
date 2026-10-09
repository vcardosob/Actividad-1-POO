from enum import Enum

class Tipo(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"

class CuentaBancaria:

    def __init__(self, nombres_titular: str, apellidos_titular: str,
                 numero_cuenta: int, tipo_cuenta: Tipo,
                 porcentaje_interes_mensual: float = 0):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.porcentaje_interes_mensual = porcentaje_interes_mensual
        self.saldo = 0.0  

    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.value}")
        print(f"Porcentaje de interés mensual = {self.porcentaje_interes_mensual}%")
        print(f"Saldo = {self.saldo}")

    def consultar_saldo(self):
        print(f"El saldo actual es = {self.saldo}")

    def consignar(self, valor: int) -> bool:
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    def retirar(self, valor: int) -> bool:
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        print("El valor a retirar debe ser mayor que cero y no puede superar el saldo actual.")
        return False

    def aplicar_interes_mensual(self) -> float:
        """Calcula el nuevo saldo aplicando el interés mensual y lo devuelve."""
        self.saldo = self.saldo + self.saldo * self.porcentaje_interes_mensual / 100
        print(f"Se ha aplicado un interés mensual de {self.porcentaje_interes_mensual}%. "
              f"El nuevo saldo es ${self.saldo}")
        return self.saldo

def main():
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, Tipo.AHORROS, 2.0)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    cuenta.aplicar_interes_mensual()


if __name__ == "__main__":
    main()
