nome = "joão"
Idade = 22
print("Nome:{nome} /n Idade:{Idade}".format(nome=nome, Idade=Idade))

print(nome[2])
print(nome[-1])

print(len(nome))
print(nome.upper())

print(nome.capitalize())
print(nome.replace("j", "J"))

frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas)
print(frutas[1])
frutas.append("abacaxi")
frutas.remove("banana")
print(frutas)

Frutas = ("maçã", "banana", "laranja", "uva")
print(len(Frutas))

funcionarios = [
    {
        "nome": "Ana",
        "idade": 28,
        "cargo": "Analista"
    },
    {
        "nome": "Marcos",
        "idade": 25,
        "cargo": "Rei" 
    }
]
print(funcionarios[1])
print(funcionarios[1]["nome"])
funcionarios[1]["salario"] = 50000
print(funcionarios[1])   