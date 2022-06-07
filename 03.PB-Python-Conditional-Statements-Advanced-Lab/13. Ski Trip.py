days = int(input())
room = input()
score = input()

nights = days - 1

room_for_one = 18
apartment = 25
president_apartment = 35

price = 1

if days < 10:
    if room == "room for one person":
        price = room_for_one * nights
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
    elif room == "apartment":
        price = apartment * nights
        price = price - price * 0.30
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
    elif room == "president apartment":
        price = president_apartment * nights
        price = price - price * 0.10
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
elif 10 <= days <= 15:
    if room == "room for one person":
        price = room_for_one * nights
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
    elif room == "apartment":
        price = apartment * nights
        price = price - price * 0.35
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
    elif room == "president apartment":
        price = president_apartment * nights
        price = price - price * 0.15
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
elif days > 15:
    if room == "room for one person":
        price = room_for_one * nights
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
    elif room == "apartment":
        price = apartment * nights
        price = price - price * 0.50
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')
    elif room == "president apartment":
        price = president_apartment * nights
        price = price - price * 0.20
        if score == "positive":
            price = price + price * 0.25
        elif score == "negative":
            price = price - price * 0.10
        print(f'{price:.2f}')