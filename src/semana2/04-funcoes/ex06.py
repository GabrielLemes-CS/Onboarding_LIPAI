def calcular_volume(aquario):
    comprimento = aquario['comprimento']
    altura = aquario['altura']
    largura = aquario['largura']
    return (comprimento * altura * largura) / 1000


def calcular_potencia_termostato(volume, aquario):
    temp_desejada = aquario['temperatura_desejada']
    temp_ambiente = aquario['temperatura_ambiente']
    return volume * 0.05 * (temp_desejada - temp_ambiente)


def calcular_filtragem(volume):
    filtragem_min = volume * 2
    filtragem_max = volume * 3
    return filtragem_min, filtragem_max

comprimento = float(input("Comprimento do aquário (cm): "))
altura = float(input("Altura do aquário (cm): "))
largura = float(input("Largura do aquário (cm): "))
temp_desejada = float(input("Temperatura desejada (°C): "))
temp_ambiente = float(input("Temperatura ambiente (°C): "))

aquario = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura,
    'temperatura_desejada': temp_desejada,
    'temperatura_ambiente': temp_ambiente
}

volume = calcular_volume(aquario)
potencia = calcular_potencia_termostato(volume, aquario)
filtragem_min, filtragem_max = calcular_filtragem(volume)

print("Volume do aquário: " + str(volume) )
print("Potência do termostato necessária: " + str(potencia))
print("Filtragem recomendada: " + str(filtragem_min) +" a " +  str(filtragem_max))

#ex02 pois o fato de poder manipular os valores da saida função nos permite fazer mais coisas com eles, como formatar a saída, reutilizar os valores em outros cálculos, entre outros.
#ex03/ex04 pois a possibilidade de receber uma quantidade variável de argumentos torna as funções mais flexíveis e adaptáveis a diferentes situações.
#Prefiro usar tupla como parâmetro quando os valores já estão organizados em uma coleção e quero deixar claro que a função trabalha sobre esse conjunto. Já sobre o uso de *args prefiro quando a função precisa ser flexível, já que ela é mais reitulizavel e facil de usar.