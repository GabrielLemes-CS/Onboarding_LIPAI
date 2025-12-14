<<<<<<< HEAD
for i in range(10):
    if i == 4:
        break
busca = 5
numeros = [1, 5, 9, 7, 3, 3, 2, 1, 7]
posicao = -1

contador = 0
for numero in numeros:
    print('Procurando na posicao:', contador)
    if numero == busca:
        posicao = contador
        break
    contador += 1

print(posicao)

print('-----')
for numero in numeros:
    if numero == 3:
        continue
=======
for i in range(10):
    if i == 4:
        break
busca = 5
numeros = [1, 5, 9, 7, 3, 3, 2, 1, 7]
posicao = -1

contador = 0
for numero in numeros:
    print('Procurando na posicao:', contador)
    if numero == busca:
        posicao = contador
        break
    contador += 1

print(posicao)

print('-----')
for numero in numeros:
    if numero == 3:
        continue
>>>>>>> c89ca16 (Reorganização do projeto)
    print(numero)