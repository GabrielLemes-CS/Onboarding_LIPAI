class Projeto:
    def __init__(self,linha):
        if not linha or linha.strip() == "":
            raise ValueError("Linha não pode ser vazia")

        partes = linha.strip().split(",")

        if len(partes) != 3:
            raise ValueError("Formato inválido.")

        self.codigo = int(partes[0])
        self.titulo = partes[1]
        self.responsavel = partes[2]

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        if valor is None:
            raise ValueError("Código não pode ser vazio")
        self._codigo = int(valor)
    
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Título não pode ser vazio")
        self._titulo = valor
    
    @property
    def responsavel(self):
        return self._responsavel
    @responsavel.setter
    def responsavel(self, valor):
        if not valor:
            raise ValueError("Responsável não pode ser vazio")
        self._responsavel = valor

    def __eq__(self, other):
        if not isinstance(other, Projeto):
            return  False
        return self._codigo == other._codigo
    
