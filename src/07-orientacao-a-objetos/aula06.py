nome1 = 'Gabriel'
nome2 = 'Gabriel'

print(nome1 == nome2)

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __eq__(self, other):
        return self.nome == other.nome and self.cpf == other.cpf

    def __hash__(self):
        return hash(self.nome) 
    
    def __repr__(self):
        return f'Pessoa(nome={self.nome}, cpf={self.cpf})'
    
pessoa1 = Pessoa("Gabriel", "12345678901")
pessoa2 = Pessoa("Gabriel", "12345678901")

pessoa_list = [pessoa1, pessoa2] 
print(pessoa_list)
   
