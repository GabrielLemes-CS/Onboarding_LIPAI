class aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

class participacao:
    def __init__(self,codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = int(codigo)
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

class projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = int(codigo)
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []
          

