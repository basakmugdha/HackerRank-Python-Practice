import numpy as np
#this code uses the linalg sub-module of numpy

n = int(input())
matrix = np.empty((n,n), dtype=float)
for i in range(n):
    matrix[i] = list(map(float, input().split()))

print (round(np.linalg.det(matrix), 2))