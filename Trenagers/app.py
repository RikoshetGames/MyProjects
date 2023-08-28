from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()

validate_card(card_number)
validate_pin(card_pin)

if validate_card(card_number):
    print("Номер карты норм")
else:
    print("Номер косяк")

if validate_pin(card_pin):
    print("Пин норм")
else:
    print("Пин косяк")
