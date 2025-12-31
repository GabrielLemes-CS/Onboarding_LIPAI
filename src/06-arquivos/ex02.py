def carrega_dados_projeto(nome_arquivo):
    with open(nome_arquivo, "r") as arq:
        linhas = arq.readlines()

    projetos = []
    for linha in linhas:
        codigo, titulo, responsavel = linha.strip().split(",")
        projeto = {
            "codigo": codigo,
            "titulo": titulo,
            "responsavel": responsavel
        }
        projetos.append(projeto)
    return tuple(projetos)

print(carrega_dados_projeto("C:/Users/gabri/OneDrive/Documentos/Onboarding_LIPAI/src/06-arquivos/projetos.txt")) 
   