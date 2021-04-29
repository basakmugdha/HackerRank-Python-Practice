def split_and_join(line):
    # write your code here
    my_list = line.split(" ")
    line = "-".join(my_list)
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)