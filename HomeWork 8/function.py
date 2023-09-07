import json
import os.path

from question import *
import random

path = "question.json"

def load_question(path):
    """
    Загружает список словарей из файла json.
    :param path: Название файла.
    :return: Список словарей.
    """

    with open(path, "r", encoding="utf8") as file:
        file_question = json.load(file)
    return file_question

def get_question(path):
    """
    Создает список экземпляров класса.
    :param path: Название файла json.
    :return: Список экземпляров класса.
    """
    questions = load_question(path)

    ask = []

    for quest in questions:
        text = quest["q"]
        difficult = int(quest["d"])
        right_answer = quest["a"]
        question = Question(text, difficult, right_answer)
        ask.append(question)
    return ask


def get_random(questions):
    """
    Перемешивает вопросы.
    :param questions: Список вопросов.
    :return: Перемешанный список вопросов.
    """
    random.shuffle(questions)
    return questions

def get_quest(questions):
    """
    Выводит вопросы пользователю и получает ответы.
    :param quest: Вопрос.
    :return: None
    """
    shuffled_questions = get_random(questions)
    for quest in shuffled_questions:
        print(quest.build_question())
        user_answer = input("Введите ответ: ")
        quest.user_answer = user_answer
        print(quest.build_feedback())


def build_stats(questions):
    """
    Собирает статистику правильных ответов и количества баллов.
    :param questions: Список вопросов.
    :return: Строка со значениями статистики.
    """
    points = 0
    count = 0

    for question in questions:
        if question.is_correct():
            points += question.points
            count += 1

    return  f"Вот и всё!\n" \
            f"Отвечено {count} вопроса из {len(questions)}.\n" \
            f"Набрано баллов: {points}"

