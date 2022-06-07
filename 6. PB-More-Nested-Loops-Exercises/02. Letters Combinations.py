start_letter = input()
end_letter = input()
excluded_letter = input()

start_letter_num = ord(start_letter)
end_letter_num = ord(end_letter)
excluded_letter_num = ord(excluded_letter)
counter = 0

for i in range(start_letter_num, end_letter_num + 1):
    for j in range(start_letter_num, end_letter_num + 1):
        for k in range(start_letter_num, end_letter_num + 1):
            if i == excluded_letter_num or j == excluded_letter_num or k == excluded_letter_num:
                continue
            else:
                counter += 1
                print(f'{chr(i)}{chr(j)}{chr(k)} ', end="")
print(counter)