from ex01 import Aluno
from ex02 import Projeto


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError("Código da participação não pode ser vazio")
        self._codigo = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if not valor:
            raise ValueError("Data de início não pode ser vazia")
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if not valor:
            raise ValueError("Data de fim não pode ser vazia")
        self._data_fim = valor

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        if not isinstance(valor, Aluno):
            raise ValueError("Aluno deve ser um objeto da classe Aluno")
        self._aluno = valor

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, valor):
        if not isinstance(valor, Projeto):
            raise ValueError("Projeto deve ser um objeto da classe Projeto")
        self._projeto = valor
