rounds = int(input())
s_letter = 0
t_letter = 0
for i in range(rounds):
    c= input()
    c = c.upper()
    phrase = list(c)
    for u in phrase:
        if u=='T':
            t_letter +=1
        elif u=='S':
            s_letter+=1
if s_letter>=t_letter:
    print('French')
else:
    print('English')

    