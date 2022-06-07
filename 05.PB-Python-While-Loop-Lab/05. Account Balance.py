payment = input()
total = 0.0

while payment != 'NoMoreMoney':
    current_amount = float(payment)

    if current_amount < 0:
        print("Invalid operation!")
        break

    total += current_amount
    print(f'Increase: {current_amount:.2f}')
    payment = input()

print(f'Total: {total:.2f}')