import numpy as np

def water_filling(H, sigma_ndB, P_dB):
    U, S, V = np.linalg.svd(H)
    Eigen_values = np.linalg.svd(H)[1] ** 2
    sigma_n = 10 ** (sigma_ndB / 10)
    P = 10 ** (P_dB / 10)
    N = len(Eigen_values)
    T_powers = np.zeros(N)
    All = sigma_n * np.sum(1 / Eigen_values)
    beta = (P + All) / N
    T = N
    for i in range(N):
        if beta - sigma_n / Eigen_values[i] > 0:
            T_powers[i] = beta - sigma_n / Eigen_values[i]
        else:
            T_powers[i] = 0
            T -= 1
            beta = P + (sigma_n * (np.sum(1 / Eigen_values) - (1 / Eigen_values[i]))) / T
    return T_powers

# Example usage:
H = np.array([[3, 0, 8],
              [0, 1, 0],
              [4, 0, 6]])
sigma_ndB = 3  # Receiver noise power in dB
P_dB = -1.75  # Transmit power in dB

T_powers = water_filling(H, sigma_ndB, P_dB)
print("Allocated Transmit Powers (linear scale):", T_powers)

    