array = []
while True:
    word = input()
    array.append(word)
    if word=='SCHOOL':
        break
array.reverse()
array.pop(0)
array.append('HOME')
temporary = []
for i in array:
    if i =='L' or i=='R':
        temporary.append(i)
    else:
        temporary.append(i)
        if temporary[0]=='L':
            if temporary[1]=='HOME':
                print(f'Turn RIGHT into your HOME.')
            else:
                print(f'Turn RIGHT onto {temporary[1]} street.')
        elif temporary[0]=='R':
            if temporary[1]=='HOME':
                print(f'Turn LEFT into your HOME.')
            else:
                print(f'Turn LEFT onto {temporary[1]} street.')
        temporary = []
