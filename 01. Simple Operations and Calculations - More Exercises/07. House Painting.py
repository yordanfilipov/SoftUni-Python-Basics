x = float(input())
y = float(input())
h = float(input())

roof_area = x * h + 2 * (x * y)
side_area = (x * x * 2) + (x * y * 2)
side_area -= 1.2 * 2 + 2 * 1.5 * 1.5

green_paint = side_area / 3.4
red_paint = roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')