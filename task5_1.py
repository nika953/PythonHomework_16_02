while True:
    price = int(input("Введите стоимость: "))
    if price == 0:
        break
    sales = int(input("Введите скидку: "))
    print(price - (sales / 100 * price))