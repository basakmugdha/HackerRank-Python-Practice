# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_carpet(n,m):
    #upper half
    for i in range(n//2):
        s = ''.join('.|.' for _ in range(i*2+1))
        print((s).center(m,'-'))
    print('WELCOME'.center(m,'-'))
    #lower half
    for i in range(n//2-1,-1,-1):
        s = ''.join('.|.' for _ in range(i*2+1))
        print((s).center(m,'-'))
        
if __name__ == '__main__':
    n,m = map(int,input().split())
    print_carpet(n,m)
