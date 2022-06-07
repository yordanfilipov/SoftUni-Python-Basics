first_num = int(input())
second_num = int(input())
magical_num = int(input())

counter = 0
flag = False

for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        counter += 1
        if i + j == magical_num:
            flag = True
            print(f'Combination N:{counter} ({i} + {j} = {magical_num})')
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magical_num}')
