#arquivo = open("src/06-arquivos/test.txt", "x")

#print(arquivo.readable())
#print(arquivo.read())
#lista = arquivo.readlines()
#print(lista[3])

#arquivo.write("\nLinha adicionada pelo Python")
#arquivo.write("\nOutra linha adicionada pelo Python")

#arquivo.close()

import os
#os.remove("src/06-arquivos/test3.txt")

if os.path.exists("src/06-arquivos/test2.txt"):
    os.remove("src/06-arquivos/test2.txt")
else:
    print("O arquivo não existe")


os.rmdir("src/06-arquivos/pasta_teste")

