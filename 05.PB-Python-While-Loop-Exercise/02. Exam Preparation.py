bad_grades = int(input())
grade = 0
count_of_bad_grades = 0
problems = 0
score = 0

line = input()
while line != "Enough":

    assignment_name = line
    grade = int(input())
    problems += 1
    score += grade

    if grade <= 4:
        count_of_bad_grades += 1
    if count_of_bad_grades == bad_grades:
        break
    line = input()

if line == "Enough":
    avg_score = score / problems
    print(f'Average score: {avg_score:.2f}')
    print(f'Number of problems: {problems}')
    print(f'Last problem: {assignment_name}')
else:
    print(f"You need a break, {count_of_bad_grades} poor grades.")