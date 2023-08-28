import random

def load_words(path):
    """
    Функция загружает слово из файла.
    :param path: название файла.
    :return: извлеченное слово.
    """
    with open(path, "r", encoding="utf8") as file:
        lines = file.read().strip().split("\n")
    return lines


def shuffle_word(word):
    """
    Функция перемешивает слово.
    :param word: выбранное слово.
    :return: слово после перемешивания.
    """
    return "".join(random.sample(word, len(word)))


def add_record(path, player_name, player_score):
    """
    Функция выводит имя и заработанные баллы.
    :param path: название файла.
    :param player_name: имя игрока.
    :param player_score: количество баллов.
    :return: имя игрока и баллы.
    """
    with open(path, "a", encoding="utf8") as file:
        file.write(f"{player_name}  {player_score}\n")


def get_leader(path):
    """
    Функция определяет лучшего игрока и его рекорд.
    :param path: Название файла
    :return: Количество сыграных игр и максиальное количество баллов.
    """
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
