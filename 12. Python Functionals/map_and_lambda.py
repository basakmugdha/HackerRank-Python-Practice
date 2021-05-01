cube = lambda x: pow(x,3) 

def fibonacci(n):
    # return a list of fibonacci numbers
    fiblist = [0,1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2,n):
            fiblist.append(fiblist[i-1]+fiblist[i-2])
        return fiblist
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))