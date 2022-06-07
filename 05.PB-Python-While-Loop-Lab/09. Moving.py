width = int(input())
length = int(input())
height = int(input())
box = input()

room_cub_meters = width * length * height
filled_space = 0

while box != "Done":
    current_box = int(box)
    filled_space += current_box

    if filled_space > room_cub_meters:
        break
    box = input()

if filled_space > room_cub_meters:
    print(f'No more free space! You need {filled_space - room_cub_meters} Cubic meters more.')
else:
    print(f'{room_cub_meters - filled_space} Cubic meters left.')