destination = input()
days_reserved = input()
nights = int(input())

if destination == "France":
    if days_reserved == "21-23":
        price = 30
    elif days_reserved == "24-27":
        price = 35
    else:
        price = 40
elif destination == "Italy":
    if days_reserved == "21-23":
        price = 28
    elif days_reserved == "24-27":
        price = 32
    else:
        price = 39
else:
    if days_reserved == "21-23":
        price = 32
    elif days_reserved == "24-27":
        price = 37
    else:
        price = 43

sum = nights * price

print(f'Easter trip to {destination} : {sum:.2f} leva.')
