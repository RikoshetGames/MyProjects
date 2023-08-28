import json


def load_data(path: str) -> dict:
    """
    Функция загружает список из файла.
    :param path: Название файла.
    :return: Список из файла.
    """
    with open(path) as file:
        data = json.load(file)
    return data

# print(load_data("professions.json"))

def get_student_by_pk(pk: int) -> dict:
    """
    Функция получает словарь с данными студента по его pk.
    :param pk: Номер студента в списке.
    :return: Словарь с данными студента.
    """
    students = load_data("students.json")
    for student in students:
        if student["pk"] == pk:
            return student
    return None


def get_profession_by_title(title: str) -> dict:
    """
    Функция получает словарь с инфо о профе по названию.
    :param title: Название профессии.
    :return: Словарь с информацией.
    """
    professions = load_data("professions.json")
    for profession in professions:
        if profession["title"] == title:
            return profession
    return None



def check_fitness(student, profession: str) -> dict:
    """
    Функция получает студента и профессию, возвращает словарь
    :param student: Данные из функции get_student_by_pk.
    :param profession: Данные из функции get_profession_by_title.
    :return: Словарь c данными о соответствии студента.
    """
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(student_skills)

    fit_percent = len(has_skills) / len(profession_skills) * 100

    return {
        "has": list(has_skills),
        "lacks": list(lacks_skills),
        "fit_percent": fit_percent
    }