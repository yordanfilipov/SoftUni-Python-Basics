budget = int(input())
season = input()
fishermen = int(input())

price_ship = 0

if season == "Summer" or season == "Autumn":
    price_ship = 4200
elif season == "Spring":
    price_ship = 3000
elif season == "Winter":
    price_ship = 2600

if fishermen <= 6:
    price_ship = price_ship - price_ship * 0.1
elif 7 <= fishermen <= 11:
    price_ship = price_ship - price_ship * 0.15
else:
    price_ship = price_ship - price_ship * 0.25

if fishermen % 2 == 0 and season != "Autumn":
    price_ship = price_ship - price_ship * 0.05

if budget >= price_ship:
    enough_money = budget - price_ship
    print(f'Yes! You have {enough_money:.2f} leva left.')
else:
    not_enough = price_ship - budget
    print(f'Not enough money! You need {not_enough:.2f} leva.')