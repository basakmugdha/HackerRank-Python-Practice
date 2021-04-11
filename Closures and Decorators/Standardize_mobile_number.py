def wrapper(f):
    def fun(l):
        # complete the function
        newlist = ['+91 '+str(num)[-10:-5]+' '+str(num)[-5:] for num in l]
        return f(newlist)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


