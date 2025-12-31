class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def __str__(self):
        return f"Retângulo(largura={self.largura}, altura={self.altura})"
    def __repr__(self):
        return f"Retangulo({self.largura}, {self.altura})"
    

retangulo1 = Retangulo(10, 5)
retangulo2 = Retangulo(20, 15)

print(retangulo1.__repr__())
retangulo1 = eval('Retangulo(10, 5)')

 
