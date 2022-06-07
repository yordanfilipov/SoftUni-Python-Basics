fruit = input()
set_size = input()
sets_count = int(input())

watermelon_price_small = 56
mango_price_small = 36.66
pineapple_price_small = 42.10
raspberry_price_small = 20
watermelon_price_big = 28.70
mango_price_big = 19.60
pineapple_price_big = 24.80
raspberry_price_big = 15.20
big = 5
small = 2
current_price = 0
discount = 0


if fruit == "Watermelon":
    if set_size == "small":
        current_price = sets_count * small * watermelon_price_small
    else:
        current_price = sets_count * big * watermelon_price_big
elif fruit == "Mango":
    if set_size == "small":
        current_price = sets_count * small * mango_price_small
    else:
        current_price = sets_count * big * mango_price_big
elif fruit == "Pineapple":
    if set_size == "small":
        current_price = sets_count * small * pineapple_price_small
    else:
        current_price = sets_count * big * pineapple_price_big
else:
    if set_size == "small":
        current_price = sets_count * small * raspberry_price_small
    else:
        current_price = sets_count * big * raspberry_price_big

if 400 <= current_price <= 1000:
    discount = current_price * 0.15
    current_price -= discount
elif current_price > 1000:
    discount = current_price * 0.5
    current_price -= discount

print(f'{current_price:.2f} lv.')