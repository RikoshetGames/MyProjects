
from basic_word import *
import random
import requests
import urllib3


def load_json_keeper(url):
    """
    Получит список слов с внешнего ресурса.
    :param url: Ссылка на внешний ресурс
    :return: Выведенные данные
    """
    urllib3.disable_warnings()  # Отключаем предупреждения о безопасности SSL-сертификата
    response = requests.get(url=url, verify=False) # Загружаем данные из внешнего ресурса
    random_words = response.json() # Преобразуем данные в формат JSON в список
    if response.status_code == 200: # делаем проверку
        return random_words
    return None


def choice_word(random_words):
    """
    Выберет случайное слово,
    создаст экземпляр класса `BasicWord`,
    вернет этот экземпляр.
    :param random_words: Полученные данные источника.
    :return: Экземпляр класса.
    """
    random_word = random.choice(random_words)  # Выбираем случайное слово из списка
    instance = BasicWord(random_word["word"], random_word["subwords"]) # Создаем экземпляр класса BasicWord
    return instance


def hello_player(player, random_word):
    """
    Выводи приветствие игроку.
    :param player: Имя игрока.
    :param random_word: Загружаемые данные из функции.
    :return: None.
    """
    print(f"Привет, {player.name}!\n") # Приветствуем игрока
    print(f"Составьте {len(random_word.subwords)} слов из слова {random_word.word.upper()}.")
    print("Слова должны быть не короче 3 букв.")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop".\n')
    print("Поехали, ваше первое слово?")




def start_game(random_word, player):
    """
    Выводит вопросы игроку и результат игры.
    :param player: Имя игрока.
    :param random_word: Загружаемые данные из функции.
    :return: None.
    """
    while True:
        word = input().lower()

        # Если введено "stop" или "стоп", то игра завершается
        if word == "stop" or word == "стоп":
            break
        else:
            # Если слово короче 3 букв, выводим сообщение об ошибке
            if len(word) < 3:
                print("Это слишком короткое слово.")
                continue

            # Если введенное слово не является допустимым подсловом, выводим сообщение об ошибке
            if not random_word.is_subword_valid(word):
                print(f"Неверное слово.")
                continue

            # Если слово уже использовано, выводим сообщение об ошибке
            if player.is_word_used(word):
                print("Уже использовано.")
                continue

            # Добавляем использованное подслово в случайное слово и использованное слово в список использованных слов игрока
            random_word.add_used_subword(word)
            player.add_used_word(word)
            print(f"Верно!")

        # Если все подслова случайного слова были угаданы, то игра завершается
        if len(random_word.get_used_subwords()) == len(random_word.subwords):
            break


    print(f"Игра завершена, вы угадали {player.get_used_words()} слов!")