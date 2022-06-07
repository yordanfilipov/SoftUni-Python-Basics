n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif 200 <= current_num <= 399:
        p2 += 1
    elif 400 <= current_num <= 599:
        p3 += 1
    elif 600 <= current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

x = 100 / n

print(f'{p1 * x:.2f}%')
print(f'{p2 * x:.2f}%')
print(f'{p3 * x:.2f}%')
print(f'{p4 * x:.2f}%')
print(f'{p5 * x:.2f}%')