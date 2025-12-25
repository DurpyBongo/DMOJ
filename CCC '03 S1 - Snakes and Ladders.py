import sys
square = 1
while True:
    dice = int(input())
    square+=dice
    if square>100:
        square-=dice
    if square==1:
        square+=dice
    elif square ==9:
        square=34
    elif square ==40:
        square=64
    elif square ==67:
        square=86
    elif square ==54:
        square=19
    elif square ==90:
        square=48
    elif square ==99:
        square=77

    
    if dice==0:
        print('You Quit!')
        sys.exit()
    elif square==100:
        print('You are now on square 100')
        print('You Win!')
        sys.exit()
    else:
        print(f'You are now on square {square}')
    

    