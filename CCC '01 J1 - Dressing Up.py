rows = int(input())
columns = rows*2
for i in range(rows):
    if i == rows//2:
        print('*'*columns)
    elif i ==0:
        print(f"*{(columns-2)*" "}*")
    elif i< rows//2:
        print(f"{(i*2 +1)*"*"}{(columns-(2*(i*2 +1)))*" "}{(i*2 +1)*"*"}")
    elif i > rows//2:
        u = (rows//2)-abs(i-(rows//2))
        print(f"{(u*2 +1)*"*"}{(columns-(2*(u*2 +1)))*" "}{(u*2 +1)*"*"}")