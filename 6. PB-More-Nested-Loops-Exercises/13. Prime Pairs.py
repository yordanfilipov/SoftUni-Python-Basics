first_pair = int(input())
second_pair = int(input())
first_ceil = int(input())
second_ceil = int(input())

for i in range(first_pair, first_pair + first_ceil + 1):
    for j in range(second_pair, second_pair + second_ceil + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and j % 2 != 0 and j % 3 != 0 and j % 5 != 0 and \
                j % 7 != 0:
            print(f'{i}{j}')
