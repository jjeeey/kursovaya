import numpy as np
print("Введите число строк:")
n = int(input())
print("Введите число столбцов:")
m = int(input())
arr = np.random.randint(10,20,(n,m))
arrav=arr.mean(axis=1)
print(arrav)
arrmin = arrav.min()
print(arrmin
