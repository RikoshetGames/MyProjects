from pin import check_pin

user_input = input("Введите ваш Пин-код: ")

if check_pin(user_input):
    print("Такой пин подходит")

else:
    print("Не подходит")