num_one = int(input())
num_two = int(input())

for first in range(num_one, num_two + 1):
    for second in range(num_one, num_two + 1):
        for third in range(num_one, num_two + 1):
            for fourth in range(num_one, num_two + 1):
                if first % 2 == 0 and fourth % 2 == 1 and first > fourth and (second + third) % 2 == 0:
                    print(f'{first}{second}{third}{fourth}', end=" ")
                elif first % 2 == 1 and fourth % 2 == 0 and first > fourth and (second + third) % 2 == 0:
                    print(f'{first}{second}{third}{fourth}', end=" ")