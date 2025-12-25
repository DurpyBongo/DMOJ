number = int(input())
word = input()
array = list(word)
acount = 0
bcount=0
for i in range(number):
    if array[i]=='A':
        acount+=1
    else:
        bcount+=1
if acount>bcount:
    print("A")
elif acount<bcount:
    print("B")
else:
    print("Tie")