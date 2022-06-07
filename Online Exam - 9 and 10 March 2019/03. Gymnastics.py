country = input()
tool = input()

if country == "Russia":
    if tool == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif tool == "hoop":
        difficulty = 9.300
        performance = 9.800
    else:
        difficulty = 9.600
        performance = 9.000
if country == "Bulgaria":
    if tool == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif tool == "hoop":
        difficulty = 9.550
        performance = 9.750
    else:
        difficulty = 9.500
        performance = 9.400
if country == "Italy":
    if tool == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif tool == "hoop":
        difficulty = 9.450
        performance = 9.350
    else:
        difficulty = 9.700
        performance = 9.150

sum = difficulty + performance
print(f'The team of {country} get {sum:.3f} on {tool}.')

percent = 100 - ((sum / 20) * 100)
print(f'{percent:.2f}%')