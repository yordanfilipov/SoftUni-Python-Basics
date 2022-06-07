days_count = int(input())
hours_per_day = int(input())
price = 0
total_price = 0

for day in range(1, days_count + 1):
    for hours in range(1, hours_per_day + 1):
        if day % 2 == 0 and hours % 2 == 1:
            price += 2.50
        elif day % 2 == 1 and hours % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f'Day: {day} - {price:.2f} leva')
    total_price += price
    price = 0
print(f"Total: {total_price:.2f} leva")