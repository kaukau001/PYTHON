import matplotlib.pyplot as plt
from data.parser import DataParser
from utils.constants import XLSX_PATH, ARMOR_VOLTAGE, TACOMETER_VOLTAGE

x_axis, y_axis = DataParser(XLSX_PATH).parse_xlsx(ARMOR_VOLTAGE, TACOMETER_VOLTAGE)

plt.plot(x_axis, y_axis, marker='o', linestyle='-')
plt.title('Gráfico de Linha')
plt.xlabel('Tensão de armadura [V]')
plt.ylabel('Tensão do tacômetro [V]')
plt.grid(True)
plt.show()
