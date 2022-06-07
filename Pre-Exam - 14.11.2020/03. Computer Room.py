month = input()
total_hours_spent = int(input())
total_people = int(input())
day_time = input()

person_money = 0

if month == 'march' or month == 'april' or month == 'may':
    if day_time == 'day':
        person_money = 10.50
    else:
        person_money = 8.40
else:
    if day_time == 'day':
        person_money = 12.60
    else:
        person_money = 10.20

# person_money *= total_hours_spent

if total_people >= 4:
    person_money = person_money - (person_money * 0.1)
if total_hours_spent >= 5:
    person_money = person_money - (person_money * 0.5)

print(f'Price per person for one hour: {person_money:.2f}')
total_cost = person_money * total_hours_spent * total_people
print(f'Total cost of the visit: {total_cost:.2f}')