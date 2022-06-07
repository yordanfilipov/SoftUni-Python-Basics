month = input()
nights = int(input())

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    price_studio = studio * nights
    price_apartment = apartment * nights
    if nights > 14:
        price_studio = price_studio - (price_studio * 0.3)
        price_apartment = price_apartment - (price_apartment * 0.1)
    elif nights > 7:
        price_studio = price_studio - (price_studio * 0.05)
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    price_studio = studio * nights
    price_apartment = apartment * nights
    if nights > 14:
        price_studio = price_studio - (price_studio * 0.20)
        price_apartment = price_apartment - (price_apartment * 0.1)
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
else:
    studio = 76
    apartment = 77
    price_studio = studio * nights
    price_apartment = apartment * nights
    if nights > 14:
        price_apartment = price_apartment - (price_apartment * 0.1)
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
