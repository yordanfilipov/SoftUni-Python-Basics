people = int(input())
back = 0
chest = 0
legs = 0
abs_ = 0
shake = 0
bar = 0

train = 0
protein = 0

for i in range(people):
    action = input()
    if action == "Back":
        back += 1
        train += 1
    elif action == "Chest":
        chest += 1
        train += 1
    elif action == "Legs":
        legs += 1
        train += 1
    elif action == "Abs":
        abs_ += 1
        train += 1
    elif action == "Protein shake":
        shake += 1
        protein += 1
    else:
        bar += 1
        protein += 1

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs_} - abs')
print(f'{shake} - protein shake')
print(f'{bar} - protein bar')

total_people = train + protein

train_percent = (train / total_people) * 100
protein_percent = (protein / total_people) * 100
print(f'{train_percent:.2f}% - work out')
print(f'{protein_percent:.2f}% - protein')