if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper = False
    for x in s:
        if x.isalnum() and not alnum:
            alnum=True
        if x.isalpha() and not alpha:
            alpha=True
        if x.isdigit() and not digit:
            digit=True
        if x.islower() and not lower:
            lower=True
        if x.isupper() and not upper:
            upper=True
    
    print (alnum)
    print (alpha)
    print (digit)
    print (lower)
    print (upper)
