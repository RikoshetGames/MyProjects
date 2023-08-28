from functions import *

while True:
    student_pk = input("Введите номер студента:\n")

    if student_pk == "quit":
        print("Программа завершена.")
        quit()

    elif student_pk.isdigit():
        student = get_student_by_pk(int(student_pk))

        if student:
            print(f"Студент {student['full_name']}")
            print(f"Знает: {', '.join(student['skills'])}")

            while True:
                print(f"Выберите профессию для оценки студента {student['full_name']}:")
                profession_title = input().title()
                profession = get_profession_by_title(profession_title)

                if profession_title == "Quit":
                    print("Программа завершена.")
                    quit()

                elif profession:
                    fitness = check_fitness(student, profession)
                    print(f"{student['full_name']} знает {', '.join(fitness['has'])}")
                    print(f"{student['full_name']} не знает {', '.join(fitness['lacks'])}")
                    print(f"Пригодность {fitness['fit_percent']}%")
                    break

                else:
                    print("У нас нет такой специальности.")
            break
        else:
            print("У нас нет такого студента.")
    else:
        print("Неправильный ввод.")