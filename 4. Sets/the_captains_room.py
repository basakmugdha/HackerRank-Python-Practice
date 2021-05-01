k = int(input())
rn_list = list(map(int,input().split()))
rn_set = set(rn_list)
print(((sum(rn_set)*k) - sum(rn_list))//(k-1))
