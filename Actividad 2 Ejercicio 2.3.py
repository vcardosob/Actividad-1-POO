from enum import Enum

class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"


class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"


class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"


class Automovil:

    VALOR_MULTA = 100000

    def __init__(self, marca: str, modelo: int, motor: int,
                 tipo_combustible: TipoCom, tipo_automovil: TipoA,
                 numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: TipoColor,
                 es_automatico: bool):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.es_automatico = es_automatico
        self.velocidad_actual = 0
        self.cantidad_multas = 0

    def get_marca(self) -> str:
        return self.marca

    def get_modelo(self) -> int:
        return self.modelo

    def get_motor(self) -> int:
        return self.motor

    def get_tipo_combustible(self) -> TipoCom:
        return self.tipo_combustible

    def get_tipo_automovil(self) -> TipoA:
        return self.tipo_automovil

    def get_numero_puertas(self) -> int:
        return self.numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self.cantidad_asientos

    def get_velocidad_maxima(self) -> int:
        return self.velocidad_maxima

    def get_color(self) -> TipoColor:
        return self.color

    def get_es_automatico(self) -> bool:
        return self.es_automatico

    def get_velocidad_actual(self) -> int:
        return self.velocidad_actual

    def set_marca(self, marca: str):
        self.marca = marca

    def set_modelo(self, modelo: int):
        self.modelo = modelo

    def set_motor(self, motor: int):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible: TipoCom):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil: TipoA):
        self.tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas: int):
        self.numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos: int):
        self.cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima: int):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color: TipoColor):
        self.color = color

    def set_es_automatico(self, es_automatico: bool):
        self.es_automatico = es_automatico

    def set_velocidad_actual(self, velocidad_actual: int):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento_velocidad: int):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_actual + incremento_velocidad
        else:
        
            self.cantidad_multas = self.cantidad_multas + 1
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")
            print(f"Se ha generado una multa. Multas acumuladas: {self.cantidad_multas}")

    def desacelerar(self, decremento_velocidad: int):
        if (self.velocidad_actual - decremento_velocidad) > 0:
            self.velocidad_actual = self.velocidad_actual - decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: int) -> float:
        if self.velocidad_actual == 0:
            print("El automóvil está detenido, no se puede calcular el tiempo.")
            return None
        return distancia / self.velocidad_actual

    def tiene_multas(self) -> bool:
        return self.cantidad_multas > 0

    def calcular_total_multas(self) -> int:
        return self.cantidad_multas * self.VALOR_MULTA

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible.value}")
        print(f"Tipo de automóvil = {self.tipo_automovil.value}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Color = {self.color.value}")
        print(f"Es automático = {self.es_automatico}")


def main():
    auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO,
                      5, 6, 250, TipoColor.NEGRO, True)
    auto1.imprimir()
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual = {auto1.velocidad_actual}")
    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.velocidad_actual}")
    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.velocidad_actual}")
    auto1.frenar()
    print(f"Velocidad actual = {auto1.velocidad_actual}")
    auto1.desacelerar(20)

    print()
    print(f"¿Tiene multas? = {auto1.tiene_multas()}")
    auto1.set_velocidad_actual(200)
    auto1.acelerar(100)   
    auto1.acelerar(80)    
    print(f"¿Tiene multas? = {auto1.tiene_multas()}")
    print(f"Valor total de multas = ${auto1.calcular_total_multas()}")


if __name__ == "__main__":
    main()
