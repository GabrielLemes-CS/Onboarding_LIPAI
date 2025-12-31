class Aluno:
    def __init__(self,linha):
        if not linha or linha.strip() == "":
            raise ValueError("Linha não pode ser vazia")

        partes = linha.strip().split(",")

        if len(partes) != 3:
            raise ValueError("Formato inválido.")

        self._prontuario = partes[0]
        self._nome = partes[1]
        self._email = partes[2]

    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, valor):
        if not valor:
            raise ValueError("Prontuário não pode ser vazio")
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if not valor:
            raise ValueError("Email não pode ser vazio")
        self._email = valor

    def __eq__(self, other):
        if not isinstance(other, Aluno):
            return  False
        return self._prontuario == other._prontuario
    
    def __hash__(self):
        return hash(self._prontuario)
    
    
