degrees = int(input())
day_type = input()

outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if day_type == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif day_type == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif day_type == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if day_type == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif day_type == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif day_type == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if day_type == "Morning":
            outfit = "T-Shirt"
            shoes = "Sandals"
    elif day_type == "Afternoon":
            outfit = "Swim Suit"
            shoes = "Barefoot"
    elif day_type == "Evening":
            outfit = "Shirt"
            shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")