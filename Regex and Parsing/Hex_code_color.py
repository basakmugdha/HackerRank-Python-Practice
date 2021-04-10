# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'(?<!^)#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b')
t = int(input())
for _ in range(t):
    m = re.findall(pattern, input())
    if m:
        print (*m, sep='\n')
