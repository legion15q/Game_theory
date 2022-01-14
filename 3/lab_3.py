import numpy as np
from lab_2 import Braun_Robinson


def ker(x, y):
    # функция из примера
    # return -3 * (x ** 2) + (3 / 2) * (y ** 2) + (18 / 5) * x * y - (18 / 50) * x - (72 / 25) * y
    return -5 * (x ** 2) + (5 / 12) * (y ** 2) + (10 / 3) * x * y - (2 / 3) * x - (4 / 3) * y


def saddle_points(arr):
    max_col = np.amax(arr, axis=0)
    min_row = np.amin(arr, axis=1)
    result = []
    for i in range(len(min_row)):
        for j in range(len(max_col)):
            if max_col[j] == min_row[i]:
                result.append((i, j))
    return result


def main():
    N = 10
    print('N =', N)
    H = np.zeros((N + 1, N + 1))
    for i in range(len(H)):
        for j in range(len(H)):
            H[i][j] = ker(i / N, j / N)
    print(np.round(H, 3))
    saddles = saddle_points(H)
    if len(saddles) != 0:
        for i in saddles:
            x = i[0] / N
            y = i[1] / N
            print("Найдена седловая точка.", 'x =', x, 'y =', y, 'H =', np.round(ker(x, y),4))
    else:
        print("Седловая точка не найдена. Ищем решение методом Брауна-Робинсон")
        range_ = Braun_Robinson(H)
        v_average = np.average(range_)
        idx = idx_of_nearest_value(H, v_average)
        x = idx[0] / N
        y = idx[1] / N
        print('x =', idx[0] / N, 'y =', idx[1] / N, 'H =', np.round(ker(x, y),4))


def idx_of_nearest_value(matrix_, number):
    ravel_matrix = matrix_.ravel()
    N = len(matrix_)
    idx = np.abs(ravel_matrix - number).argmin()
    return (idx // N, idx % N)


if __name__ == '__main__':
    main()
