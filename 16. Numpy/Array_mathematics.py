import numpy as np
np.set_printoptions(sign=' ')
n,m = map(int, input().split())
A = np.array([input().split() for _ in range(n)],int)
B = np.array([input().split() for _ in range(n)],int)

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(A//B)
print(np.mod(A,B))
print(np.power(A,B))
