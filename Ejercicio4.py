"""
Ejercicio No. 4
A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele
a Juan su edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la
edad de Juan y mi edad es la suma de las tres. Hacer un algoritmo que
muestre la edad de los cuatro.
"""

class Edades:

    def calcular_edalber(edjuan: float) -> float:
        return 2 * edjuan / 3

    def calcular_edana(edjuan: float) -> float:
        return 4 * edjuan / 3

    def calcular_edmama(edjuan: float, edalber: float, edana: float) -> float:
        return edjuan + edalber + edana

def main():
    edjuan = float(input("How old is Juan? "))

    edalber = Edades.calcular_edalber(edjuan)
    edana = Edades.calcular_edana(edjuan)
    edmama = Edades.calcular_edmama(edjuan, edalber, edana)

    print(f"la edad de la mama es: {edmama}")
    print(f"la edad de juan es: {edjuan}")
    print(f"la edad de alber es: {edalber}")
    print(f"la edad de ana es: {edana}")


if __name__ == "__main__":
    main()
