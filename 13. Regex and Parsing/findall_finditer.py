# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
matches = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
if matches:
    print (*[m for m in matches], sep='\n')
else:
    print(-1)
