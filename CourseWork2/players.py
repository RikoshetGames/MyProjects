
class Player:
    def __init__(self, name):
        self.name = name  # имя пользователя
        self.used_words = []  # использованные слова пользователя

    def get_used_words(self):
        """
        :return: Возвращает количество использованных слов.
        """
        return len(self.used_words)

    def add_used_word(self, word):
        """
        Добавляет использованное слово в список.
        :param word: Использованное слово.
        :return: None.
        """
        self.used_words.append(word)

    def is_word_used(self, word):
        """
        Проверяет, было ли слово уже использовано.
        :param word: Использованное слово.
        :return: bool.
        """
        return word in self.used_words

    def __repr__(self):
        return f"Player(name={self.name})"
