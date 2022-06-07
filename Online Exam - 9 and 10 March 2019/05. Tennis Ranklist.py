import math
tournaments = int(input())
starting_points = int(input())

total_points = 0
won = 0

for i in range(tournaments):
    reached_point = input()
    if reached_point == "W":
        total_points += 2000
        won += 1
    elif reached_point == "F":
        total_points += 1200
    else:
        total_points += 720


print(f'Final points: {total_points + starting_points}')
print(f'Average points: {math.floor(total_points / tournaments)}')
percent = (won / tournaments) * 100
print(f'{percent:.2f}%')