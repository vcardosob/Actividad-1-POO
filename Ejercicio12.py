class Salario:

    def calcular_salario_bruto(horas: float, valor_hora: float) -> float:
        return horas * valor_hora

    def calcular_retencion(salario_bruto: float, porcentaje: float = 12.5) -> float:
        return salario_bruto * porcentaje / 100

    def calcular_salario_neto(salario_bruto: float, retencion: float) -> float:
        return salario_bruto - retencion

def main():
    horas = float(input("Cuantas horas trabajo el empleado? "))
    valor_hora = float(input("Cual es el valor de la hora? "))

    salario_bruto = Salario.calcular_salario_bruto(horas, valor_hora)
    retencion = Salario.calcular_retencion(salario_bruto)
    salario_neto = Salario.calcular_salario_neto(salario_bruto, retencion)

    print(f"el salario bruto es: {salario_bruto}")
    print(f"la retencion en la fuente es: {retencion}")
    print(f"el salario neto es: {salario_neto}")

if __name__ == "__main__":
    main()
