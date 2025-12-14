valor = input("Digite o ID: ")
if len(valor) != 7:
    print("ID inválido")
elif not(valor[0] == 'B' and valor[1] == 'R'):
    print("ID inválido")
elif not(valor[2:6].isdigit()):
    print("ID inválido")
elif not(valor[6] == 'X'):
    print("ID inválido")
else:
    print("ID válido")