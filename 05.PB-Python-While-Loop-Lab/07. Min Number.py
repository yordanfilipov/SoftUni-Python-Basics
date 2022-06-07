import sys
num = input()

min_num = sys.maxsize

while num != "Stop":
    current_number = int(num)

    if current_number < min_num:
        min_num = current_number
    num = input()

print(min_num)
