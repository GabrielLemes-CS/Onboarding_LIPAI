class Pessoa:
    especie = "Humano"

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa("Ana Maria", "ana.maria@email.com")
pessoa2 = Pessoa("Carlos Silva", "carlos@gmail.com")

pessoa1.especie = "Mutante"
print("Pessoa 1 - Nome:", pessoa1.nome)
print("Pessoa 1 - Email:", pessoa1.email)
print("Pessoa 2 - Nome:", pessoa2.nome)
print("Pessoa 2 - Email:", pessoa2.email)