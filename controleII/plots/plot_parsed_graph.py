import matplotlib.pyplot as plt
import numpy as np
from data.parser import parse_csv

x_axis, y_ch1_axis, y_ch2_axis = parse_csv()

plt.plot(x_axis, y_ch1_axis, linestyle='-', label='CH1')
plt.plot(x_axis, y_ch2_axis, linestyle='-', label='CH2')
plt.legend()


def format_coord(x, y):
    index = np.argmin(np.abs(x_axis - x))  # Encontrar o índice mais próximo
    return f'Índice={index}, Tempo={x:.2f} s, Tensão={y:.2f} V'


plt.gca().format_coord = format_coord
plt.title('Gráfico de Linha')
plt.xlabel('Tempo [s]')
plt.ylabel('Tensão [V]')
plt.grid(True)
plt.show()
