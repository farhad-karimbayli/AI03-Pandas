"""
AI Applications Using Python — Pandas Homework
Главный модуль для последовательного запуска всех 5 заданий.
"""

from tasks.task1_books import run_task1
from tasks.task2_orders import run_task2
from tasks.task3_products import run_task3
from tasks.task4_employees import run_task4
from tasks.task5_tickets import run_task5


def main():
    print("\n" + "#" * 65)
    print("#  КУРС: AI Applications Using Python")
    print("#  ТЕМА: Pandas Data Analysis — Домашнее задание (5 задач)")
    print("#" * 65 + "\n")

    # Задание 1
    run_task1()
    print("\n" + "-" * 60 + "\n")

    # Задание 2
    run_task2()
    print("\n" + "-" * 60 + "\n")

    # Задание 3
    run_task3()
    print("\n" + "-" * 60 + "\n")

    # Задание 4
    run_task4()
    print("\n" + "-" * 60 + "\n")

    # Задание 5
    run_task5()
    print("\n" + "#" * 65)
    print("#  Все 5 заданий успешно выполнены!")
    print("#" * 65 + "\n")


if __name__ == "__main__":
    main()
