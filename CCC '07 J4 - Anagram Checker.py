first = list(input())
second = list(input())


a = []
for sigma in first:
    if sigma in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        a.append(sigma)
b = []
for i in second:
     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        b.append(i)
a = sorted(a)
b = sorted(b)
if a == b:
    print('Is an anagram.')
else:
    print('Is not an anagram.')