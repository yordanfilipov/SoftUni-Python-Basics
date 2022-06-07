one_lev = int(input())
two_lev = int(input())
five_lev = int(input())
lev_sum = int(input())

for one in range(0, one_lev + 1):
    one_sum = one * 1
    for two in range(0, two_lev + 1):
        two_sum = two * 2
        for five in range(0, five_lev + 1):
            five_sum = five * 5
            if one_sum + two_sum + five_sum == lev_sum:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {lev_sum} lv.')