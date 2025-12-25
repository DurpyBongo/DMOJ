#y,m,d
rounds = int(input())
answer = []
for i in range(rounds):
    date = input()
    date_list = date.split()
    if int(date_list[0])<1989:
        answer.append('Yes')
    elif int(date_list[0])==1989:
        if int(date_list[1])<2:
            answer.append('Yes')
        elif int(date_list[1])==2:
            if int(date_list[2])<=27:
                answer.append('Yes')
            else:
                answer.append('No')
        else:
            answer.append('No')
    else:
        answer.append('No')
for u in answer:
    print(u)