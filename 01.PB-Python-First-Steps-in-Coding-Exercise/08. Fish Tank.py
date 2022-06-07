a = int(input())
b = int(input())
h = int(input())
already_Taken_Percent = float(input())

full_Capacity_dm = (a * b * h) / 1000

water_Percent = 100 - already_Taken_Percent

x = full_Capacity_dm / (water_Percent + already_Taken_Percent)
water_Liters = x * water_Percent

print(water_Liters)
