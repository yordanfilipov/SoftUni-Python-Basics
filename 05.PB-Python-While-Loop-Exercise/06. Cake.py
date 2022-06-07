width = int(input())
length = int(input())

all_pieces = width * length
count_pieces = 0

while count_pieces <= all_pieces:
    line = input()
    if line == "STOP":
        left_pieces = all_pieces - count_pieces
        print(f'{left_pieces} pieces are left.')
        break
    count_pieces += int(line)
    if count_pieces >= all_pieces:
        diff = count_pieces - all_pieces
        print(f'No more cake left! You need {diff} pieces more.')
