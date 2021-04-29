
import os

# Complete the solve function below.
def solve(s):
    slist = s.split()
    for x in slist:
        s = s.replace(x,x.capitalize()) 
    return s    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
