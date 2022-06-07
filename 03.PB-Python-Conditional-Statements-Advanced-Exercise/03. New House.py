flower_type = input()
quantity = int(input())
budget = int(input())

rose = 5
dahlia = 3.80
tulip = 2.80
narcissus = 3
gladiolus = 2.50

final_price = 0

if flower_type == "Roses":
    if quantity > 80:
        final_price = quantity * 5
        final_price = final_price - (final_price * 0.1)
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
    else:
        final_price = quantity * 5
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
elif flower_type == "Dahlias":
    if quantity > 90:
        final_price = quantity * 3.80
        final_price = final_price - (final_price * 0.15)
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
    else:
        final_price = quantity * 3.80
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
elif flower_type == "Tulips":
    if quantity > 80:
        final_price = quantity * 2.80
        final_price = final_price - (final_price * 0.15)
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
    else:
        final_price = quantity * 2.80
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
elif flower_type == "Narcissus":
    if quantity < 120:
        final_price = quantity * 3
        final_price = final_price + (final_price * 0.15)
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
    else:
        final_price = quantity * 3
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')
elif flower_type == "Gladiolus":
    if quantity < 80:
        final_price = quantity * 2.50
        final_price = final_price + (final_price * 0.20)
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')

    else:
        final_price = quantity * 2.50
        if budget >= final_price:
            print(f'Hey, you have a great garden with {quantity} {flower_type} and {(budget - final_price):.2f} leva '
                  f'left.')
        else:
            print(f'Not enough money, you need {(final_price - budget):.2f} leva more.')