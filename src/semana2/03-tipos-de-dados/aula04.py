carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
print(carro, type(carro))

print(carro["marca"])
print(carro.get("marca"))

print(carro.keys())
print(carro.values())
print(carro.items())

print("cor" in carro)

carro["cor"] = 'Azul'
print("cor" in carro)
print(carro, type(carro))

marca = carro.pop("marca")
print(marca)
print(carro)

for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

print(carro.items())

for key, value in carro.items():
    print(key, value)

aluno1 = {
    'nome': 'João',
    'email': 'joao@email.com',
    'notas': [10.0, 5.3, 7.0]
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@email.com',
    'notas': [10.0, 2.3, 10.0]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)