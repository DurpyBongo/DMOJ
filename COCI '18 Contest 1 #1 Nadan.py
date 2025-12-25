money = int(input())
groups = int(input())
one = 1
total = 0
for i in range(groups-1):
    print(one)
    total +=one
    one+=1
print(money-total)
