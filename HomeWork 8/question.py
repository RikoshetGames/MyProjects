class Question:
    def __init__(self, question, complication, right_answer, asked=False, user_answer=None):
        self.question = question
        self.complication = complication
        self.right_answer = right_answer

        self.asked = asked
        self.user_answer = user_answer
        self.points = self.complication * 10

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        :return: количество баллов.
        """
        return self.points


    def is_correct(self):
        """
        Проверяет правильность ответа пользователя.
        :return: True or False.
        """
        return self.user_answer == self.right_answer

    def build_question(self):
        """
        :return: Вопрос и его сложность.
        """
        return (f"Вопрос: {self.question}\n"
                f"Сложность: {self.complication}/5")

    def build_feedback(self):
        """
        :return: Правильный или не правильный ответ.
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.get_points()} баллов."
        else:
            return f"Ответ неверный, верный ответ {self.right_answer}"

    def __str__(self):
        return self.build_question()