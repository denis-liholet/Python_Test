"""
test_duration() - декоратор для подсчета времени выполнения теста

logger() - декоратор для логирования имени пользователя, времени, даты
         и продолжительности теста. Результат сохраняется в файл,
         заданный в значении file_path_log

file_path_log - путь к файлу для логгирования

"""


from datetime import datetime

file_path_log = "log.txt"


def test_duration(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        finish = datetime.now()
        time_result = finish - start
        print("You passed the test in " + str(time_result.seconds) + " seconds")
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        login = input("Please, enter your login: ")
        start = datetime.now()
        func(*args, **kwargs)
        finish = datetime.now()
        time_result = finish - start
        with open(file_path_log, "a", encoding="UTF-8") as log:
            log.write("login: " + login + "\n")
            log.write("date: " + str(start.date()) + "\n")
            log.write("time: " + str(start.strftime("%r")) + "\n")
            log.write("test time: " + str(time_result.seconds).strip() + " seconds" + "\n")
            log.write("---------------------------------------------------" + "\n")
    return wrapper
