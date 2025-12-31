def calcular_imc(individuo):
    peso = individuo['peso']
    altura = individuo['altura']
    return peso / (altura * altura)


def obter_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    elif imc < 35:
        return "Obesidade de Classe 1"
    elif imc < 40:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"


def situacao_individuo(imc):
    if imc < 18.5:
        return "ganhar peso"
    elif imc < 25:
        return "normal"
    else:
        return "perder peso"


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

individuo = {
    'peso': peso,
    'altura': altura
}

imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print("\nIMC: " + str(imc))
print("Classificação: " + classificacao)
print("Situação atual: " + situacao)
