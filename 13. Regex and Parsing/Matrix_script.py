import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
  
message = ''
for x in zip(*matrix):
    message += "".join(x)

clean_msg  =  re.sub(r'(?<=\w)[^\w]+(?=\w)',' ', message)     
print(clean_msg.strip())

