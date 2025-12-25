finger = int(input())
maximus = 0

if finger<=5:
    maximus+=1


for i in range(1,6):
    for u in range(1,6):
        if i +u==finger and i>=u:
            maximus+=1

print(maximus)
# else:
#     for i in range(finger-1, 0, -1):
#         u=finger-i
#         if i>=u:
#             maximus+=1
#     print(maximus)
# for i in range(5, 0, -1):
#     if finger-i<=5 and i>=finger-i:
#         maximus+=1


# print(maximus)