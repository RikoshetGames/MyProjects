
from players import Player
from utils import load_random_word


def main():

    name = input("Введите имя игрока: ") # Получаем имя игрока
    player = Player(name)  # Создаем экземпляр класса игрока
    random_word = load_random_word("https://jsonkeeper.com/b/LJHI")  # Загружаем случайное слово

    print(f"Привет, {player.name}!\n") # Приветствуем игрока
    print(f"Составьте {len(random_word.subwords)} слов из слова {random_word.word.upper()}.")
    print("Слова должны быть не короче 3 букв.")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop".\n')
    print("Поехали, ваше первое слово?")

    # Бесконечный цикл для ввода слов игроком
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

if __name__ == "__main__":
    main()
