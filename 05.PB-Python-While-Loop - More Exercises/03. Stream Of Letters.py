symbol = input()

is_c = False
is_o = False
is_n = False

word = ""

while symbol != "End":
    if 'a' <= symbol <= 'z' or 'A' <= symbol <= 'Z':
        if symbol != "c" and symbol != "o" and symbol != "n":
            word += symbol
        elif symbol == 'c':
            if not is_c:
                is_c = True
            else:
                word += symbol
        elif symbol == 'o':
            if not is_o:
                is_o = True
            else:
                word += symbol
        elif symbol == 'n':
            if not is_n:
                is_n = True
            else:
                word += symbol
    if is_n == True and is_o == True and is_c == True:
        print(f'{word} ', end="")
        word = ""
        is_c = False
        is_o = False
        is_n = False
    symbol = input()