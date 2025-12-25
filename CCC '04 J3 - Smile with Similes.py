adjectives = int(input())
nouns = int(input())
adjectives_list = []
noun_list = []
for i in range(adjectives):
    word_adjective = input()
    adjectives_list.append(word_adjective)
for i in range(nouns):
    word_noun = input()
    noun_list.append(word_noun)
for adj in adjectives_list:
    for nom in noun_list:
        print(f'{adj} as {nom}')