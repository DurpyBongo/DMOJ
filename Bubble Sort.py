number_of_numbers = int(input())
number_list=list(map(int,input().split()))
count=0
for poop in number_list:
    print(f'{poop}', end=' ')
print('')
while True:
    for i in range(number_of_numbers-1):
        if number_list[i]>number_list[i+1]:
            temp = number_list[i]
            number_list[i] = number_list[i+1]
            number_list[i+1] = temp
            count+=1
        
            for u in number_list:
                print(f'{u}', end=' ')
            print('')
    if count==0:
        break
    else:
        count=0
