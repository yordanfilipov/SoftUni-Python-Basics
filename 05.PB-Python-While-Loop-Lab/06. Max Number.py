import sys
num = input()

max_num = -sys.maxsize

while num != "Stop":
    current_number = int(num)

    if current_number > max_num:
        max_num = current_number
    num = input()

print(max_num)
