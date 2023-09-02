
from players import Player
from utils import load_json_keeper, choice_word, start_game, hello_player


def main():
    name = input("Введите имя игрока: ")  # Получаем имя игрока
    player = Player(name)  # Создаем экземпляр класса игрока
    load_word = load_json_keeper("https://jsonkeeper.com/b/LJHI") # Загружаем случайное слово
    random_word = choice_word(load_word) # получаем экземпляр класса BasicWord
    hello_player(player, random_word) # приветствуем игрока
    start_game(random_word, player) # запускаем игру

if __name__ == "__main__":
    main()
