import re
t = int(input())
pattern = re.compile(r'^[+-]?[0-9]*[.][0-9]*$')
for _ in range(t):
    print(pattern.match(input()) != None)
