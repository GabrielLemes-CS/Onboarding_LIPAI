def linha_para_dict(linha, chaves):
    valores = linha.strip().split(",")
    dicionario = {}
    for valor, chave in zip(valores, chaves):
        dicionario[chave] = valor
    return dicionario

print(linha_para_dict("001,João Silva,Desenvolvedor", ["codigo", "nome", "profissao"]))