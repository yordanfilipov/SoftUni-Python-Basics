import math
record = float(input())
distance = float(input())
time_per_meter = float(input())

needed_distance = distance * time_per_meter

resistance_time = math.floor(distance / 15 ) * 12.5

ivan_time = needed_distance + resistance_time

if ivan_time < record:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
    print(resistance_time)
else:
    not_enough = ivan_time - record
    print(f"No, he failed! He was {not_enough:.2f} seconds slower.")
    print(resistance_time)