walk_minutes = int(input())
walks_count = int(input())
taken_calories = int(input())

walk_minutes *= walks_count
burned_calories = walk_minutes * 5

if burned_calories >= (taken_calories / 2):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')