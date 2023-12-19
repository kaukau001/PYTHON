import numpy as np


def area_method(x_axis: list, y_ch1_axis: list, y_ch2_axis: list) -> tuple:
    y_infinity, tau = calculate_tau(x_axis, y_ch2_axis)
    k = calculate_k(y_ch1_axis, y_infinity)
    return tau, k


def calculate_tau(x_axis: list, y_ch2_axis: list):
    print('CALCULANDO tau:')
    y_infinity = np.mean(y_ch2_axis[1500:len(y_ch2_axis)])
    print(f"O valor de y_infinity é: {y_infinity}\n")

    area_0 = np.trapz(x_axis[1500:2128], y_infinity - y_ch2_axis[1500:2128])
    print(f"A área entre a resposta e y_infinity (A0) é: {area_0}\n")

    tau = area_0 / y_infinity
    print(f"O valor de tau é: {tau}\n")
    return y_infinity, tau


def calculate_k(y_ch1_axis: list, y_infinity: float):
    step_mean = np.mean(y_ch1_axis[1500:len(y_ch1_axis)])
    print(f"O valor da tensão média do degrau linearizado 'A' é: {step_mean} V")
    K = y_infinity / step_mean
    print(f"O valor de K é: {K}\n")
    return K


def calculate_k_mmq(x_axis: list, y_axis: list) -> float:
    mmq_coefficients = np.polyfit(x_axis, y_axis, 1)
    angle_coefficient = float(mmq_coefficients[0])
    print(f"O coeficiente angular (K) obtido pelos mínimos quadrados é: {angle_coefficient:.4f}\n")
    return angle_coefficient


def calculate_kt(x_axis, y_axis):
    y_axis_rad_s = y_axis * (2 * np.pi / 60)
    mmq_coefficients = np.polyfit(x_axis, y_axis_rad_s, 1)
    angle_coefficient = float(mmq_coefficients[0])
    print(f"O coeficiente angular (Kt) obtido pelos mínimos quadrados é: {angle_coefficient:.4f}\n")
    return angle_coefficient


def calculate_csi(overtaking_percentage=0.1):
    overtaking_percentage = np.clip(overtaking_percentage, 1e-15, 1)
    csi = -np.log(overtaking_percentage) / (np.sqrt(np.log(overtaking_percentage) ** 2 + np.pi ** 2))
    print(f"O valor de Csi é: {csi:.4f}\n")
    return csi


def calculate_omega_n(tau, overtaking_percentage=0.1):
    csi = calculate_csi(overtaking_percentage)
    omega_n = 1 / (tau * csi)
    print(f"O valor de omega_n é: {omega_n:.4f}\n")
    return csi, omega_n


def calculate_kp(csi, omega_n, tau, k_mmq):
    kp = ((2 * csi * omega_n * tau) - 1) / k_mmq
    print(f"O valor de do parâmetro Kp é: {kp:.4f}\n")
    return kp


def calculate_ti(omega_n, tau, k_mmq, kp):
    fi = ((omega_n**2) * tau)/(k_mmq*kp)
    print(f"O valor de do parâmetro Fi é: {fi:.4f}\n")
    ti = 1/fi
    print(f"O valor de do parâmetro Ti é: {ti:.4f}\n")
    return ti
