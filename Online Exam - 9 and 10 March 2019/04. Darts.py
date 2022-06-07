player_name = input()
line = input()
current_points = 301
successful_shots = 0
unsuccessful_shots = 0

while line != "Retire":
    shot_type = str(line)
    points = int(input())

    if shot_type == "Triple":
        points *= 3
    elif shot_type == "Double":
        points *= 2
    else:
        points *= 1
    if points <= current_points:
        current_points -= points
        successful_shots += 1
    else:
        unsuccessful_shots += 1
        line = input()
        continue
    if current_points == 0:
        break

    line = input()

if line == "Retire":
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
else:
    print(f'{player_name} won the leg with {successful_shots} shots.')