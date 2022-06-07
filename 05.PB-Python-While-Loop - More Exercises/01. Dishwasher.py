dishwasher_bottles = int(input())
line = int(input())

dishwasher_ml = 750 * dishwasher_bottles
counter = 1
dishes = 0
pots = 0

while True:
    current = int(line)

    if counter % 3 == 0:
        pots += current
        dishwasher_ml -= 15 * current
    else:
        dishwasher_ml -= 5 * current
        dishes += current
    if dishwasher_ml < 0:
        dishwasher_ml = abs(dishwasher_ml)
        print(f"Not enough detergent, {dishwasher_ml} ml. more necessary!")
        break

    counter += 1
    line = input()
    if line == "End":
        print("Detergent was enough!")
        print(f'{dishes} dishes and {pots} pots were washed.')
        print(f'Leftover detergent {dishwasher_ml} ml.')
        break
