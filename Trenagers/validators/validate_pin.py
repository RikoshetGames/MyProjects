def validate_pin(pin):
    if len(pin) == 4 and pin.isdigit():
        return True
    else:
        return False