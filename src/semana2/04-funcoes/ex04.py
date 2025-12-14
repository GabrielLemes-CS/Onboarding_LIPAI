def soma(*args):
    return sum(args)

inputs = list(map(float, input("Digite números separados por espaço: ").split()))
print("A soma dos números é:", soma(*inputs))