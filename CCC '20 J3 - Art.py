num_droplets = int(input())
x = []
y=[]
for i in range(num_droplets):
    coord = input()
    coordinate_planes = coord.split(',')
    x.append(coordinate_planes[0])
    y.append(coordinate_planes[1])
print(f'{int(min(x))-1},{int(min(y))-1}')
print(f'{int(max(x))+1},{int(max(y))+1}')