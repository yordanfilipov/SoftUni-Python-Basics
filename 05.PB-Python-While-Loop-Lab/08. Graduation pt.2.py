name = input()
level = 1
grades_sum = 0
is_flanked = False

while level <= 12:
    current_grade = float(input())

    if current_grade < 4.00:
        if is_flanked:
            break

        is_flanked = True
        continue

    level += 1
    grades_sum += current_grade

if level < 12:
    print(f'{name} has been excluded at {level} grade')
else:
    print(f'{name} graduated. Average grade: {grades_sum / 12:.2f}')