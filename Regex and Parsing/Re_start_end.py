# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()
m = False
for i in range(len(s)): 
    if re.match(k,s[i:]):
        m = True
        print(f'({i}, {len(k)+i-1})')
if not m:
    print('(-1, -1)')
