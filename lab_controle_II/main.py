from params.calculate_params import area_method, calculate_k_mmq, calculate_kt, calculate_omega_n, calculate_kp, \
    calculate_ti
from data.parser import DataParser
from utils.constants import XLSX_PATH, CSV_PATH
if __name__ == '__main__':
    xlsx_data = DataParser(XLSX_PATH)
    csv_data = DataParser(CSV_PATH)
    print(50*'-')
    print('ANALISANDO DADOS DO EXPERIMENTO')
    print(50*'-')
    print('CALCULANDO MÉTODO DOS MÍNIMOS QUADRADOS...')
    print(50*'-')
    print('CALCULANDO K:')
    xlsx_x_axis, xlsx_y_axis = xlsx_data.parse_xlsx('Tensão', 'Tacômetro')
    k_mmq = calculate_k_mmq(xlsx_x_axis, xlsx_y_axis)

    print('CALCULANDO Kt:')
    xlsx_x_axis, xlsx_y_axis = xlsx_data.parse_xlsx('Tacômetro', 'Rotação')
    calculate_kt(xlsx_x_axis, xlsx_y_axis)

    print(50*'-')
    print('CALCULANDO MÉTODO DAS ÁREAS...')
    print(50*'-')
    csv_x_axis, csv_y_ch1_axis, csv_y_ch2_axis = csv_data.parse_csv()
    tau, k = area_method(csv_x_axis, csv_y_ch1_axis, csv_y_ch2_axis)

    print(50*'-')
    print('CALCULANDO OS PARAMETROS DE CONTROLE:')
    print(50*'-')
    print('CALCULANDO Csi e omega_n:')
    csi, omega_n = calculate_omega_n(tau)
    print('CALCULANDO Kp e Ti:')
    kp = calculate_kp(csi, omega_n, tau, k_mmq)
    ti = calculate_ti(omega_n, tau, k_mmq, kp)
    print('RELATÓRIO CONCLUIDO COM SUCESSO!')
