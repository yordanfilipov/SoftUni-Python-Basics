name_of_tournament = input()
won = 0
lost = 0

while name_of_tournament != "End of tournaments":
    matches_count = int(input())
    for i in range(1, matches_count + 1):
        dessie_points = int(input())
        opponent_points = int(input())

        if dessie_points > opponent_points:
            won += 1
            print(f'Game {i} of tournament {name_of_tournament}: win with {dessie_points - opponent_points} points.')
        else:
            lost += 1
            print(f'Game {i} of tournament {name_of_tournament}: lost with {opponent_points - dessie_points} points.')
    name_of_tournament = input()

total_games = won + lost
won_percent = (won / total_games) * 100
lost_percent = (lost / total_games) * 100

print(f'{won_percent:.2f}% matches win')
print(f'{lost_percent:.2f}% matches lost')