nomes = ['Maria', 'Pedro', 'João']
print(nomes, type(nomes))

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)

tamanho = len(nomes)
print(tamanho)

nomes.append('Marta Gomes')
print(nomes)

nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Lucia')
print(nomes)

nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

nomes.remove('Maria da Silva')
print(nomes)

del nomes[0]
print(nomes)

print(nomes)

print(nomes)

for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])