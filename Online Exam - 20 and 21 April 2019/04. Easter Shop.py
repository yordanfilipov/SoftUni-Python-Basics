eggs_stock = int(input())
line = input()
sold_eggs = 0

while line != "Close":
    current_eggs = int(input())
    if line == "Buy":
        eggs_stock -= current_eggs
        sold_eggs += current_eggs
    else:
        eggs_stock += current_eggs
    if eggs_stock < 0:
        print("Not enough eggs in store!")
        print(f'You can buy only {eggs_stock + current_eggs}.')
        break

    line = input()

if line == "Close":
    print("Store is closed!")
    print(f'{sold_eggs} eggs sold.')