retangulo1 = {
    "largura": 10,
    "altura": 5
}

retangulo2 = {
    "largura": 20,
    "altura": 15
}

def calcular_area(retangulo):
    return retangulo["largura"] * retangulo["altura"]
def calcular_perimetro(retangulo):
    return 2 * (retangulo["largura"] + retangulo["altura"])

print("Retângulo 1 - Área:", calcular_area(retangulo1))
print("Retângulo 1 - Perímetro:", calcular_perimetro(retangulo1))
print("Retângulo 2 - Área:", calcular_area(retangulo2))
print("Retângulo 2 - Perímetro:", calcular_perimetro(retangulo2))

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        self._largura = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    

print(Retangulo.calcular_area(30, 10))
retangulo3 = Retangulo.from_string("30.0, 10.0")
print("Retângulo 3 - Área:", retangulo3.calcular_area())

retangulo1 = Retangulo(10, 5)

retangulo1.base = 0.0
