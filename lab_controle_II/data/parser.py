import pandas as pd
import os

from utils.exceptions import InvalidExtensionError


class DataParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def _check_file_exists(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"O arquivo {self.file_path} não foi encontrado.")

    def _check_file_extension(self):
        try:
            file_name, file_extension = os.path.splitext(self.file_path)
            if file_extension not in ['.xlsx', '.csv']:
                raise InvalidExtensionError()
            return file_extension
        except InvalidExtensionError as e:
            print(e.message)

    def parse_csv(self) -> tuple:
        try:
            self._check_file_exists()
            file_extension = self._check_file_extension()

            if file_extension != '.csv':
                raise InvalidExtensionError('O arquivo não possui extensão .csv')

            data = pd.read_csv(self.file_path)

            if data.empty:
                raise ValueError(f"O arquivo {self.file_path} está vazio.")

            index_x = 0
            index_y_ch1 = 1
            index_y_ch2 = 2

            x_axis = data.iloc[:, index_x]
            y_ch1_axis = data.iloc[:, index_y_ch1]
            y_ch2_axis = data.iloc[:, index_y_ch2]

            linearized_x_axis = x_axis - x_axis.iloc[0]
            linearized_y_ch1_axis = y_ch1_axis - y_ch1_axis.iloc[0]
            linearized_y_ch2_axis = y_ch2_axis - y_ch2_axis.iloc[0]

            return linearized_x_axis, linearized_y_ch1_axis, linearized_y_ch2_axis
        except InvalidExtensionError as e:
            print(e.message)
        except ValueError as e:
            print(e)

    def parse_xlsx(self, x_column: list,
                   y_column: list,
                   z_column: list or None = None) -> tuple:
        try:
            self._check_file_exists()
            file_extension = self._check_file_extension()

            if file_extension != '.xlsx':
                raise InvalidExtensionError('O arquivo não possui extensão .xlsx')

            data = pd.read_excel(self.file_path)
            if data.empty:
                raise ValueError(f"O arquivo {self.file_path} está vazio.")

            if (x_column not in data.columns
                    or y_column not in data.columns
                    or (z_column not in data.columns and z_column is not None)):
                raise ValueError("As colunas especificadas não existem no conjunto de dados.")

            x_axis = data[x_column]
            y_axis = data[y_column]

            linearized_x = x_axis - x_axis.iloc[0]
            linearized_y = y_axis - y_axis.iloc[0]

            if z_column:
                z_axis = data[z_column]
                linearized_z = z_axis - z_axis.iloc[0]
                return linearized_x, linearized_y, linearized_z

            return linearized_x, linearized_y
        except InvalidExtensionError as e:
            print(e.message)
        except ValueError as e:
            print(e)
