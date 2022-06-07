money = float(input())
sex = input()
age = int(input())
sport = input()

price = 0

if sport == 'Gym':
    if sex == 'm':
        price = 42
    else:
        price = 35
elif sport == 'Boxing':
    if sex == 'm':
        price = 41
    else:
        price = 37
elif sport == 'Yoga':
    if sex == 'm':
        price = 45
    else:
        price = 42
elif sport == 'Zumba':
    if sex == 'm':
        price = 34
    else:
        price = 31
elif sport == 'Dances':
    if sex == 'm':
        price = 51
    else:
        price = 53
else:
    if sex == 'm':
        price = 39
    else:
        price = 37

if age <= 19:
    price = price - (price * 0.2)

if price < money:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    money = price - money
    print(f'You don\'t have enough money! You need ${money:.2f} more.')