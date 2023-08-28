import random
from function import *

words_txt = "words.txt"
history_txt = "history.txt"

user_name = input("Введите ваше имя: ")
words = load_words("words.txt")

score = 0
for word in words:
    print(f"Угадайте слово: {shuffle_word(word)}")
    user_answer = input()
    if user_answer.lower().strip(" ") == word:
        print("Верно! Вы получаете 10 очковю")
        score += 10
    else:
        print(f"Неверно! Верный ответ - {word}")

add_record(history_txt, user_name, score)
print(get_leader(history_txt))
