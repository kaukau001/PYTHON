import matplotlib.pyplot as plt
from data.parser import DataParser
from utils.constants import XLSX_PATH

x_axis, y_axis = DataParser(XLSX_PATH).parse_xlsx('Tensão', 'Tacômetro')
print(x_axis)
print('')
print(y_axis)
plt.plot(x_axis, y_axis, marker='o', linestyle='-')
plt.title('Gráfico de Linha')
plt.xlabel('Tensão de armadura [V]')
plt.ylabel('Tensão do tacômetro [V]')
plt.grid(True)
plt.show()
