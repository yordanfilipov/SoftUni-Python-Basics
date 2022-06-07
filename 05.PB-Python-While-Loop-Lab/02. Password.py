name = input()
password = input()

current_pass = input()

while password != current_pass:
    current_pass = input()

print(f'Welcome {name}!')