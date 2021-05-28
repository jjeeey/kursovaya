import numpy as np

N = 6
M = 2
K = np.random.randint(0 , 10)

A = np.random.randint(low=-4, high=9, size= (N, M))
print("Матрица:\r\n{}\n".format( A))

M_n = np.sum(A, axis= 1 ) * (- 1)
A = np.hstack((A, M_n.reshape(- 1, 1)))

print("Новая матрица:\r\n{}\n".format( A))
