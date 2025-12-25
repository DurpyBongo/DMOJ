first = int(input())
second = int(input())
num_list = []
num_list.append(first)
num_list.append(second)
toatl = 2
while first>=second:
    third=first-second
    first=second
    second=third
    toatl+=1
    # for i in range(len(num_list)):
    #     if num_list[i]>num_list[i+1]:
    #         num_list.append(num_list[i]-num_list[i+1])
    #     else:
    #         for u in range(len(num_list)):
    #             toatl+=1
print(toatl)