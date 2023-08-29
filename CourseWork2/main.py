
from players import Player
from utils import load_random_word, game, hello


def main():
    name = input("Введите имя игрока: ") # Получаем имя игрока
    player = Player(name)  # Создаем экземпляр класса игрока
    random_word = load_random_word("https://jsonkeeper.com/b/LJHI")  # Загружаем случайное слово
    hello(player, random_word)
    game(random_word, player)

if __name__ == "__main__":
    main()
