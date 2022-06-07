first_num_max = int(input())
second_num_max = int(input())
third_num_max = int(input())

for first in range(1, first_num_max + 1):
    for second in range(2, second_num_max + 1):
        if second == 4 or second == 6 or second == 8 or second == 9:
            continue
        for third in range(1, third_num_max + 1):
            if first % 2 == 0 and third % 2 == 0:
                print(f"{first} {second} {third}")
