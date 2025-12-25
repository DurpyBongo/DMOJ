
number = int(input())
number +=1
while True:
    empty = list(str(number))
    if len(set(empty))==len(empty):
        print(number)
        break
    else:
        number+=1

# number=int(input())
# number+=1
# while True:
#     for i in range(1,len(str(number))):
#         if i==1:
#             if number[0]==number[i]:
#                 number+=1
#         elif i!=number[-1]:
#             if number[i]==number[i-1]:
#                 number+=1
        





# number = int(input())+1
# number_set = []
# grah = []
# for u in list(str(number)):
#     grah.append(u)

#     for digit in list(str(number)):
#         number_set.append(digit)
#         for l in number_set:
#             if l==grah:
#                 number+1
#                 break
# print(number)

    







# poop = int(input())
# num = poop +1
# digit = 0
# num_list = list(str(num)) # 1,9,8,7
# for i in range(len(num_list)): #0,1,2,3
#     if i+1==len(num_list)-1:
#         print(num)
#         break
#     else:
#         if num_list[i] == num_list[i+1]:
#             num +=1
#             digit = 0
#         else:
#             digit +=1
#             if digit==(len(num_list))-1:
#                 print(num)
#                 break


# for i in range(len(list(num))):
#     while num[i] == num[i+1]:





