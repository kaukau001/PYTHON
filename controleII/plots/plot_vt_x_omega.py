import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data.parser import parse_xlsx

x_axis, y_axis = parse_xlsx('Tacômetro', 'Rotação')


# Plotar o gráfico
plt.plot(x_axis, y_axis, marker='o', linestyle='-')
plt.title('Gráfico de Linha')
plt.xlabel('Tensão do tacômetro [V]')
plt.ylabel('Velocidade [RPM]')
plt.grid(True)
plt.show()
