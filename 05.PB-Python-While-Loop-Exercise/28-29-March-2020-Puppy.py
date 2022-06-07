bought_food = int(input())
bought_food *= 1000

counter_food = 0

line = input()
# while line != "Adopted":
while True:
    if line != "Adopted":
        counter_food += int(line)
        line = input()
    else:
        break

diff = abs(bought_food - counter_food)
if counter_food <= bought_food:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')