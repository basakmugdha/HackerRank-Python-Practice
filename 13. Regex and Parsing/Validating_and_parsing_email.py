# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'(?<=\<)[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}(?=\>)')
t = int(input())
for _ in range(t):
    string = input()
    if re.search(pattern, string):
        print (string)
