import matplotlib.pyplot as plt
from data.parser import DataParser
from utils.constants import CSV_PATH

x_axis, y_ch1_axis, y_ch2_axis = DataParser(CSV_PATH).parse_csv()

plt.plot(x_axis, y_ch1_axis, linestyle='-', label='Degrau')
plt.plot(x_axis, y_ch2_axis, linestyle='-', label='Motor')
plt.legend()

plt.title('Gráfico do motor com resposta ao degrau')
plt.xlabel('Tempo [s]')
plt.ylabel('Tensão [V]')
plt.grid(True)
plt.show()
