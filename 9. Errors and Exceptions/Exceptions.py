t = int(input())
for _ in range(t):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')
