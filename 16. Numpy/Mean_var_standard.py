import numpy as np

n, m = list(map(int, input().split()))
matrix = np.empty((n,n), dtype=int)
for i in range(n):
    matrix[i] = list(map(int, input().split()))
    
print(np.mean(matrix, axis=1))
print(np.var(matrix, axis=0))
print(round(np.std(matrix), 11))