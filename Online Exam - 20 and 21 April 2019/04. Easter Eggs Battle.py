player_one = int(input())
player_two = int(input())

line = input()

while line != "End of battle":
    if line == "one":
        player_two -= 1
    else:
        player_one -= 1
    if player_one == 0:
        print(f'Player one is out of eggs. Player two has {player_two} eggs left.')
        break
    elif player_two == 0:
        print(f'Player two is out of eggs. Player one has {player_one} eggs left.')
        break
    line = input()

if line == "End of battle":
    print(f"Player one has {player_one} eggs left.")
    print(f"Player two has {player_two} eggs left.")
