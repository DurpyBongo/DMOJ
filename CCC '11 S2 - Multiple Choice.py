lines = int(input())
empty = []
haha = []
for i in range(lines*2):
    if i<= lines-1:
        student_answer = input()
        empty.append(student_answer)
    else:
        student_answer = input()
        haha.append(student_answer)
count = 0
for u in range(lines):
    if empty[u]==haha[u]:
        count+=1
print(count)




