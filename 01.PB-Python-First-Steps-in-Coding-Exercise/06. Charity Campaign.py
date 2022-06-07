campaign_Days = int(input())
campaign_Contests = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

sum_cakes = cakes * 45
sum_waffles = waffles * 5.8
sum_pancakes = pancakes * 3.2

per_Contest = campaign_Contests * (sum_cakes + sum_waffles + sum_pancakes)
whole_Sum = per_Contest * campaign_Days
whole_Sum = whole_Sum - whole_Sum / 8

print(whole_Sum)
