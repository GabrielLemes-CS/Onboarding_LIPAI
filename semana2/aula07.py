print('hello world','this is aula07',1,True,sep=' - ', end='!!!\n')

arquivo = open('nome.txt', 'w', encoding='utf-8')

print('joao@gmail.com', file=arquivo, sep = ';')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(type(nome), type(idade))

arquivo.close()

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

arquivo_nots = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_nots.read()
notas = conteudo.split(';')
media = (float(notas[0]) + float(notas[1]) + float(notas[2])) / len(notas)
print('Média das notas:', media)
arquivo_nots.close()