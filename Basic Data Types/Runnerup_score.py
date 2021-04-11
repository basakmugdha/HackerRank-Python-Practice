if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array=set(arr)
    array = [i for i in array]
    array.sort(reverse=True)
    print(array[1])