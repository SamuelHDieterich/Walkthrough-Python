# GRÁFICO DA FUNÇÃO SENO

# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Valores de x e y para o gráfico
x = np.linspace(-5, 5, 100) # Array com 100 valores indo de -5 até 5
y = np.sin(x)               # Array com os valores da função seno em 'x'

plt.plot(x, y)  # Gera o gráfico de linha
plt.show()      # Mostra o gráfico produzido