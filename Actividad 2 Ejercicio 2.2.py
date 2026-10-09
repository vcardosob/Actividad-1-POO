from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    UA_EN_KM = 149597870

    def __init__(self, nombre: str = None, cantidad_satelites: int = 0,
                 masa: float = 0, volumen: float = 0, diametro: int = 0,
                 distancia_sol: int = 0, tipo: TipoPlaneta = None,
                 es_observable: bool = False,
                 periodo_orbital: float = 0, periodo_rotacion: float = 0):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa                    
        self.volumen = volumen              
        self.diametro = diametro            
        self.distancia_sol = distancia_sol  
        self.tipo = tipo
        self.es_observable = es_observable
        self.periodo_orbital = periodo_orbital      
        self.periodo_rotacion = periodo_rotacion    

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")
        print(f"Periodo orbital (años) = {self.periodo_orbital}")
        print(f"Periodo de rotación (días) = {self.periodo_rotacion}")

    def calcular_densidad(self) -> float:
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        limite = self.UA_EN_KM * 3.4
        return self.distancia_sol > limite


def main():
    p1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000,
                 TipoPlaneta.TERRESTRE, True, 1.0, 0.997)
    p1.imprimir()
    print(f"Densidad del planeta = {p1.calcular_densidad()}")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
    print()

    p2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000,
                 TipoPlaneta.GASEOSO, True, 11.86, 0.413)
    p2.imprimir()
    print(f"Densidad del planeta = {p2.calcular_densidad()}")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}")


if __name__ == "__main__":
    main()
