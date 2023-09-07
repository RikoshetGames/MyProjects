from function import *

def main():
    """
    Основная программа.
    :return: None
    """
    file = "question.json"
    questions = get_question(file)
    get_quest(questions)
    print(build_stats(questions))

if __name__ == "__main__":
    main()