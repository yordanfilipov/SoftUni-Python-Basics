n = int(input())
sum = 0

for i in range(0, n):
    if i <= n:
        current_number = int(input())
        sum += current_number
print(sum)