
n = int(input())
s = set(map(int, input().split()))

m = int(input())
for _ in range(m):
    command = list(input().split())
    if len(command)>1:
       value = int(command[1]) 
    
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(value)
    elif command[0] == 'discard':
        s.discard(value)
        
print(sum(s))
