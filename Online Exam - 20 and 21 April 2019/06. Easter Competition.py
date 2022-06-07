easter_bread_count = int(input())
previous_player_points = 0
current_points = 0

for bread in range(easter_bread_count):
    chef_name = input()
    previous_player_points = current_points
    current_points = 0
    line = input()
    while line != "Stop":
        point = int(line)
        current_points += point

        line = input()
        if line == "Stop":
            print(f'{chef_name} has {current_points} points.')
            if current_points > previous_player_points:
                print(f'{chef_name} is the new number 1!')
                competition_winner = chef_name
                current_winner_points = current_points
print(f'{competition_winner} won competition with {current_winner_points} points!')