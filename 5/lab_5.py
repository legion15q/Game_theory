import numpy as np
import random


def main():
    N = 10
    matrix_ = []
    for j in range(N):
        row = []
        for i in range(N):
            row.append((random.randint(0, 50), random.randint(0, 50)))
        matrix_.append(row)
    A = np.zeros((N, N))
    B = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            A[i][j] = matrix_[i][j][0]
            B[i][j] = matrix_[i][j][1]
    print('M = ', matrix_)
    print('A =', A)
    print('B =', B)
    max_j = np.argmax(A, axis=0)
    max_i = np.argmax(B, axis=1)
    optimum_set = []
    for i in range(N):
        if max_i[i] == max_j[i]:
            optimum_set.append((i, max_i[i]))
    print('Найдены равновесные по Нэшу и оптимальные по Парето ситуации:',  optimum_set)

if __name__ == '__main__':
    main()
