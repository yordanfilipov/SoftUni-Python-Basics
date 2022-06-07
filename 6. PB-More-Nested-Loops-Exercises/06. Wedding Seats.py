last_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())


ascii_last_sector = ord(last_sector)

counter_seats = 0

for sector in range(65, ascii_last_sector + 1):
    for rows in range(1, first_sector_rows + 1):
        if rows % 2 == 0:
            for seats in range(97, odd_row_seats + 99):
                counter_seats += 1
                print(f'{chr(sector)}{rows}{chr(seats)}')
        else:
            for seats in range(97, odd_row_seats + 97):
                counter_seats += 1
                print(f'{chr(sector)}{rows}{chr(seats)}')
    first_sector_rows += 1
print(counter_seats)
