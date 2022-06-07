n = int(input())
washing_mach_price = float(input())
toy_price = int(input())

toy_count = 0
money = 0

for i in range(1, n + 1, 1):
    if i % 2 == 1:
        toy_count += 1
    else:
        money += (i / 2) * 10
        money -= 1

toys_money = toy_count * toy_price

money += toys_money

if money >= washing_mach_price:
    enough_money = money - washing_mach_price
    print(f'Yes! {enough_money:.2f}')
else:
    not_enough_money = washing_mach_price - money
    print(f'No! {not_enough_money:.2f}')