from models import (
    projeto, 
    aluno, 
    participacao)

# Funções para preencher listas de objetos a partir dos arquivos CSV
def preencher_alunos():
    alunos = []
    with open("alunos.csv", "r") as arquivo:
        for linha in arquivo:
            prontuario, nome, email = linha.strip().split(",")
            alunos.append(aluno(prontuario, nome, email))
    return alunos

def preencher_projetos():
    projetos = []
    with open("projetos.csv", "r") as arquivo:
        for linha in arquivo:
            codigo, titulo, responsavel = linha.strip().split(",")
            projetos.append(projeto(codigo, titulo, responsavel))
    return projetos

def preencher_participacoes(alunos, projetos):
    participacoes = []

    with open("participacoes.csv", "r") as arquivo:
        for linha in arquivo:
            codigo, data_inicio, data_fim, prontuario, cod_projeto = linha.strip().split(",")

            aluno_encontrado = None
            for a in alunos:
                if a.prontuario == prontuario:
                    aluno_encontrado = a
                    break

            projeto_encontrado = None
            for p in projetos:
                if p.codigo == int(cod_projeto):
                    projeto_encontrado = p
                    break

            if aluno_encontrado and projeto_encontrado:
                p = participacao(codigo, data_inicio, data_fim, aluno_encontrado, projeto_encontrado)

                participacoes.append(p)
            elif not aluno_encontrado:
                print(f"Aviso: Aluno com prontuario {prontuario} nao encontrado para a participacao {codigo}.")
            elif not projeto_encontrado:
                print(f"Aviso: Projeto com codigo {cod_projeto} nao encontrado para a participacao {codigo}.")

    return participacoes

def preencher_dados():
    alunos = preencher_alunos()
    projetos = preencher_projetos()
    participacoes = preencher_participacoes(alunos, projetos)

    for projeto in projetos:
        x = projeto.codigo
        for particao in participacoes:
            if particao.projeto.codigo == x:
                projeto.participacoes.append(particao)

    return alunos, projetos, participacoes

#################################################################################################
# Funções para cadastrar novos registros e verificar campos vazios
def campo_vazio(*campos):
    for c in campos:
        if c is None or str(c).strip() == "":
            return True
    return False

def cadastrar_projeto(projetos):
    cod_proj = input("Digite o codigo do projeto: ")
    cod_proj = validar_codigo_projeto(cod_proj, projetos)
    if(verificar_codigo_projeto(cod_proj, projetos)):
        return False
    titulo = input("Digite o titulo do projeto: ")
    responsavel = input("Digite o nome do responsavel pelo projeto: ")

    if campo_vazio(cod_proj, titulo, responsavel):
        print("Erro: nenhum campo pode estar vazio.")
        return False
    
    with open("projetos.csv", "a") as arquivo:
        arquivo.write(f"{cod_proj},{titulo},{responsavel}\n")
        projetos.append(projeto(cod_proj, titulo, responsavel))
        return True
    return False

def cadastrar_participacao(participacoes,alunos,projetos):
    cod_part = input("Digite o código da participação: ")
    cod_part = validar_codigo_participacao(cod_part, participacoes)
    if(verificar_codigo_participacao(cod_part, participacoes)):
        return False
    data_inicio = input("Digite a data de inicio da participacao (DD/MM/AAAA): ")
    data_inicio = validar_data(data_inicio)
    data_fim = input("Digite a data de fim da participacao (DD/MM/AAAA): ")
    data_fim = validar_data(data_fim)
    prontuario = input("Digite o prontuario do aluno: ")
    temp_cod_projeto = input("Digite o codigo do projeto: ")

    aluno_encontrado = None
    for a in alunos:
        if a.prontuario == prontuario:
            aluno_encontrado = a
            break
    
    projeto_encontrado = None
    for p in projetos:
        if p.codigo == int(temp_cod_projeto):
            projeto_encontrado = p
            break
    
    if aluno_encontrado is None:
        print(f"Erro: Aluno com prontuario {prontuario} nao encontrado.")
        return False
    if projeto_encontrado is None:
        print(f"Erro: Projeto com codigo {temp_cod_projeto} nao encontrado.")
        return False

    if campo_vazio(cod_part, data_inicio, data_fim, prontuario, temp_cod_projeto):
        print("Erro: nenhum campo pode estar vazio.")
        return False
    
    participacoes.append(participacao(cod_part, data_inicio, data_fim, aluno_encontrado, projeto_encontrado))
    for projeto in projetos:
        if projeto.codigo == temp_cod_projeto:
            projeto.participacoes.append(participacoes[-1])
            break

    with open("participacoes.csv", "a") as arquivo:
        arquivo.write(f"{cod_part},{data_inicio},{data_fim},{prontuario},{temp_cod_projeto}\n")
        return True
    return False


