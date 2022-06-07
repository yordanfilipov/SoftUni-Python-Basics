pens_pack = int(input())
markers_pack = int(input())
board_clean = float(input())
discount = int(input())

pens_price = 5.80
markers_price = 7.20
cleaning_price = 1.20

pens = pens_pack * pens_price
markers = markers_pack * markers_price
clean = board_clean * cleaning_price
sum_without_disc = pens + markers + clean

discount = (discount / 100) * sum_without_disc

sum_with_disc = sum_without_disc - discount

print(f'{sum_with_disc:.3f}')