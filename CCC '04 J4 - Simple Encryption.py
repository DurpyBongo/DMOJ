encryption = input()
widthpanel = len(encryption)
actualinput = input()

def getcode(word):
    code = []
    newnewword = []
    for i in range(len(word)):
        if word[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            newnewword.append(word[i])
    for u in range(len(newnewword)):
        code.append(ord(newnewword[u])-65)
    return code
# to get the numbers for the code encryption



def columns(otherinput):
    message = []
    empty_column = []
    all_columns = []
    for p in range(len(otherinput)):
        if otherinput[p] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            message.append(otherinput[p]) # gets rid of spaces and bad stuff
    for jk in range(widthpanel):
        for n in range(len(message)):
            modnumber = (n+1) % widthpanel
            if modnumber == jk:
                empty_column.append(message[n])
        all_columns.append(empty_column)
        empty_column = []
    move = all_columns[0]
    all_columns.pop(0)
    all_columns.append(move)
    return all_columns


# the message will be split into the columsn whether to add how much 


def findnumber(letter, number):
    start = ord(letter) - ord('A')
    shifted = (start + number) % 26
    return chr(ord('A') + shifted)

# given a letter and number, find the new letter

code_list = getcode(encryption)
big_column_list = columns(actualinput)
    
max_height = 0
for poopy in big_column_list:
    if len(poopy) > max_height:
        max_height = len(poopy)


# max height so i know where to stop
# finding row and column essentially
for row in range(max_height):
    for mini_column in range(widthpanel):
        if row < len(big_column_list[mini_column]):
            letter = big_column_list[mini_column][row]
            shift = code_list[mini_column]
            print(findnumber(letter, shift), end='')
# for code_number in range(len(code_list)):
#     for mini_column_number in range(widthpanel):
#         if code_number < len(big_column_list[mini_column_number]):
#             letter = big_column_list[mini_column_number][code_number]
#             shift = code_list[code_number]
#             print(findnumber(letter, shift), end='')

