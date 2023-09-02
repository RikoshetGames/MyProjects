
from players import Player
from utils import load_random_word, start_game, hello_player


def main():
    name = input("Введите имя игрока: ")  # Получаем имя игрока
    player = Player(name)  # Создаем экземпляр класса игрока
    random_word = load_random_word("https://jsonkeeper.com/b/LJHI")  # Загружаем случайное слово
    hello_player(player, random_word)
    start_game(random_word, player)

if __name__ == "__main__":
    main()
