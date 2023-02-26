start = input("раздел развлечений: ")
if start == "game":
    while True:
        print("Угадай число")
        for i in range(3):
            num = input("Введите чсло:")
            if num == "5":
                print("Вы выиграли билет на концерт!")
                break
            elif num == "off":
                exit(105)