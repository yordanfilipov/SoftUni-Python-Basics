plane_capacity = float(input())
line = float(input())
suitcases_loaded = 0
taken_capacity = 0

while line != "End":
    luggage_size = float(line)
    suitcases_loaded += 1

    if suitcases_loaded % 3 == 0:
        luggage_size = luggage_size + luggage_size * 0.1

    taken_capacity += luggage_size

    if plane_capacity < taken_capacity:
        print("No more space!")
        suitcases_loaded -= 1
        break

    line = input()


if line == "End":
    print("Congratulations! All suitcases are loaded!")
print(f'Statistic: {suitcases_loaded} suitcases loaded.')