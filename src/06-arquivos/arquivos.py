arq = open("arquivo_teste.txt", "w")

print(arq)
arq.write("Linha 1\n")
arq.writelines("Linha 2\n")

with open("arquivo_teste.txt", "a") as arq:
    arq.write("Linha 3\n")
    arq.write("Linha 4\n")

x = arq.read("arquivo_teste.txt")
print(x)