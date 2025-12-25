first= input()
second=input()

asdf = second


def rearrange(word):
    word_list = list(word)
    move = word_list[0]
    word_list.pop(0)
    word_list.append(move)
    result = ''.join(word_list)
    return result
        
for i in range(len(list(second))):
    if first.find(asdf) != -1:
        print('yes')
        break
    else:
        asdf = rearrange(asdf)

    if i == len(list(second))-1 and first.find(asdf) == -1: 
        print('no')
        break



