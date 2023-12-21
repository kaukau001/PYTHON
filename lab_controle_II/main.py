from data.parser import DataParser
from utils.constants import XLSX_PATH, CSV_PATH, TACOMETER_VOLTAGE, ARMOR_VOLTAGE, ENGINE_SPEED
from params.simulation_params_calculator import SimulationParamsCalculator
from params.calculate_motor_controller_params import CalculateMotorControllerParams
from utils.logger import AppLogger

if __name__ == '__main__':
    logger = AppLogger().get_logger()
    xlsx_data = DataParser(XLSX_PATH, logger)
    csv_data = DataParser(CSV_PATH, logger)

    logger.warning('ANALISANDO DADOS DO EXPERIMENTO')
    voltage, tachometer, rotation = xlsx_data.linearize_xlsx(ARMOR_VOLTAGE, TACOMETER_VOLTAGE, ENGINE_SPEED)
    logger.info('DADOS DE TENSÃO DE ARMADURA, TENSÃO DO TACÔMETRO E ROTAÇÃO DO MOTOR EXTRAIDOS COM SUCESSO ')

    logger.warning('INICIANDO ANALISE DOS DADOS PARA A SIMULAÇÃO!')
    simulation_params = SimulationParamsCalculator(voltage, tachometer, rotation, logger)

    logger.warning('CALCULANDO MÉTODO DOS MÍNIMOS QUADRADOS!')
    k_mmq = simulation_params.calculate_k_mmq()

    logger.warning('CALCULANDO Kt!')
    simulation_params.calculate_kt()

    logger.warning('INICIANDO CÁLCULO DO MÉTODO DAS ÁREAS!')

    x_axis, y_chanel_one_axis, y_chanel_two_axis = csv_data.parse_csv()
    motor_controller_params = CalculateMotorControllerParams(x_axis, y_chanel_one_axis, y_chanel_two_axis, logger)
    tau, k = motor_controller_params.area_method()

    logger.warning('INICIANDO CALCULOS DOS PARAMETROS DE CONTROLE!')

    logger.warning('CALCULANDO ZETA E OMEGA_N!')
    zeta = motor_controller_params.calculate_zeta()
    omega_n = motor_controller_params.calculate_omega_n(tau, zeta)

    logger.warning('CALCULANDO KP e TI!')
    kp = motor_controller_params.calculate_kp(k, tau, zeta, omega_n)
    ti = motor_controller_params.calculate_ti(k, tau, omega_n, kp)
    logger.warning('RELATÓRIO CONCLUIDO COM SUCESSO!')

