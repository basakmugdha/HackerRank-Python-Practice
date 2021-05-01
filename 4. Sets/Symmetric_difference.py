m = int(input())
mset = set(list(map(int,input().split())))
n = int(input())
nset = set(list(map(int,input().split())))

symm_diff = list(mset.union(nset)-mset.intersection(nset))
symm_diff = sorted(symm_diff)
for x in symm_diff:
    print(x)