n = int(input())
for _ in range(n):
    a, set_a = int(input()), set(map(int,input().split()))
    b, set_b = int(input()), set(map(int,input().split()))
    if set_a.issubset(set_b):
        print(True)
    else:
        print(False)
