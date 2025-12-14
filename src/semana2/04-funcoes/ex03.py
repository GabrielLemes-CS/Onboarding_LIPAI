def soma(numeros):
    return sum(numeros)

inputs = tuple(map(float, input("Digite números separados por espaço: ").split()))
print("A soma dos números é:", soma(inputs))