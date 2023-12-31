import tkinter as tk
import pandas as pd
from pandas import DataFrame
import subprocess
from utils.constants import XLSX_PATH, ARMOR_VOLTAGE, TACOMETER_VOLTAGE, CSV_PATH, ENGINE_SPEED
from data.parser import DataParser
from plots.plotter import Plotter
from utils.logger import AppLogger
from tkinter import scrolledtext
from tkinter import ttk


class DataAnalysisInterface:
    def __init__(self,
                 window,
                 plotter: Plotter,
                 logger: AppLogger.get_logger):

        style = tk.ttk.Style()
        style.configure("TButton", padding=(10, 5, 10, 5), font='Helvetica 10 bold', background='#ccc')

        self.window = window
        self.plotter = plotter
        self.logger = logger

        self.window.title("Interface para Processar e Plotar Arquivos")
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))

        self.label_xlsx = tk.Label(self.window, text="Dados do experimento:")
        self.label_xlsx.grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)

        self.entry_xlsx = tk.Entry(self.window, width=50)
        self.entry_xlsx.grid(row=0, column=1, columnspan=3, pady=5, padx=5)

        self.label_csv = tk.Label(self.window, text="Dados do osciloscópio:")
        self.label_csv.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)

        self.entry_csv = tk.Entry(self.window, width=50)
        self.entry_csv.grid(row=1, column=1, columnspan=3, pady=5, padx=5)

        self.process_button = tk.Button(self.window, text="Processar Arquivos", command=self.process_files)
        self.process_button.grid(row=2, column=0, columnspan=4, pady=10, padx=5)

        self.plot_linear_region_button = tk.Button(self.window, text="Plotar Região Linear",
                                                   command=self.plotter.plot_linear_region)
        self.plot_linear_region_button.grid(row=3, column=0, columnspan=4, pady=5, padx=5)

        self.plot_motor_response_button = tk.Button(self.window, text="Plotar Resposta do Motor",
                                                    command=self.plotter.plot_motor_response)
        self.plot_motor_response_button.grid(row=4, column=0, columnspan=4, pady=5, padx=5)

        self.plot_armature_tachometer_button = tk.Button(self.window, text="Plotar Va x Vt",
                                                         command=self.plotter.plot_armature_tachometer)
        self.plot_armature_tachometer_button.grid(row=5, column=0, columnspan=4, pady=5, padx=5)

        self.plot_tachometer_speed_button = tk.Button(self.window, text="Plotar Vt x ω",
                                                      command=self.plotter.plot_tachometer_speed)
        self.plot_tachometer_speed_button.grid(row=6, column=0, columnspan=4, pady=5, padx=5)

        self.generate_report_button = tk.Button(self.window, text="Gerar Relatório", command=self.generate_report)
        self.generate_report_button.grid(row=7, column=0, columnspan=4, pady=10, padx=5)

        self.log_text = scrolledtext.ScrolledText(self.window, width=80, height=15, wrap=tk.WORD)
        self.log_text.grid(row=8, column=0, columnspan=4, pady=10, padx=5)

        self.default_path_xlsx = XLSX_PATH
        self.default_path_csv = CSV_PATH

        self.entry_xlsx.insert(0, self.default_path_xlsx)
        self.entry_csv.insert(0, self.default_path_csv)

    def process_files(self):
        try:
            path_xlsx = self.entry_xlsx.get() or self.default_path_xlsx
            path_csv = self.entry_csv.get() or self.default_path_csv

            data_parser_xlsx = DataParser(file_path=path_xlsx, logger=logger)
            data_parser_csv = DataParser(file_path=path_csv, logger=logger)

            armor, tachometer, engine_speed = data_parser_xlsx.parse_xlsx(x_column=ARMOR_VOLTAGE,
                                                                          y_column=TACOMETER_VOLTAGE,
                                                                          z_column=ENGINE_SPEED)
            x_axis, y_chanel_one_axis, y_chanel_two_axis = data_parser_csv.parse_csv()

            df_xlsx = pd.DataFrame({
                'Armor Voltage': armor,
                'Tachometer Voltage': tachometer,
                'Engine Speed': engine_speed
            })
            df_csv = pd.DataFrame({
                'Time': x_axis,
                'Chanel 1': y_chanel_one_axis,
                'Chanel 2': y_chanel_two_axis
            })

            self.show_data(df_xlsx, "Dados do Experimento")
            self.show_data(df_csv, "Dados do Osciloscópio")

        except Exception as e:
            AppLogger().get_logger().error(f"Erro ao processar arquivos: {e}")

    def show_data(self, dataframe: DataFrame, title: str, logs: str = ""):
        data_window = tk.Toplevel(self.window)
        data_window.title(title)

        altura_window = min(500, len(dataframe) * 20)
        data_window.geometry(f"500x{altura_window}")

        texto_dados = tk.Text(data_window, height=len(dataframe), width=60)
        texto_dados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(data_window, command=texto_dados.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        texto_dados.config(yscrollcommand=scrollbar.set)

        texto_dados.insert(tk.END, dataframe.to_string(index=False))

        if logs:
            self.log_text.insert(tk.END, logs)

    def generate_report(self):
        try:
            self.log_text.delete('1.0', tk.END)

            result = subprocess.run(
                ["python", "C:\\Users\\kauan\\Documents\\GitHub\\PYTHON\\lab_controle_II\\rotine.py"],
                capture_output=True, text=True, encoding='utf-8')

            self.log_text.insert(tk.END, result.stdout)
            self.log_text.insert(tk.END, result.stderr)

        except Exception as e:
            self.logger.error(f"Erro ao gerar o relatório: {e}")


logger = AppLogger().get_logger()
plotter_instance = Plotter()

principal_window = tk.Tk()

principal_interface = DataAnalysisInterface(principal_window, plotter_instance, logger)

principal_window.mainloop()
