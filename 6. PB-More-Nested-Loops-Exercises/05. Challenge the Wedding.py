males = int(input())
females = int(input())
tables = int(input())

tables_counter = 0
flag = False

for i in range(1, males + 1):
    if flag:
        break
    for j in range(1, females + 1):
        tables_counter += 1
        if tables_counter > tables:
            flag = True
            break
        print(f'({i} <-> {j})', end=" ")


# men_clients = int(input())
# women_clients = int(input())
# tables_max = int(input())
#
# for man in range(1, men_clients + 1):
#     if tables_max == 0:
#         break
#     for woman in range(1, women_clients + 1):
#         tables_max -= 1
#         print(f"({man} <-> {woman})", end=" ")
#         if tables_max == 0:
#             break