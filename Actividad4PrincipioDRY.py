class Geometria:
    def area(self, *lados):
        if len(lados) == 1:
            return lados[0] ** 2
        elif len(lados) == 2:
            return lados[0] * lados[1]
        else:
            raise ValueError("Número incorrecto de lados")

    def perimetro(self, *lados):
        if len(lados) == 1:
            return 4 * lados[0]
        elif len(lados) == 2:
            return 2 * (lados[0] + lados[1])
        else:
            raise ValueError("Número incorrecto de lados")

def main():
    geom = Geometria()

    # Solicitar al usuario que elija entre cuadrado o rectángulo
    print("Seleccione la figura: ")
    print("1. Cuadrado")
    print("2. Rectángulo")
    opcion = int(input("Opción: "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"Área del cuadrado: {geom.area(lado)}")
        print(f"Perímetro del cuadrado: {geom.perimetro(lado)}")
    elif opcion == 2:
        lado1 = float(input("Ingrese el primer lado del rectángulo: "))
        lado2 = float(input("Ingrese el segundo lado del rectángulo: "))
        print(f"Área del rectángulo: {geom.area(lado1, lado2)}")
        print(f"Perímetro del rectángulo: {geom.perimetro(lado1, lado2)}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()