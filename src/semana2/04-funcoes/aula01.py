print('Olá', 123, True)

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

def saudacoes():
    print('Olá')

saudacoes()
saudacoes()
saudacoes()

def saudacoes(nome):
    print(f'Olá {nome}')

saudacoes('Maria')
saudacoes('Pedro')
nome = 'Carlos'
saudacoes(nome)

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)

calcular_media(10.0, 3.0, 6.0)

n1 = 10.0
n2 = 3.0
n3 = 8.0

calcular_media(n1, n2, n3)

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


media = calcular_media(10.0, 8.4, 3.2)
print('valor da média', media)
