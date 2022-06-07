budget = float(input())
statists = int(input())
price_clothes = float(input())

full_price_clothes = statists * price_clothes
decor = budget * 0.1

if statists > 150:
    full_price_clothes = full_price_clothes - (full_price_clothes * 0.1)

spend_money = decor + full_price_clothes

if spend_money > budget:
    not_enough_money = spend_money - budget
    print("Not enough money!")
    print(f'Wingard needs {not_enough_money:.2f} leva more.')
else:
    enough_money = budget - spend_money
    print(f'Action!')
    print(f"Wingard starts filming with {enough_money:.2f} leva left.")
