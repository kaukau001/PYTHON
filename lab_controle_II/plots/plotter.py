import numpy as np
import matplotlib.pyplot as plt
from data.parser import DataParser
from utils.constants import XLSX_PATH, ARMOR_VOLTAGE, TACOMETER_VOLTAGE, POLY_DEGREE, CSV_PATH, ENGINE_SPEED
from utils.logger import AppLogger


class Plotter:
    def __init__(self):
        self.logger = AppLogger().get_logger()

    def plot_linear_region(self):
        armor, tachometer = DataParser(XLSX_PATH, self.logger).parse_xlsx(ARMOR_VOLTAGE, TACOMETER_VOLTAGE)

        plt.figure('Linear Region')
        plt.plot(armor, tachometer, 'o', label='Dados Experimentais')

        mmq_adjust = np.polyfit(armor, tachometer, POLY_DEGREE)
        pol_adjust = np.polyval(mmq_adjust, armor)
        plt.plot(armor, pol_adjust, label='Ajuste Polinomial (7º Grau)')

        derivative_adjust = np.polyval(np.polyder(mmq_adjust), armor)
        derivative_adjust[0] = derivative_adjust[1]
        derivative_adjust[-1] = derivative_adjust[-2]
        plt.plot(armor, derivative_adjust, label='Derivada do Ajuste Polinomial')

        horizontal_line = np.mean(derivative_adjust[11:])
        plt.axhline(y=horizontal_line, color='r', linestyle='--', label='Média (a partir de 12º ponto)')

        self._set_plot_properties('Região Linear', 'Tensão de armadura [V]', 'Tensão do tacômetro [V]')

    def plot_motor_response(self):
        x_axis, y_ch1_axis, y_ch2_axis = DataParser(CSV_PATH, self.logger).parse_csv()
        plt.figure('Engine response')
        plt.plot(x_axis, y_ch1_axis, linestyle='-', label='Degrau')
        plt.plot(x_axis, y_ch2_axis, linestyle='-', label='Motor')
        plt.legend()

        self._set_plot_properties('Gráfico do motor com resposta ao degrau', 'Tempo [s]', 'Tensão [V]')

    def plot_armature_tachometer(self):
        plt.figure('armature voltage x tachometer voltage')
        x_axis, y_axis = DataParser(XLSX_PATH, self.logger).parse_xlsx(ARMOR_VOLTAGE, TACOMETER_VOLTAGE)

        plt.plot(x_axis, y_axis, marker='o', linestyle='-')
        self._set_plot_properties('Va x Vt', 'Tensão de armadura Va [V]', 'Tensão do tacômetro Vt [V]')

    def plot_tachometer_speed(self):
        plt.figure('tachometer voltage x engine speed')
        x_axis, y_axis = DataParser(XLSX_PATH, self.logger).parse_xlsx(TACOMETER_VOLTAGE, ENGINE_SPEED)

        plt.plot(x_axis, y_axis, marker='o', linestyle='-')
        self._set_plot_properties('Vt x ω', 'Tensão do tacômetro Vt [V]', 'Velocidade ω [RPM]')

    @staticmethod
    def _set_plot_properties(title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()


# Exemplo de uso
if __name__ == "__main__":
    plotter = Plotter()
    plotter.plot_armature_tachometer()
    plotter.plot_tachometer_speed()
    plotter.plot_linear_region()
    plotter.plot_motor_response()

