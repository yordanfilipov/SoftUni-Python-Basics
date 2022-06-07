from sys import maxsize

n = int(input())
max_num = -maxsize
sum_numbers = 0

for i in range(n):
    current_num = int(input())
    sum_numbers += current_num
    if current_num > max_num:
        max_num = current_num

new_sum = sum_numbers - max_num

if new_sum == max_num:
    print('Yes')
    print(f'Sum = {new_sum}')
else:
    diff = abs(max_num - new_sum)
    print('No')
    print(f'Diff = {diff}')