class Geometria:
    def area_cuadrado(self, lado):
        return lado * lado
    def area_rectangulo(self, ancho, alto):
        return ancho * alto
    def perimetro_cuadrado(self, lado):
        return 4 * lado
    def perimetro_rectangulo(self, ancho, alto):
        return 2 * (ancho + alto)

def main():
    geom = Geometria()

    # Solicitar al usuario que elija entre cuadrado o rectángulo
    print("Seleccione la figura: ")
    print("1. Cuadrado")
    print("2. Rectángulo")
    opcion = int(input("Opción: "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"Área del cuadrado: {geom.area_cuadrado(lado)}")
        print(f"Perímetro del cuadrado: {geom.perimetro_cuadrado(lado)}")
    elif opcion == 2:
        lado1 = float(input("Ingrese el primer lado del rectángulo: "))
        lado2 = float(input("Ingrese el segundo lado del rectángulo: "))
        print(f"Área del rectángulo: {geom.area_rectangulo(lado1, lado2)}")
        print(f"Perímetro del rectángulo: {geom.perimetro_rectangulo(lado1, lado2)}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()