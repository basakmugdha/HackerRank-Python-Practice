import re

n = int(input())
pattern = re.compile(r'^[456]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$')
for _ in range(n):
    cnum = input()
    if re.match(pattern, cnum):
        print('Invalid' if re.search(r'(\d)-?\1-?\1-?\1', cnum) else 'Valid')
    else:
        print('Invalid')