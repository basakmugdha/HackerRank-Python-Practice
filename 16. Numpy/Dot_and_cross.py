import numpy as np

n = int(input())
A = np.empty((n,n), dtype=int)
B = np.empty((n,n), dtype=int)
for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(n):
    B[i] = list(map(int, input().split()))

print(np.dot(A,B))
