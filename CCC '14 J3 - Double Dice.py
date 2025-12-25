first = 100
second = 100
rounds = int(input())
for i in range(rounds):
    C = input()
    answer=C.split()
    actual = [ int(x) for x in answer ]
    if actual[0]<actual[1]:
        first=first-actual[1]
    elif actual[0]>actual[1]:
        second=second-actual[0]
print(first)
print(second)
            
