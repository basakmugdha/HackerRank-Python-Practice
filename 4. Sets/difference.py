n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

total = len(english.symmetric_difference(french))
print(total)
