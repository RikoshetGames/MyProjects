import random

def load_words(path):
    """"""
    with open(path, "r", encoding="utf8") as file:
        lines = file.read().strip().split("\n")
    return lines


def shuffle_word(word):
    """"""
    return "".join(random.sample(word, len(word)))



def add_record(path, player_name, player_score):
    with open(path, "a", encoding="utf8") as file:
        file.write(f"{player_name}  {player_score}\n")


def get_leader(path):
    max = 0
    count = 0

    with open(path,"r", encoding="utf8") as file:
        for line in file.readlines():
            count += 1
            score = int(line.split("  ")[1])
            if score > max:
                max = score
    return f'Всего игр сыграно:{count}\n' \
           f'Максимальный рекорд: {max}'


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