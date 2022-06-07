total_locations = int(input())
daily_total = 0
diff = 0

for locations in range(total_locations):
    expected_average_gold = float(input())
    days = int(input())
    for days in range(1, days + 1):
        daily_gold = float(input())
        daily_total += daily_gold
    average_gold = daily_total / days
    if average_gold < expected_average_gold:
        diff = expected_average_gold - average_gold
        print(f'You need {diff:.2f} gold.')
    else:
        diff = average_gold - expected_average_gold
        print(f'Good job! Average gold per day: {average_gold:.2f}.')
    daily_total = 0