desired_height = int(input())
starting_height = desired_height - 30

failed_jumps = 0
total_jumps = 0
flag = True

while flag:
    for step in range(starting_height, desired_height + 1, 5):
        current_jump = int(input())
        total_jumps += 1
        while current_jump <= step:
            failed_jumps += 1
            if failed_jumps == 3:
                flag = False
                break
            current_jump = int(input())
            total_jumps += 1
            continue
        if not flag:
            break
        failed_jumps = 0
        if current_jump > desired_height:
            flag = False
            break
        if current_jump > step:
            continue

if failed_jumps < 3:
    print(f'Tihomir succeeded, he jumped over {step}cm after {total_jumps} jumps.')
else:
    print(f'Tihomir failed at {step}cm after {total_jumps} jumps.')