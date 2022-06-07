guests_number = int(input())
cover_person = float(input())
budget = float(input())

cake_price = budget * 0.1

if 10 <= guests_number <= 15:
    cover_person = cover_person - cover_person * 0.15
elif 15 <= guests_number <= 20:
    cover_person = cover_person - cover_person * 0.20
elif guests_number > 25:
    cover_person = cover_person - cover_person * 0.25

expenses = (guests_number * cover_person) + cake_price


if expenses < budget:
    diff = budget - expenses
    print(f"It is party time! {diff:.2f} leva left.")
else:
    diff = expenses - budget
    print(f"No party! {diff:.2f} leva needed.")