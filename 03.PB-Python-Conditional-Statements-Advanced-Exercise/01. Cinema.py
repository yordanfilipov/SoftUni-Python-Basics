screening_type = input()
rows = int(input())
columns = int(input())

income = 0

seats = rows * columns

if screening_type == "Premiere":
    income = seats * 12.00
elif screening_type == "Normal":
    income = seats * 7.50
elif screening_type == "Discount":
    income = seats * 5.00
print(f'{income:.2f} leva')