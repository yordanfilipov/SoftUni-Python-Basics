import math
processors_count = int(input())
employees_count = int(input())
working_days = int(input())

losses = 0
profit = 0

total_hours = employees_count * working_days * 8
total_processors = math.floor(total_hours / 3)

if total_processors < processors_count:
    losses = processors_count - total_processors
    losses *= 110.10
    print(f'Losses: -> {losses:.2f} BGN')
else:
    profit = total_processors - processors_count
    profit *= 110.10
    print(f'Profit: -> {profit:.2f} BGN')