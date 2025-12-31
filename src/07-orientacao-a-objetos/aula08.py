class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - (0.10 * self.salario)

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento()
        return pagamento_salario + self.bonus


cliente = Cliente("Jose", "Augusto", "123.456.789-00")
print(cliente.obtem_nome_completo())

funcionario = Funcionario("Joao", "Silva", "111.222.333-44", 5000)
print(funcionario.calcula_pagamento()) 

programador = Programador("Maria", "Souza", "555.666.777-88", 5000, 200)
print(programador.calcula_pagamento()) 