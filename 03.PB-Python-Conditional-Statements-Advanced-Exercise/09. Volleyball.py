import math
year_type = input()
holidays = int(input())
home_trip = int(input())


saturday_games_sofia = (48 - home_trip)
saturday_games_sofia = saturday_games_sofia * 0.75

holidays = holidays * (2/3)

result = saturday_games_sofia + home_trip + holidays

if year_type == "leap":
    result = result + result * 0.15
else:
    result = result
result = math.floor(result)
print(result)
