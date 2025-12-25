# K = int(input())
# word = input()
# badnk = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# for i in range(1,len(word)):
#     S = 3*(i) + K
#     position = i-1-S
#     if position <0:
#         position +=28
#         print(badnk[position],end='')
#     else:
#         print(badnk[position],end='')


# K = int(input())
# word = input()
# word_list = list(word)
# def get_position(i,fixed_value):
#     num_of_Char= ord(i)-65+1
#     return 3*num_of_Char + fixed_value
# def get_chr(character,step):
#     poop = step % 26
#     num_value = ord(character)+poop
#     if num_value>90:
#         num_value -=90
#         return chr(64+num_value)
#     else:
#         return chr(num_value)
# print(get_position('F',3))
# print(get_chr('F',21))
# for i in word_list:
#     print(get_chr(i,get_position(word_list.index(i),K)),end='')
    
    
# for i in range(len(word_list)):
#     S = 3*(ord(word_list[i]))-65+K
#     position = ord(word_list[i])-S
#     if position <65:
#         print(chr(65-position+91),end='')
#     else:
#         print(chr(position))

constant = int(input())
word = input()

for i in range(len(word)):
    shift = 3*(i+1) + constant
    shift = shift % 26
    if ord(word[i])-shift < 65:
       print(chr(91-(65-(ord(word[i])-shift))),end='')
    else:
        print(chr(ord(word[i])-shift),end='')