if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command, *inputs = input().split()
        inputs = list(map(int, inputs))
        if command == 'print':
            print(arr)
        elif  command == 'insert':
            arr.insert(inputs[0],inputs[1])
        elif  command == 'remove': 
            arr.remove(inputs[0])
        elif  command == 'append': 
            arr.append(inputs[0])
        elif  command == 'sort': 
            arr.sort()
        elif  command == 'pop': 
            arr.pop()
        elif  command == 'reverse': 
            arr.reverse() 
