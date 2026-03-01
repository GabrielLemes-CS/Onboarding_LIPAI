import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("metrics.csv")
temp = np.arange(1, len(data)+1)

fig, ax = plt.subplots(2,1, figsize=(10, 10))

ax[0].plot(temp, data.train_acc, label="accuracy")
ax[0].plot(temp, data.val_acc, label="val_accuracy")
ax[0].set_title("Accuracy por Epoch")
ax[0].set_xlabel("Epoch")
ax[0].set_ylabel("Accuracy")
ax[0].legend()

ax[1].plot(temp, data.train_loss, label="loss", color="red")
ax[1].plot(temp, data.val_loss, label="val_loss", color="orange")
ax[1].set_title("Loss por Epoch")
ax[1].set_xlabel("Epoch")
ax[1].set_ylabel("Loss")
ax[1].legend()

plt.tight_layout()
plt.show()
