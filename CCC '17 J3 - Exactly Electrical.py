x = input()
start = x.split()
y = input()
destination = y.split()
energy = int(input())
answer = abs(int(start[0])-int(destination[0]))+abs(int(start[1])-int(destination[1]))
mod = answer % 2
if energy == answer:
    print('Y')
elif energy % 2 == mod and answer<energy:
    print('Y')
else:
    print('N')


