import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("classification_results_trial_0001.csv")

tamanho_malign = len(data[data["real_class"] == "malign"])
tamanho_benign = len(data[data["real_class"] == "benign"])
tamanho_predicted_malign = len(data[data["predicted_class"] == "malign"])
tamanho_predicted_benign = len(data[data["predicted_class"] == "benign"]) 
erro_benign = len(data[(data["real_class"] == "benign") & (data["predicted_class"] != "benign")])
erro_malign = len(data[(data["real_class"] == "malign") & (data["predicted_class"] != "malign")])
fig, ax = plt.subplots(2, 3, figsize=(15, 10))

ax[0,0].bar(["malign", "benign"], [tamanho_malign, tamanho_benign])
ax[0,0].set_title("Quantidade de amostras por classe")
ax[0,0].set_xlabel("Classe")
ax[0,0].set_ylabel("Quantidade de amostras")

ax[0,1].bar(
    ["predicted_malign", "predicted_benign"],
    [tamanho_predicted_malign, tamanho_predicted_benign]
)
ax[0,1].set_title("Quantidade de amostras por classe predita")
ax[0,1].set_xlabel("Classe")
ax[0,1].set_ylabel("Quantidade de amostras")

ax[0,2].hist(data.prob_benign, range=(0, 1), bins=5)
ax[0,2].set_title("Distribuição da probabilidade de benignidade")
ax[0,2].set_xlabel("Probabilidade de ser benigno")
ax[0,2].set_ylabel("Frequência")

ax[1,0].hist(data.prob_malign, range=(0, 1), bins=5)
ax[1,0].set_title("Distribuição da probabilidade de malignidade")
ax[1,0].set_xlabel("Probabilidade de ser maligno")
ax[1,0].set_ylabel("Frequência")

colors = np.where(data.real_class == data.predicted_class, "blue", "red")

ax[1,1].scatter(
    data.prob_benign,
    data.prob_malign,
    c=colors,
    cmap="viridis"
)
ax[1,1].set_title("Relação entre probabilidade de benignidade e malignidade")
ax[1,1].set_xlabel("Probabilidade de ser benigno")
ax[1,1].set_ylabel("Probabilidade de ser maligno")

ax[1,2].bar(["Erro benign", "Erro malign"], [erro_benign, erro_malign])
ax[1,2].set_title("Quantidade de erros por classe")
ax[1,2].set_xlabel("Tipo de erro")
ax[1,2].set_ylabel("Quantidade de erros")

plt.tight_layout()
plt.show()

#O pior erro é o falso negativo, pois ele pode atrasar o diagnostico e o tratamento de um paciente com câncer.