def cadastrar_aluno(alunos):
    prontuario = input("Digite o prontuario do aluno: ")
    prontuario = validar_prontuario(prontuario, alunos)
    if(verificador_prontuario(prontuario, alunos)):
        return False
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    email = validar_email(email)

    if campo_vazio(prontuario, nome, email):
        print("Erro: nenhum campo pode estar vazio.")
        return False

    with open("alunos.csv", "a") as arquivo:
        arquivo.write(f"{prontuario},{nome},{email}\n")
        alunos.append(aluno(prontuario, nome, email))
        return True
    return False


#################################################################################################
# Funções para listar registros
def listar_projetos(projetos):
    print("=== Lista de Projetos ===")
    cont = 0
    for projeto in projetos:
        print(f"Codigo: {projeto.codigo}, Titulo: {projeto.titulo}, Responsavel: {projeto.responsavel}")
        cont += 1

    if cont == 0:
        return True
    return False

def listar_alunos(alunos):
    print("=== Lista de Alunos ===")
    cont = 0
    for aluno in alunos:
        print(f"Prontuario: {aluno.prontuario}, Nome: {aluno.nome}, Email: {aluno.email}")
        cont += 1
    
    if cont == 0:
        return True
    return False

#################################################################################################
# Funções de busca
def buscar_aluno(prontuario,alunos):
    for aluno in alunos:
        if aluno.prontuario == prontuario:
            return aluno
    return None

def buscar_projeto(codigo,projetos):
    for projeto in projetos:
        if projeto.codigo == codigo:
            return projeto
    return None

def buscar_participacao_aluno(participacoes, prontuario):
    cont = 0
    for participacao in participacoes:
        if participacao.aluno.prontuario == prontuario:
            print(f"O aluno {participacao.aluno.prontuario} de prontuario {prontuario}  esta ou estava participando do projeto {participacao.projeto.titulo}")
            cont += 1
    if cont == 0:
        return False
    return True 

def buscar_participacao_projeto(participacoes, codigo):
    cont = 0
    for participacao in participacoes:
        if participacao.projeto.codigo == codigo:
            print(f"O projeto {participacao.projeto.titulo} de codigo {codigo} tem ou teve o aluno {participacao.aluno.nome} de prontuario {participacao.aluno.prontuario} participando dele")
            cont += 1
    if cont == 0:
        return False  
    return True

##################################################################################################
#funções de validação e verificação de dados
def validar_data(data):
    dia  = data[0:2]
    mes  = data[3:5]
    ano  = data[6:10] 
    if(len(data) != 10 or not data[0:2].isdigit() or not 
       data[3:5].isdigit() or not data[6:10].isdigit() or 
       data[2] != '/' or data[5] != '/' or dia < '01' or dia > '31' or 
       mes < '01' or mes > '12' or ano < '1900' or ano > '2100'):
        print("Data em formato invalido.")
        temp_data = input("Digite a data novamente (DD/MM/AAAA): ")
        return validar_data(temp_data)
    return data

def validar_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Email em formato invalido.")
        temp_email = input("Digite o email novamente: ")
        return validar_email(temp_email)
    return email

def verificador_prontuario(prontuario, alunos):
    for aluno in alunos:
        if aluno.prontuario == prontuario:
            print("Prontuario ja cadastrado.")
            return True 
    return False

def validar_prontuario(prontuario, alunos):
    if len(prontuario) != 5:
        print("Prontuario invalido.")
        temp_prontuario = input("Digite o prontuario novamente: ")
        return validar_prontuario(temp_prontuario, alunos)
    return prontuario
    
def verificar_codigo_projeto(codigo, projetos):
    for projeto in projetos:
        if projeto.codigo == codigo:
            print("Codigo ja cadastrado.")
            return True
    return False

def validar_codigo_projeto(codigo,projetos):
    if not str(codigo).isdigit() or int(codigo) < 1:
        print("Codigo invalido.") 
        temp_codigo = input("Digite o codigo novamente: ")
        return int(validar_codigo_projeto(temp_codigo, projetos))
    return int(codigo)

def verificar_codigo_participacao(codigo, participacoes):
    for participacao in participacoes:
        if participacao.codigo == codigo:
            print("Codigo ja cadastrado.")
            return True
    return False

def validar_codigo_participacao(codigo, participacoes):
    if not str(codigo).isdigit() or int(codigo) < 1:
        print("Codigo invalido.")
        temp_codigo = input("Digite o codigo novamente: ")
        return validar_codigo_participacao(temp_codigo, participacoes)
    return int(codigo)
  