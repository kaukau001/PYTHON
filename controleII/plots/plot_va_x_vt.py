import matplotlib.pyplot as plt
from data.parser import parse_xlsx

x_axis, y_axis = parse_xlsx('Tensão', 'Tacômetro')

plt.plot(x_axis, y_axis, marker='o', linestyle='-')
plt.title('Gráfico de Linha')
plt.xlabel('Tensão de armadura [V]')
plt.ylabel('Tensão do tacômetro [V]')
plt.grid(True)
plt.show()
