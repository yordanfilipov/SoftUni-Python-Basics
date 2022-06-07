import math
control_minutes = int(input())
control_seconds = int(input())
lane_length = float(input())
seconds_for_one_h_meters = int(input())

control_seconds = control_seconds + control_minutes * 60

slower_time = lane_length / 120
slower_time *= 2.5

total_time = (lane_length / 100) * seconds_for_one_h_meters - slower_time

if control_seconds >= total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f'His time is {total_time:.3f}.')
else:
    rounded = total_time - control_seconds
    print(f"No, Marin failed! He was {rounded:.3f} second slower.")