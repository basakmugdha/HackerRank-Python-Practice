# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for _ in range(t):
    uid = input().strip()
    if uid.isalnum() and len(uid)==10:
        try:
            assert re.search(r'[A-Z]{2,}', uid)
            assert re.search(r'\d{3,}', uid)
            assert not re.search(r'(.).*\1', uid)
        except:
            print('Invalid')
        else:
            print('Valid')
