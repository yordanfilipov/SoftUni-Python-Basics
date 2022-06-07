customer_count = int(input())
basket = 1.50
wreath = 3.80
chocolate_bunny = 7

spend_money = 0
bought_items = 0
average_bill = 0

for customer in range(customer_count):
    bought_items = 0
    spend_money = 0
    line = input()
    while True:
        if line == "basket":
            spend_money += basket
        elif line == "wreath":
            spend_money += wreath
        else:
            spend_money += chocolate_bunny
        bought_items += 1

        line = input()
        if line == "Finish":
            if bought_items % 2 == 0:
                spend_money -= spend_money * 0.2
            print(f'You purchased {bought_items} items for {spend_money:.2f} leva.')
            average_bill += spend_money
            break
print(f'Average bill per client is: {(average_bill / customer_count):.2f} leva.')
