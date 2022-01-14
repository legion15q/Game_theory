import numpy as np
import random


def main():
    A = np.array(
        [[1, 11, 11],
         [7, 5, 8],
         [16, 6, 2]]
    )
    Braun_Robinson(A)
    return 1

def Braun_Robinson(matrix_):
    N = len(matrix_)
    sum_1 = np.zeros(N)  # -- суммарный выигрыш первого игрока
    sum_2 = np.zeros(N)  # -- суммарный выиграш второго игрока
    k = 0
    v_i1 = np.array([])
    v_i2 = np.array([])
    x_bar = np.zeros(N)  # -- смешанная стратегия первого игрока
    y_bar = np.zeros(N)  # -- смешанная стратегия второго игрока
    epsilon = 1
    while (epsilon > 0.3) and (k != 500):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        sum_1 += matrix_[:, j]
        sum_2 += matrix_[i]
        v_i1 = np.append(v_i1, np.amax(sum_1) / (k + 1))
        v_i2 = np.append(v_i2, np.amin(sum_2) / (k + 1))
        x_bar[i] += 1
        y_bar[j] += 1
        k += 1
        epsilon = np.amin(v_i1) - np.amax(v_i2)

    print(epsilon)
    print(k)
    v_lower = np.amax(v_i2)
    v_top = np.amin(v_i1)
    print(v_lower)
    print(v_top)
    print(x_bar / k)
    print(y_bar / k)

if __name__ == '__main__':
    main()
