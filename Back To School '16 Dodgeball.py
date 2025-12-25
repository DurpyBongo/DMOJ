num_of_students = int(input())
students=list(map(str,input().split()))
firstletter = []
for i in students:
    firstletter.append((i[0]).upper())
newword = ''.join(firstletter)

def combo(rando):
    values = len(rando)
    answer = (values*(values+1))/2
    return answer
basket = ['120983']
final_groups = []
for i in range(num_of_students):
    if firstletter[i]==basket[0]:
        basket.append(firstletter[i])
    else:
        final_groups.append(basket)
        basket=[]
        basket.append(firstletter[i])
final_groups.append(basket)
sigma_answer = 0
final_groups.pop(0)

for i in range(len(final_groups)):
    comboniations_of_group = combo(final_groups[i])
    sigma_answer+=comboniations_of_group
print(int(sigma_answer)%1000000007)


# for u in range(students):
#     if u < num_of_students-1:
#         if firstletter[u]==firstletter[u+1]:
#             answer+=1
        
