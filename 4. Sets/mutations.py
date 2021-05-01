n = int(input())
a = set(map(int, input().split()))

ops = int(input())
for _ in range(ops):
    operation, length = input().split()
    update_list = list(map(int, input().split()))
    if operation == 'update':
        a.update(update_list)
    elif operation == 'intersection_update':
        a.intersection_update(update_list)
    elif operation == 'difference_update':
        a.difference_update(update_list)
    elif operation == 'symmetric_difference_update':
        a.symmetric_difference_update(update_list)
        
print(sum(a))
