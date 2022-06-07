year_fee = int(input())

sneakers = year_fee - year_fee * 0.4
jersey = sneakers - sneakers * 0.2
ball = jersey / 4
accessories = ball / 5

price = year_fee + sneakers + jersey + ball + accessories
print(f'{price:.2f}')