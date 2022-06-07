import math
guests_number = int(input())
budget = int(input())

easter_breads = math.ceil(guests_number / 3)
easter_breads_price = easter_breads * 4
eggs = guests_number * 2
eggs_price = eggs * 0.45

sum = easter_breads_price + eggs_price

if sum <= budget:
    diff = budget - sum
    print(f'Lyubo bought {easter_breads} Easter bread and {eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    diff = sum - budget
    print("Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')