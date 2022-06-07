import math
easter_breads = int(input())

last_used_sugar = 0
max_sugar = 0
last_used_flour = 0
max_flour = 0
sum_sugar = 0
sum_flour = 0


for packs in range(easter_breads):
    current_sugar = int(input())
    sum_sugar += current_sugar
    if current_sugar > last_used_sugar:
        max_sugar = current_sugar
        last_used_sugar = current_sugar

    current_flour = int(input())
    sum_flour += current_flour
    if current_flour > last_used_flour:
        max_flour = current_flour
        last_used_flour = current_flour

sugar_packs = math.ceil(sum_sugar / 970)
print(f'Sugar: {sugar_packs}')
flour_packs = math.ceil(sum_flour / 750)
print(f'Flour: {flour_packs}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')