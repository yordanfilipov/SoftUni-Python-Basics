import math
best_record = float(input())
meters = float(input())
seconds_per_meter = float(input())

slowing_meters = meters / 50
slowing_meters = math.floor(slowing_meters)
slowing_meters *= 30

current_record = meters * seconds_per_meter
current_record += slowing_meters
difference = current_record - best_record

if current_record >= best_record:
    print(f'No! He was {difference:.2f} seconds slower.')
else:
    print(f'Yes! The new record is {current_record:.2f} seconds.')