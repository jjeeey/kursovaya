import numpy as np

N = 4
M = 5

V = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(V))

a = np.diagonal(V)
a_sum = a.sum()
print("Главная диагональ: \n" + str(a) + "\n Её сумма = " + str(a_sum))
b = np.fliplr(V).diagonal(0)
b_sum = b.sum()
print("Побочная диагональ: \n" + str(b) + "\n Её сумма = " + str(b_sum))
