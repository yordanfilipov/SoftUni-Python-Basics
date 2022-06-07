needed_money = int(input())
line = input()
counter = 0
raised_money = 0
cash_payment = 0
credit_card_payment = 0
counter_cash = 0
counter_credit_card = 0

while line != "End":
    current_payment = int(line)
    if counter % 2 == 0:
        if current_payment <= 100:
            raised_money += current_payment
            cash_payment += current_payment
            counter_cash += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if current_payment >= 10:
            raised_money += current_payment
            credit_card_payment += current_payment
            counter_credit_card += 1
            print("Product sold!")
        else:
            print("Error in transaction!")

    counter += 1
    if raised_money >= needed_money:
        cash_payment /= counter_cash
        credit_card_payment /= counter_credit_card
        print(f'Average CS: {cash_payment:.2f}')
        print(f'Average CC: {credit_card_payment:.2f}')
        break

    line = input()
    if line == "End":
        print("Failed to collect required money for charity.")
        break
