days = int(input())
array = []
for i in range(days):
    weather = input()
    array.append(weather)

#Has list with all S and P
# sunny = 'S'

# sunny_indices = []
# for i in range(len(array)):
#     if array[i] == sunny:
#         sunny_indices.append(i)
# #sunny_indices has all index for S

# consecutive = []
# for u in range(len(sunny_indices)):
#     if sunny_indices[u]


def consecutive(list):
    count=0
    maximus=0
    for i in list:
        if i == 'S':
            count+=1
        else:
            if count>=maximus:
                maximus=count
            count=0
    maximus = max(maximus, count)
    return maximus



array_copy = array.copy()

real_max = 0
for u in range(len(array)):
    if array[u] == 'P':
        array_copy[u]="S"
        current=consecutive(array_copy)
        if current>=real_max:
            real_max=current
            array_copy[u]='U'
        else:
            array_copy[u]='U'
    elif array[u] == 'S':
        array_copy[u]='P'
        current = consecutive(array_copy)
        if current>=real_max:
            real_max=current
            array_copy[u]='S'
        else:
            array_copy[u]='S'
print(real_max)
