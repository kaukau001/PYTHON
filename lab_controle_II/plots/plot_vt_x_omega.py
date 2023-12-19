import matplotlib.pyplot as plt

from data.parser import DataParser
from utils.constants import XLSX_PATH, TACOMETER_VOLTAGE, ENGINE_SPEED

x_axis, y_axis = DataParser(XLSX_PATH).parse_xlsx(TACOMETER_VOLTAGE, ENGINE_SPEED)

plt.plot(x_axis, y_axis, marker='o', linestyle='-')
plt.title('Gráfico de Linha')
plt.xlabel('Tensão do tacômetro [V]')
plt.ylabel('Velocidade [RPM]')
plt.grid(True)
plt.show()
