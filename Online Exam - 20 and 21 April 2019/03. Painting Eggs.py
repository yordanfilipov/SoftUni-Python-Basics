egg_size = input()
egg_color = input()
batch_count = int(input())

price = 0

if egg_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    else:
        price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    else:
        price = 7
else:
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    else:
        price = 5

sum = batch_count * price

sum -= sum * 0.35
print(f'{sum:.2f} leva.')