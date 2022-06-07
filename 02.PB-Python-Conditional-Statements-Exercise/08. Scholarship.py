import math
income_parent = float(input())
average_score = float(input())
minimum_wage = float(input())

social_scholarship = minimum_wage * 0.35
score_scholarship = average_score * 25

if average_score >= 5.50 and income_parent < minimum_wage:
    if social_scholarship > score_scholarship:
        print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
    else:
        print(f'You get a scholarship for excellent results {math.floor(score_scholarship)} BGN')
elif average_score >= 5.50:
    print(f'You get a scholarship for excellent results {math.floor(score_scholarship)} BGN')
elif average_score > 4.50 and income_parent < minimum_wage:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
else:
    print('You cannot get a scholarship!')