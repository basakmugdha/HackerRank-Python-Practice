set_a = set(map(int,input().split()))
n = int(input())
strict_superset = True
for _ in range(n):
    other_set = set(map(int,input().split()))
    if not set_a.issuperset(other_set):
        strict_superset = False
        break
print(strict_superset)