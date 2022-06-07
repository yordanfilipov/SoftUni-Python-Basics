import math
speed = float(input())
liters = float(input())     #per 100 km

total_distance = 384400 * 2
total_time = total_distance / speed
total_time = math.ceil((total_time))

total_time += 3
fuel = (liters * total_distance) / 100

print(total_time)
print(round(fuel))
