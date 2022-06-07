strawberries_Price = float(input())
bananas_weight = float(input())
oranges_weight = float(input())
raspberries_weight = float(input())
strawberries_weight = float(input())

raspberries_Price = strawberries_Price / 2
oranges_Price = raspberries_Price - (raspberries_Price * 0.4)
bananas_Price = raspberries_Price - (raspberries_Price * 0.8)

sum = (strawberries_weight * strawberries_Price) + (bananas_weight * bananas_Price) + (oranges_weight * oranges_Price) + (raspberries_weight * raspberries_Price)

print(sum)