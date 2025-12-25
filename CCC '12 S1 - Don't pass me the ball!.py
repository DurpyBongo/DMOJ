J = int(input())
zero = 0
for i in range(1,J):
    for u in range(1,J):
        for x in range(1,J):
            if x>u>i:
                zero += 1
print(zero)