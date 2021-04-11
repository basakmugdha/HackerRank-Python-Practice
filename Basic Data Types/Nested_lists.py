if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    scores = [marks for [name,marks] in records]
    second = sorted(list(set(scores)))[1]    
    
    names =[name for [name,marks] in records if marks == second]
     
    names.sort()      
    for x in names:
         print(x)
