import pandas as pd
import os

path_parser = os.path.abspath(__file__)
folder_parser = os.path.dirname(path_parser)
csv_file_path = os.path.join(folder_parser, 'arquivo.csv')
xlsx_file_path = os.path.join(folder_parser, 'Dados.xlsx')


def parse_csv():
    file_path = csv_file_path
    data = pd.read_csv(file_path)

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


def parse_xlsx(x_column, y_column):
    file_path = xlsx_file_path
    data = pd.read_excel(file_path)

    if x_column not in data.columns or y_column not in data.columns:
        raise ValueError("As colunas especificadas não existem no conjunto de dados.")

    x_axis = data[x_column]
    y_axis = data[y_column]

    linearized_x = x_axis - x_axis.iloc[0]
    linearized_y = y_axis - y_axis.iloc[0]

    return linearized_x, linearized_y
