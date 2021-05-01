# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab, bc = int(input()), int(input())
theta = math.degrees(math.atan2(ab,bc))
degree_sign= u'\N{DEGREE SIGN}'
print(f'{round(theta)}{degree_sign}')
