seats = int(input())
num_list = []
total = 0
for i in range(seats):
    num = int(input())
    num_list.append(num)
    across = seats//2 
for u in range(seats):
    if u+across<=seats-1:
        if num_list[u] == num_list[u+across]:
            total+=2
print(total)