import math
input_hours = int(input())
input_minutes = int(input())

hours = 0
minutes = 0

if input_minutes >= 45 and input_hours == 23:
    minutes = input_minutes - 45
    hours = input_hours - 23
elif input_minutes >= 45 and input_hours != 23:
    minutes = input_minutes - 45
    hours = input_hours + 1
elif input_minutes < 45 and input_hours != 23:
    minutes = input_minutes + 15
    hours = input_hours
elif input_minutes < 45 and input_hours == 23:
    minutes = input_minutes + 15
    hours = input_hours
elif input_minutes < 45 and input_hours == 0:
    minutes = input_minutes + 15
    hours = input_hours
elif input_minutes >= 45 and input_hours == 0:
    minutes = input_minutes + 15
    hours = input_hours
else:
    minutes = input_minutes + 15
    hours = input_hours + 1

minutes = math.floor(minutes)

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')