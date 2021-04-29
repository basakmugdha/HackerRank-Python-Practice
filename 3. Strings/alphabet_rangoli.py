def print_rangoli(size):
    #upper half
    for i in range(size,1,-1):
        s = '-'.join(chr(ord('a')+j) for j in range(i-1,size))
        print((s[::-1]+s[1:]).center(size*4-3,'-'))
    #lower half
    for i in range(1,size+1):
        s = '-'.join(chr(ord('a')+j) for j in range(i-1,size))
        print((s[::-1]+s[1:]).center(size*4-3,'-'))
        
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)