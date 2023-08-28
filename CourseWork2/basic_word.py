
class BasicWord:
    def __init__(self, word, subwords):
        self.word = word # исходное слово
        self.subwords = subwords # набор допустимых подслов
        self.used_subwords = [] # использованные слова

    def add_used_subword(self, subword):
        """
        Добавляет использованное подслово в список.
        :param subword: Набор допустимых подслов.
        :return: None.
        """
        self.used_subwords.append(subword)

    def is_subword_valid(self, subword):
        """
        Проверяет, является ли подслово допустимым.
        :param subword: Набор допустимых подслов.
        :return: Bool.
        """
        return subword in self.subwords

    def get_used_subwords(self):
        """
        Возвращает список использованных подслов.
        :return: Список использованных слов.
        """
        return self.used_subwords

    def __repr__(self):
        return f"BasicWord(word={self.word}, subwords={self.subwords})"
