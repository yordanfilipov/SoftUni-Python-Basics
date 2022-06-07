final_stage = input()
ticket_type = input()
ticket_counts = int(input())
trophy_pic = input()

current_price = 0

if final_stage == "Quarter final":
    if ticket_type == "Standard":
        current_price += 55.50
    elif ticket_type == "Premium":
        current_price += 105.20
    else:
        current_price += 118.90
if final_stage == "Semi final":
    if ticket_type == "Standard":
        current_price += 75.88
    elif ticket_type == "Premium":
        current_price += 125.22
    else:
        current_price += 300.40
if final_stage == "Final":
    if ticket_type == "Standard":
        current_price += 110.10
    elif ticket_type == "Premium":
        current_price += 160.66
    else:
        current_price += 400

current_price *= ticket_counts

if current_price > 4000:
    current_price = current_price - current_price * 0.25
elif 2500 < current_price <= 4000:
    current_price = current_price - current_price * 0.10
    if trophy_pic == "Y":
        current_price = current_price + ticket_counts * 40
else:
    if trophy_pic == "Y":
        current_price = current_price + ticket_counts * 40

print(f'{current_price:.2f}')