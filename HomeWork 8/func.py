from function import *

if __name__ == "__main__":
    main()

def main():
    """
    Выводит вопрос и получает ответ пользователя.
    Выводит статистику по итогу заданных вопросов.
    """
    questions = get_question("Question.json")
    for question in questions:
        print(question.build_question())
        user_answer = input("Введите ответ ")
        question.user_answer = user_answer
        print(question.build_feedback())

    print(statistics(questions))

def sort_questions(questions):
    """
    Сортирует и выводит вопросы пользователю.
    :param questions: Список вопросов.
    :return: None
    """
    random.shuffle(questions)
    for quest in questions:
        print(quest.build_question())
        user_answer = input("Введите ответ: ")
        quest.user_answer = user_answer
        print(quest.build_feedback())