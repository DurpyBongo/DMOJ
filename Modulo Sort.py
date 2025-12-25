length = int(input())
num = int(input())
numbers=list(map(int,input().split()))
smalllist = []
biglist = []
for i in range(len(numbers)):
    remainder = numbers[i] % num
    smalllist.append(remainder)
    smalllist.append(numbers[i])
    biglist.append(smalllist)
    smalllist=[]
poop = biglist.sort()
for i in range(length):
    print(f'{biglist[i][1]} ',end='')


# length = int(input())
# num = int(input())
# numbers=list(map(int,input().split()))
# smalllist = []
# biglist = []
# for i in range(len(numbers)):
#     remainder = numbers[i] % num
#     smalllist.append(remainder)
#     smalllist.append(numbers[i])
#     biglist.append(smalllist)
#     smalllist=[]

# answer = []

# def insertonetolist(smallliste=[], finallist=[]):
   
#     if finallist==[]:
#         finallist.append(smallliste)
#         return finallist
#     else:
#         for idk in range(len(finallist)):
#             if smallliste[0]<finallist[idk][0]:
#                 finallist.insert(idk,smallliste)
#             elif smallliste[0]==finallist[idk][0]:
#                 if smallliste[1]<=finallist[idk][1]:
#                     finallist.insert(idk,smallliste)
#                 else:
#                     finallist.insert(idk+1,smallliste)
#         finallist.append(smallliste)
#     return finallist

# for u in range(len(biglist)):
#     print(f'{biglist[u]} is poo')
#     answer = insertonetolist(biglist[u],answer)
# print(answer)


# for pee in range(len(biglist)):
#     print(f'{(biglist[pee])[1]} ',end='')

# # HERE IS WHERE IT ENDS


# # for u in range(len(biglist)):
# #     for alex in range(len(biglist)):
# #         if (biglist[u])[0]>=(biglist[alex])[0]:
# #             biglist.insert(alex+1,biglist[u])
# #             biglist.remove(biglist[u])

# # empty=[]
# # answer=[]
# # remains_0=[]
# # for i in range(len(numbers)):
# #     remainder = numbers[i] % num
# #     if empty==[]:
# #         empty.append(remainder)
# #         answer.append(numbers[i])
# #     elif remainder==0:
# #         remains_0.append(numbers[i])
# #     for u in range(len(empty)):
# #         if remainder>=empty[u]:
# #             answer.insert(u+1,numbers[i])
# #             empty.insert(u+1,remainder)
# #             break
# # for alex in remains_0[::-1]:
# #     answer.insert(0,alex)
    
# # answer.pop()
# # for i in answer:
# #     print(f'{i} ',end='')

# # for i in numbers:
# #     remainder = i % num
# #     for u in range(len(empty)+1):
# #         if empty==[]:
# #             answer.insert(u+1,num)
# #             empty.insert(u+1,remainder)
# #         elif remainder>=empty[u]:
# #             answer.insert(u+1,num)
# #             empty.insert(u+1,remainder)
# #         print(answer)
# #         print(empty)
# # for i in answer:
# #     print(i,end='')