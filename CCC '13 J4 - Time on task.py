time = int(input())
amount = int(input())
empty = []
for i in range(amount):
    C = int(input())
    empty.append(C)
empty.sort()

zero = 0
another = 0
for u in range(len(empty)):
    if empty[u]+zero <= time:
        zero=empty[u]+zero
        another+=1
    else:
        print(another)
        break