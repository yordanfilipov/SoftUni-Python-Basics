days_input = int(input())
total_food = float(input())
total_eaten = 0
total_dog_eaten = 0
total_cat_eaten = 0
total_biscuits = 0
total_eaten_day = 0

for i in range(1, days_input + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())

    total_dog_eaten += dog_eaten
    total_cat_eaten += cat_eaten

    if i % 3 == 0:
        total_eaten_day = dog_eaten + cat_eaten
        total_biscuits = total_biscuits + (0.1 * total_eaten_day)
        total_eaten_day = 0

    dog_eaten = 0
    cat_eaten = 0

print(f'Total eaten biscuits: {round(total_biscuits)}gr.')

total_percentage = ((total_dog_eaten + total_cat_eaten) / total_food) * 100 #print

print(f'{total_percentage:.2f}% of the food has been eaten.')

total_eaten = total_dog_eaten + total_cat_eaten

total_dog_eaten = total_dog_eaten / total_eaten
total_cat_eaten = total_cat_eaten / total_eaten


total_dog_eaten *= 100 #print
total_cat_eaten *= 100 #print

print(f'{total_dog_eaten:.2f}% eaten from the dog.')
print(f'{total_cat_eaten:.2f}% eaten from the cat.')