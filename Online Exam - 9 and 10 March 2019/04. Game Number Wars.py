first_player_name = input()
second_player_name = input()

line = input()

first_player_points = 0
second_player_points = 0
flag = False

while line != "End of game":
    current_points = 0
    first_player_card = int(line)
    second_player_card = input()
    second_player_card = int(second_player_card)

    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card

    elif first_player_card < second_player_card:
        second_player_points += second_player_card - first_player_card
    else:
        while True:
            first_player_card = int(input())
            second_player_card = int(input())
            if first_player_card > second_player_card:
                first_player_points = first_player_card - second_player_card
                print("Number wars!")
                print(f'{first_player_name} is winner with {first_player_points} points')
                break
            else:
                second_player_points = second_player_card - first_player_card
                print("Number wars!")
                print(f'{second_player_name} is winner with {second_player_points} points')
                break
    line = input()

if line == "End of game":
    print(f'{first_player_name} has {first_player_points} points')
    print(f'{second_player_name} has {second_player_points} points')