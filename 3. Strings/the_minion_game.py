def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    Kevin_points = 0
    Stuart_points = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin_points += len(string) - i   
        else:
            Stuart_points += len(string) - i
    
   
    if Kevin_points > Stuart_points:
        print("Kevin {}".format(Kevin_points))
    elif Kevin_points < Stuart_points:
        print("Stuart {}".format(Stuart_points))
    else:
        print("Draw")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)