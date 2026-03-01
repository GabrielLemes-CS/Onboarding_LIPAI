import pandas as pd

data = pd.read_csv("classification_results_trial_0001.csv")
benign = 0
malignant = 0
acerto = 0
erro = 0
soma_erro = 0
############### ex01 ###############
for tipo in data.real_class:
    if tipo == "benign":
        benign += 1
    else:
        malignant += 1
print(f"Benign: {benign}, Malignant: {malignant}")

################ ex02 ###############
temp = data[data.predicted_class == data.real_class]
for i in temp.index:
    acerto += 1
erro = len(data) - acerto
print(f"Acertos: {acerto}, Erros: {erro}")

################ ex03 ###############
temp = data[data.predicted_class != data.real_class]
conf_erro = (
    temp["prob_benign"] * (temp["predicted_class"] == "benign") +
    temp["prob_malign"] * (temp["predicted_class"] == "malign")
)

if((conf_erro.sum()/len(temp)) > 0.5):
    print("O estava confiante em suas previsões erradas")
else:
    print("O modelo não estava confiante em suas previsões erradas")

############### ex04 ###############
temp1 = data[(data.real_class == data.predicted_class) & (data.real_class == "benign")]
print(f"Quantidade de TP: {len(temp1)}")
temp2 = data[(data.real_class == data.predicted_class) & (data.real_class == "malign")]
print(f"Quantidade de TN: {len(temp2)}")
temp3 = data[(data.real_class != data.predicted_class) & (data.real_class == "benign")]
print(f"Quantidade de FP: {len(temp3)}")
temp4 = data[(data.real_class != data.predicted_class) & (data.real_class == "malign")]
print(f"Quantidade de FN: {len(temp4)}")

############### ex05 ###############
acuracia = (len(temp1) + len(temp2)) / ( len(temp1) + len(temp2) + len(temp3) + len(temp4))
print(f"Acurácia: {acuracia}")
precisao = len(temp1) / (len(temp1) + len(temp3))
print(f"Precisão: {precisao}")
recall = len(temp1) / (len(temp1) + len(temp4))
print(f"Recall: {recall}")
especificidade = len(temp2) / (len(temp2) + len(temp3))
print(f"Especificidade: {especificidade}")
############### ex06 ###############
minimo = data[data.real_class == "benign"].sort_values(by="prob_benign", ascending=True).head(5)
print(f"Valor mínimo de prob_benign: {minimo}")
#Os falso positivos erraram com uma confiança alta, o que é preocupante, pois o modelo estava confiante em suas previsões errradas.

############## ex07 ###############
maximo = data[data.real_class == "benign"].sort_values(by="prob_benign", ascending=False).head(5)
print(f"Valor máximo de prob_benign: {maximo}")
#Quando o valor de prob_benign é alto, o modelo acerta mais, o que é esperado, pois o modelo está mais confiante em suas previsões corretas.