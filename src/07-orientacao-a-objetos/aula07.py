class endereco:
    def __init__(self,cep,numero):
        self.cep = cep
        self.numero = numero

    def str__(self):
        return f'Endereço(cep={self.cep}, numero={self.numero})'


class telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def str__(self):
        return f'Telefone(ddd={self.ddd}, numero={self.numero})'
class pessoa:
    def __init__(self, cpf,nome,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_endereco(self,endereco):
        self.enderecos.append(endereco)
    
    def str__(self):
        return f'Pessoa(nome={self.nome}, cpf={self.cpf}, telefone={self.telefone})'


pessoa1 = pessoa("12345678901","Gabriel",telefone("11","987654321"))
pessoa1.add_endereco(endereco("01234-567",100))

print(pessoa1)
print(pessoa1.telefone.ddd)
print(pessoa1.telefone.numero)
