games = int(input())
sum1 = 0
sum2=0
empty = []
first = input()
second = input()
firstgames = first.split()
secondgames = second.split()
for i in range(games):
    sum1 += int(firstgames[i])
    sum2+= int(secondgames[i])
    if sum1==sum2:
        empty.append(i+1)
if empty=='0' or empty==[]:
    print('0')
else:
    print(max(empty))
    