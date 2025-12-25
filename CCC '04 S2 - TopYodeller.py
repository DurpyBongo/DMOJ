poop = list(map(int,input().split()))
players = poop[0]
rounds = poop[1]
all_rounds_list = []
player_total_score = []
for i in range(rounds):
    oneround = list(map(int,input().split()))
    all_rounds_list.append(oneround)
for x in range(players):
    playerscore=0
    for u in range(len(all_rounds_list)):
        playerscore+=all_rounds_list[u][x]
    player_total_score.append(playerscore)


value_to_find = max(player_total_score)
indices = []
for i in range(len(player_total_score)):
    if player_total_score[i] == value_to_find:
        indices.append(i)

cumulative_scores = [0] * players
worst_rank = [0] * players

for r in range(rounds):
    for p in range(players):
        cumulative_scores[p] += all_rounds_list[r][p]
    for p in range(players):  
        count_higher = 0       
        for q in range(players):   
            if cumulative_scores[q] > cumulative_scores[p]:
                count_higher += 1
        rank = 1 + count_higher  
        worst_rank[p] = max(worst_rank[p], rank)



for i in indices:
    print(f'Yodeller {i+1} is the TopYodeller: score {player_total_score[i]}, worst rank {worst_rank[i]}')
    

