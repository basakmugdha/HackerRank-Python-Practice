# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'^[789]\d{9}$')
t = int(input())
for _ in range(t):
    print ("YES" if re.match(pattern, input()) else "NO")
