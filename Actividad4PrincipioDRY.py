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