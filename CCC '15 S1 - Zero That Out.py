num_of_lines = int(input())
num_list = [0,0,0,0]
final = 0
for i in range(num_of_lines):
    num = int(input())
    if num ==0:
        num_list.pop()
    else:
        num_list.append(num)
for u in num_list:
    final+=u
print(final)