n = int(input())
avg = 0
sum = 0

for i in range(n):
    current_number = int(input())
    sum += current_number

avg = sum / n
print(f'{avg:.2f}')