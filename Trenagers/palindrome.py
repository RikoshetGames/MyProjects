def is_palindrome(word):
    word = word.replace(" ", "").lower()
    reversed_str = word[::-1]
    if reversed_str == word:
        return True
    else:
        return False

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")