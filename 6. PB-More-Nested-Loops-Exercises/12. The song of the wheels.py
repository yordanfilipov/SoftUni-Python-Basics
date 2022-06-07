control_value = int(input())
counter = 0
password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_value and a < b and c > d:
                    print(f'{a}{b}{c}{d}', end=" ")
                    counter += 1
                    if counter == 4:
                        password = str(a) + str(b) + str(c) + str(d)
if counter >= 4:
    print()
    print(f'Password: {password}')
else:
    print()
    print("No!")