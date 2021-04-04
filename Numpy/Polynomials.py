import numpy as np

p = np.array(input().split(), int)
x = int(input())

print(np.polyval(p,x))
