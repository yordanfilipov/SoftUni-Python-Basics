import math

excursion_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle_price = 2.6
talking_doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2

all_toys_number = number_of_talking_dolls + number_of_minions + number_of_puzzles + number_of_teddy_bears + number_of_trucks

sum_talking_dolls = number_of_talking_dolls * talking_doll_price
sum_minions = number_of_minions * minion_price
sum_puzzles = number_of_puzzles * puzzle_price
sum_teddy_bears = number_of_teddy_bears * teddy_bear_price
sum_trucks = number_of_trucks * truck_price

gained_money = sum_trucks + sum_minions + sum_puzzles + sum_talking_dolls + sum_teddy_bears

if all_toys_number >= 50:
    gained_money = gained_money - (gained_money * 0.25)

gained_money = gained_money - (gained_money * 0.1)

if excursion_price <= gained_money:
    left_money = gained_money - excursion_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    not_enough_money = excursion_price - gained_money
    print(f"Not enough money! {not_enough_money:.2f} lv needed.")
