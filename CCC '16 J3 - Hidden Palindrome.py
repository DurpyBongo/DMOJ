# word = input()
# nothing = []
# answer = []
# for i in range(len(list(word))):
#     answer=[]
#     nothing.append(i)
#     if nothing == nothing.reverse() and len(nothing)>=len(answer):
#         answer.append(nothing)
#     elif nothing!= nothing.reverse():
#         nothing = []
# print(answer)

# word = list(input())
# length = len(word)
# count = 0
# extra = word.copy()
# for i in range(length):
#     if extra==extra[::-1]:
#         if len(extra)>=count:
#             count=len(extra)
#     extra.pop()
# extra=word.copy()
# for i in range(length):
#     if extra==extra[::-1]:
#         if len(extra)>=count:
#             count=len(extra)
#     extra.pop(0)
# extra=word.copy()
# print(count)


# word = list(input())
# count=0
# extra = word.copy()
# extra.insert(0,'f')
# for i in range(len(word)):
#     extra.pop()
#     for j in range(i):
#         if extra==extra[::-1]:
#             if len(extra)>= count:
#                 count=len(extra)
#         extra.pop()
# print(count)

word = list(input())
count=0
extra = word.copy()
for i in range(len(word)):
    for u in range(i+1,len(word)+1):
        palindrome = extra[i:u]
        if palindrome==palindrome[::-1]:
            if len(palindrome)>=count:
                count=len(palindrome)
print(count)

