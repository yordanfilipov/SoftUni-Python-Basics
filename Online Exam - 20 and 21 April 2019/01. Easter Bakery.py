flour_price_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_cartons = int(input())
yeast_packs = int(input())

sugar_price_kg = 0.75 * flour_price_kg
egg_carton_price = flour_price_kg * 1.1
yeast_pack_price = 0.20 * sugar_price_kg

sum = (flour_kg * flour_price_kg) + (sugar_kg * sugar_price_kg) + (egg_cartons * egg_carton_price) + (yeast_packs * yeast_pack_price)
print(f'{sum:.2f}')
