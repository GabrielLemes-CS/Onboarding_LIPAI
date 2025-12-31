def carregar_dados_alunos(nome_arquivo):
    with open(nome_arquivo, "r") as arq:
        linhas = arq.readlines()

    alunos = []
    for linha in linhas:
        prontuario, nome, email = linha.strip().split(",")
        aluno = {
            "prontuario": prontuario,
            "nome": nome,
            "email": email
        }
        alunos.append(aluno)
    
    tupla = tuple(alunos)
    return tupla

print(carregar_dados_alunos("C:/Users/gabri/OneDrive/Documentos/Onboarding_LIPAI/src/06-arquivos/teste2.txt"))