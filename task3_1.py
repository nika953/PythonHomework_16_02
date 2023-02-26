login = input("Введите логин: ")
symbols = ['=', '?', '*', '^', '$', '№', '@', '_']
for symbol in symbols:
    if symbol in login:
        print(symbol)
