all_days = int(input())
total_earned = 0
winner = 0

for day in range(all_days):
    sport_name = input()
    daily_earned = 0
    daily_won = 0
    daily_lost = 0
    while sport_name != "Finish":
        ending_game = input()
        if ending_game == "win":
            daily_won += 1
            daily_earned += 20
            total_earned += 20
        else:
            daily_lost += 1

        sport_name = input()
        if sport_name == "Finish":
            if daily_won > daily_lost:
                bonus = daily_earned * 0.1
                winner += 1
                total_earned += bonus
                break

if winner > (all_days / 2):
    total_earned = total_earned + total_earned * 0.20
    print(f"You won the tournament! Total raised money: {total_earned:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_earned:.2f}")