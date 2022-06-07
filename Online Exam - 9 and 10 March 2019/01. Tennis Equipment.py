import math
tennis_rocket_price = float(input())
tennis_rockets_count = int(input())
shoes_count = int(input())

shoes_price = tennis_rocket_price / 6

rockets_sum = tennis_rockets_count * tennis_rocket_price
shoes_sum = shoes_count * shoes_price
other_stuff = (rockets_sum + shoes_sum) * 0.2

total_sum = rockets_sum + shoes_sum + other_stuff

print(f'Price to be paid by Djokovic {math.floor(total_sum / 8)}')
print(f'Price to be paid by sponsors {math.ceil(total_sum * 7 / 8)}')