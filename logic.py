"""

answer_and_questions(input_file_name, output_file_name) - функция, считывающая вопросы
          и принимающая ответы пользователя.
          input_file_name - путь к файлу с вопросами.
          output_file_name - путь к файлу для записи ответов пользователя.

write_to_file(file_name, value: str) - функция, записывающая данные в файл.
         file_name - путь к файлу для записи.
         value: str - записываемое значение, принимает только тип str.

score_counter_and_answer_result_printing(entered_answer, correct_answer, file_name) - функция,
         выводящая на экран результат ответа на текущий вопрос. Также подсчитывает кол-во
         правильных ответов.
         entered_answer - ответ пользователя.
         correct_answer - правильный ответ.
         file_name - путь к файлу, для записи ответа пользователя

score_return() - функция, возвращающая значение количества правильных ответов

counter - переменная, хранящая кол-во правильных ответов

DIV - константа, разделитель для "украшения" вывода в консоль)))

"""


from decorators import test_duration, logger

counter = 0
DIV = "----------------------"


@logger
@test_duration
def answer_and_questions(input_file_name, output_file_name):
    for line in input_file_name:
        user_answer = ''
        print(f"question: {line.strip()}")
        write_to_file(output_file_name, str(line.strip()))
        for _ in range(3):
            print(f"option {input_file_name.readline().strip()}")
        answer = int(input_file_name.readline().split(":")[1].strip())
        try:
            while True:
                user_answer = input("\nPlease, input your choice and press Enter: ")
                user_answer = int(user_answer.strip())
                if 1 <= user_answer <= 3:
                    break
                else:
                    print("Please, enter option from 1 to 3")
        except ValueError:
            print("Oops! You should enter numbers only! Be careful next time!!!")
        score_counter_and_answer_result_printing(user_answer, answer, output_file_name)


def write_to_file(file_name, value: str):
    file_name.write(value)


def score_counter_and_answer_result_printing(entered_answer, correct_answer, file_name):
    if entered_answer == correct_answer:
        print("Correct!" + "\n" + DIV)
        global counter
        counter += 1
        write_to_file(file_name, " --> Correct" + "\n")
    else:
        print("Wrong!" + "\n" + DIV)
        write_to_file(file_name, " --> Wrong" + "\n")


def score_return():
    return counter
