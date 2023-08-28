import random

def len_words_from_file(path):
    """"""
    with open(path, 'r', encoding='utf8') as file:
       words = file.read().strip().split("\n")
    return words

def shuffle_word(word):
    """"""
    return "".join(random.sample(word, len(word)))

def record_playr (path, player_name, player_count):
    with open(path, 'a', encoding='utf8') as file:
        file.write(f'{player_name}  {player_count}')

def read_history(path):
    max = 0
    count = 0

    with open(path,"r", encoding="utf8") as file:
        for line in file.readlines():
            count += 1
            score = int(line.split("  ")[1])

            if score > max:
                max = score

    return f"Всего игр сыграно: {count}\n" \
           f"Максимальный рекорд: {max}"


words_txt = 'words.txt'
history_txt = 'history.txt'
words = len_words_from_file('words.txt')
user_name = input("Введите ваше имя: ")
count = 0
for word in words:
    shuffle_word(word)
    user_answer = input(f'Угадайте слово: {shuffle_word(word)}')
    if user_answer.lower().strip(" ") == word:
        print(f"Верный ответ! Вы получаете: 10 балов")
        count += 10
    else:
        print(f"Неверно! Верный ответ – {word}")

record_playr(history_txt, user_name, count)
print(read_history(history_txt))