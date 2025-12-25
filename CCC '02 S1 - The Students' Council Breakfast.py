pink = int(input())
green = int(input())
red = int(input())
orange = int(input())

total = int(input()) # test
combo = 0
smallest = []
for p in range((total//pink)+1):
    for g in range((total//green)+1):
        for r in range((total//red)+1):
            for o in range((total//orange)+1):
                if p*pink+g*green+r*red+o*orange==total:
                    combo+=1
                    print(f'# of PINK is {p} # of GREEN is {g} # of RED is {r} # of ORANGE is {o}')
                    smallest.append(p+g+r+o)
print(f'Total combinations is {combo}.')
print(f'Minimum number of tickets to print is {min(smallest)}.')

