groups_count = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all_the_people = 0

for group in range(groups_count):
    people_count = int(input())
    if people_count <= 5:
        musala += people_count
    elif 6 <= people_count <= 12:
        monblan += people_count
    elif 13 <= people_count <= 25:
        kilimandjaro += people_count
    elif 26 <= people_count <= 40:
        k2 += people_count
    else:
        everest += people_count

    all_the_people += people_count

musala_percentage = (musala / all_the_people) * 100
monblan_percentage = (monblan / all_the_people) * 100
kilimandjaro_percentage = (kilimandjaro / all_the_people) * 100
k2_percentage = (k2 / all_the_people) * 100
everest_percentage = (everest / all_the_people) * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimandjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')

