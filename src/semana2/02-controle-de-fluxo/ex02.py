<<<<<<< HEAD
entrada = input("Digite as notas separadas por vírgula: ")
notas = [float(x) for x in entrada.split(',')]
media = sum(notas) / len(notas)

if media > 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
=======
entrada = input("Digite as notas separadas por vírgula: ")
notas = [float(x) for x in entrada.split(',')]
media = sum(notas) / len(notas)

if media > 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
>>>>>>> c89ca16 (Reorganização do projeto)
