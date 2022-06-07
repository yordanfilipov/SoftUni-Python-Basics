number = float(input())
input_unit = input()
output_unit = input()

result = 0

if input_unit == "mm" and output_unit == "cm":
    result = number / 10
elif input_unit == "mm" and output_unit == "m":
    result = number / 1000
elif input_unit == "cm" and output_unit == "mm":
    result = number * 10
elif input_unit == "cm" and output_unit == "m":
    result = number / 100
elif input_unit == "m" and output_unit == "cm":
    result = number * 100
elif input_unit == "m" and output_unit == "mm":
    result = number * 1000

print(f'{result:.3f}')
