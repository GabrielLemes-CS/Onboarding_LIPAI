erros = []
valor = input("Digite o ID: ")
if len(valor) != 7:
    erros.append("O identificador não tem 7 caracteres.")
if not(valor[0] == 'B' and valor[1] == 'R'):
    erros.append("O identificador não inicia com a sequência BR.")
if not(valor[2:6].isdigit()):
    erros.append("O identificador não apresenta número inteiro entre 0001 e 9999.")
if not(valor[6] == 'X'):
    erros.append("O identificador não finaliza com o caractere X.")
if len(erros) == 0:
    print("ID válido")

print(erros)
