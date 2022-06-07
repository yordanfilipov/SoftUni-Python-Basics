last_number = int(input())
first_number = int(input())
breaking_number = int(input())

for i in range(first_number, last_number - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == breaking_number:
            break
        print(f'{i}', end=" ")